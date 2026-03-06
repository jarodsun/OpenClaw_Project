import asyncio
import json
import logging
import time
from contextlib import asynccontextmanager
from datetime import UTC, datetime
from uuid import uuid4

from fastapi import Depends, FastAPI, Header, HTTPException, Query, Request
from sqlalchemy import func, or_, select
from sqlalchemy.orm import Session

from app.core.config import get_settings
from app.core.logging import setup_logging
from app.db.session import SessionLocal
from app.models.article import Article
from app.models.source import Source
from app.services.ingest_scheduler import IngestScheduler, run_ingest_once as run_ingest_once_sync


settings = get_settings()
setup_logging(settings)
logger = logging.getLogger('aign.api')
start_time = time.time()
scheduler = IngestScheduler()


@asynccontextmanager
async def lifespan(_: FastAPI):
    scheduler.start()
    yield
    await scheduler.stop()


app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    debug=settings.debug,
    lifespan=lifespan,
)


@app.middleware('http')
async def request_log_middleware(request: Request, call_next):
    trace_id = str(uuid4())
    started = time.perf_counter()
    response = await call_next(request)
    cost_ms = round((time.perf_counter() - started) * 1000, 2)
    response.headers['X-Trace-Id'] = trace_id
    logger.info(
        'api request',
        extra={
            'service': 'api',
            'event': 'api.request',
            'trace_id': trace_id,
            'extra_data': {
                'method': request.method,
                'path': request.url.path,
                'status_code': response.status_code,
                'latency_ms': cost_ms,
            },
        },
    )
    return response


@app.get('/health')
def health() -> dict[str, str | float]:
    return {
        'status': 'ok',
        'env': settings.app_env,
        'version': settings.app_version,
        'timestamp': datetime.now(UTC).isoformat(),
        'uptime_seconds': round(time.time() - start_time, 2),
    }


@app.get('/jobs/ingest/run-once')
async def run_ingest_once() -> dict[str, int]:
    trace_id = str(uuid4())
    logger.info(
        'manual ingest trigger',
        extra={
            'service': 'api',
            'event': 'ingest.run.manual_triggered',
            'trace_id': trace_id,
            'extra_data': {'source': 'api'},
        },
    )
    return await asyncio.to_thread(run_ingest_once_sync, trace_id)


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def verify_admin_token(x_admin_token: str | None = Header(default=None)) -> None:
    if not settings.admin_api_token:
        return
    if x_admin_token != settings.admin_api_token:
        raise HTTPException(status_code=401, detail="admin token invalid")


def _parse_tags(raw_tags: str | None) -> list[str]:
    if not raw_tags:
        return []
    try:
        parsed = json.loads(raw_tags)
        if isinstance(parsed, list):
            return [str(item) for item in parsed if isinstance(item, str)]
    except json.JSONDecodeError:
        logger.warning('article tags is invalid JSON: %s', raw_tags)
    return []


def _serialize_article(article: Article) -> dict[str, object | None]:
    return {
        'id': article.id,
        'source_name': article.source_name,
        'title': article.title,
        'url': article.url,
        'author': article.author,
        'language': article.language,
        'tags': _parse_tags(article.tags),
        'summary': article.summary,
        'published_at': article.published_at.isoformat() if article.published_at else None,
        'ingested_at': article.ingested_at.isoformat(),
    }


@app.get('/api/articles')
def list_articles(
    q: str | None = Query(default=None, min_length=1),
    source: str | None = Query(default=None, min_length=1),
    tag: str | None = Query(default=None, min_length=1),
    published_from: datetime | None = Query(default=None),
    published_to: datetime | None = Query(default=None),
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=20, ge=1, le=100),
    db: Session = Depends(get_db),
) -> dict[str, object]:
    statement = select(Article)

    if source:
        statement = statement.where(Article.source_name == source)
    if q:
        like_pattern = f'%{q}%'
        statement = statement.where(
            or_(
                Article.title.ilike(like_pattern),
                Article.summary.ilike(like_pattern),
                Article.content_raw.ilike(like_pattern),
            )
        )
    if tag:
        statement = statement.where(Article.tags.ilike(f'%"{tag}"%'))
    if published_from:
        statement = statement.where(Article.published_at >= published_from)
    if published_to:
        statement = statement.where(Article.published_at <= published_to)

    total = db.execute(select(func.count()).select_from(statement.subquery())).scalar_one()
    rows = db.execute(
        statement.order_by(Article.ingested_at.desc()).offset(offset).limit(limit)
    ).scalars().all()

    return {
        'total': total,
        'offset': offset,
        'limit': limit,
        'items': [_serialize_article(article) for article in rows],
    }


@app.get('/api/articles/{article_id}')
def article_detail(article_id: int, db: Session = Depends(get_db)) -> dict[str, object | None]:
    article = db.get(Article, article_id)
    if article is None:
        raise HTTPException(status_code=404, detail='article not found')

    result = _serialize_article(article)
    result['content_raw'] = article.content_raw
    return result


@app.get('/api/admin/sources')
def admin_list_sources(
    db: Session = Depends(get_db),
    _: None = Depends(verify_admin_token),
) -> dict[str, object]:
    rows = db.execute(select(Source).order_by(Source.name.asc())).scalars().all()
    return {
        'total': len(rows),
        'items': [
            {
                'id': source.id,
                'name': source.name,
                'category': source.category,
                'homepage_url': source.homepage_url,
                'feed_url': source.feed_url,
                'enabled': source.enabled,
                'updated_at': source.updated_at.isoformat(),
                'note': source.note,
            }
            for source in rows
        ],
    }


@app.get('/api/admin/jobs/status')
def admin_jobs_status(_: None = Depends(verify_admin_token)) -> dict[str, object]:
    task = scheduler._task
    scheduler_running = bool(task and not task.done())
    return {
        'scheduler_running': scheduler_running,
        'interval_seconds': scheduler.interval_seconds,
        'uptime_seconds': round(time.time() - start_time, 2),
    }
