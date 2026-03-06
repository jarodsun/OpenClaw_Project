from __future__ import annotations

import asyncio
import json
import logging
import time
from uuid import uuid4

from sqlalchemy.exc import IntegrityError

from app.collectors.api import APICollector
from app.collectors.base import CollectorKind
from app.collectors.rss import RSSCollector
from app.collectors.sources import list_high_priority_sources
from app.collectors.web import WEBCollector
from app.core.config import get_settings
from app.core.logging import setup_logging
from app.db.session import SessionLocal
from app.models.article import Article
from app.services.classifier import classify_tags
from app.services.dedup import Deduplicator
from app.services.summarizer import summary_service
from app.services.text_normalizer import normalize_text

settings = get_settings()
setup_logging(settings)
scheduler_logger = logging.getLogger('aign.scheduler')
ingest_logger = logging.getLogger('aign.ingest')


class IngestScheduler:
    def __init__(self, interval_seconds: int = 3600) -> None:
        self.interval_seconds = interval_seconds
        self._task: asyncio.Task[None] | None = None
        self._stopped = asyncio.Event()

    def start(self) -> None:
        if self._task and not self._task.done():
            return
        self._stopped.clear()
        self._task = asyncio.create_task(self._run_loop())
        scheduler_logger.info(
            'scheduler started',
            extra={
                'service': 'scheduler',
                'event': 'scheduler.started',
                'trace_id': '-',
                'extra_data': {'interval_seconds': self.interval_seconds},
            },
        )

    async def stop(self) -> None:
        self._stopped.set()
        if self._task:
            await self._task
        scheduler_logger.info(
            'scheduler stopped',
            extra={
                'service': 'scheduler',
                'event': 'scheduler.stopped',
                'trace_id': '-',
            },
        )

    async def _run_loop(self) -> None:
        while not self._stopped.is_set():
            trace_id = str(uuid4())
            try:
                await asyncio.to_thread(run_ingest_once, trace_id)
            except Exception:
                scheduler_logger.exception(
                    'scheduled ingest failed',
                    extra={
                        'service': 'scheduler',
                        'event': 'scheduler.run.failed',
                        'trace_id': trace_id,
                    },
                )
            try:
                await asyncio.wait_for(self._stopped.wait(), timeout=self.interval_seconds)
            except TimeoutError:
                continue


def _collector_for_kind(kind: CollectorKind):
    if kind == CollectorKind.RSS:
        return RSSCollector()
    if kind == CollectorKind.API:
        return APICollector()
    if kind == CollectorKind.WEB:
        return WEBCollector()
    return None


def _collect_with_retry(collector, source, max_attempts: int, backoff_seconds: float, trace_id: str):
    last_error: Exception | None = None
    for attempt in range(1, max_attempts + 1):
        try:
            return collector.collect(source), attempt - 1
        except Exception as exc:
            last_error = exc
            ingest_logger.warning(
                'collect retry failed',
                extra={
                    'service': 'ingest',
                    'event': 'ingest.source.retry_failed',
                    'trace_id': trace_id,
                    'extra_data': {
                        'source': source.name,
                        'attempt': attempt,
                        'max_attempts': max_attempts,
                        'error': str(exc),
                    },
                },
            )
            if attempt < max_attempts:
                time.sleep(backoff_seconds * attempt)

    if last_error:
        raise last_error
    raise RuntimeError(f'Collect failed for source={source.name}')


def run_ingest_once(trace_id: str | None = None) -> dict[str, int]:
    trace_id = trace_id or str(uuid4())
    sources = [source for source in list_high_priority_sources() if source.kind in {CollectorKind.RSS, CollectorKind.API, CollectorKind.WEB}]
    ingest_logger.info(
        'ingest run started',
        extra={
            'service': 'ingest',
            'event': 'ingest.run.started',
            'trace_id': trace_id,
            'extra_data': {'sources': len(sources)},
        },
    )

    fetched = 0
    inserted = 0
    skipped = 0
    deduped = 0
    collect_retried = 0
    db_retried = 0
    failed_writes = 0
    failed_sources = 0

    with SessionLocal() as db:
        existing_articles = (
            db.query(Article)
            .order_by(Article.ingested_at.desc())
            .limit(500)
            .all()
        )
        deduplicator = Deduplicator(existing_articles=existing_articles)

        for source in sources:
            ingest_logger.info(
                'source ingest started',
                extra={
                    'service': 'ingest',
                    'event': 'ingest.source.started',
                    'trace_id': trace_id,
                    'extra_data': {'source': source.name, 'kind': source.kind.value},
                },
            )
            collector = _collector_for_kind(source.kind)
            if collector is None:
                ingest_logger.warning(
                    'collector missing',
                    extra={
                        'service': 'ingest',
                        'event': 'ingest.source.collector_missing',
                        'trace_id': trace_id,
                        'extra_data': {'source': source.name, 'kind': source.kind.value},
                    },
                )
                failed_sources += 1
                continue

            try:
                articles, retried_count = _collect_with_retry(
                    collector=collector,
                    source=source,
                    max_attempts=settings.ingest_collect_max_attempts,
                    backoff_seconds=settings.ingest_collect_backoff_seconds,
                    trace_id=trace_id,
                )
                collect_retried += retried_count
            except Exception:
                ingest_logger.exception(
                    'collect failed after retries',
                    extra={
                        'service': 'ingest',
                        'event': 'ingest.source.failed',
                        'trace_id': trace_id,
                        'extra_data': {'source': source.name},
                    },
                )
                failed_sources += 1
                continue

            fetched += len(articles)
            ingest_logger.info(
                'source ingest succeeded',
                extra={
                    'service': 'ingest',
                    'event': 'ingest.source.succeeded',
                    'trace_id': trace_id,
                    'extra_data': {
                        'source': source.name,
                        'fetched': len(articles),
                        'collect_retried': retried_count,
                    },
                },
            )
            for item in articles:
                snapshot = deduplicator.build_snapshot(
                    url=item.url,
                    title=normalize_text(item.title) or item.title,
                )
                if deduplicator.is_duplicate(snapshot):
                    deduped += 1
                    skipped += 1
                    continue

                normalized_title = normalize_text(item.title) or item.title
                normalized_summary = normalize_text(item.summary)
                normalized_content = normalize_text(item.content_raw)
                tags = classify_tags(normalized_title, normalized_summary, normalized_content)
                summary = summary_service.generate(
                    title=normalized_title,
                    summary=normalized_summary,
                    content=normalized_content,
                )

                db.add(
                    Article(
                        source_name=item.source_name,
                        title=normalized_title,
                        url=snapshot.canonical_url,
                        author=normalize_text(item.author),
                        language=normalize_text(item.language),
                        tags=json.dumps(tags, ensure_ascii=False),
                        summary=summary,
                        content_raw=normalized_content,
                        published_at=item.published_at,
                    )
                )
                for write_attempt in range(1, settings.ingest_db_max_attempts + 1):
                    try:
                        db.commit()
                        inserted += 1
                        deduplicator.remember(snapshot)
                        break
                    except IntegrityError:
                        db.rollback()
                        skipped += 1
                        deduplicator.remember(snapshot)
                        break
                    except Exception as exc:
                        db.rollback()
                        ingest_logger.warning(
                            'db write retry failed',
                            extra={
                                'service': 'ingest',
                                'event': 'ingest.db.write_retry_failed',
                                'trace_id': trace_id,
                                'extra_data': {
                                    'url': item.url,
                                    'attempt': write_attempt,
                                    'max_attempts': settings.ingest_db_max_attempts,
                                    'error': str(exc),
                                },
                            },
                        )
                        if write_attempt == settings.ingest_db_max_attempts:
                            failed_writes += 1
                            skipped += 1
                        else:
                            db_retried += 1
                            time.sleep(settings.ingest_db_backoff_seconds * write_attempt)

    result = {
        'sources': len(sources),
        'failed_sources': failed_sources,
        'collect_retried': collect_retried,
        'db_retried': db_retried,
        'fetched': fetched,
        'inserted': inserted,
        'deduped': deduped,
        'skipped': skipped,
        'failed_writes': failed_writes,
    }
    ingest_logger.info(
        'ingest run finished',
        extra={
            'service': 'ingest',
            'event': 'ingest.run.finished',
            'trace_id': trace_id,
            'extra_data': result,
        },
    )
    return result
