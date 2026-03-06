from __future__ import annotations

import asyncio
import logging
from sqlalchemy.exc import IntegrityError

from app.collectors.base import CollectorKind
from app.collectors.rss import RSSCollector
from app.collectors.sources import list_high_priority_sources
from app.db.session import SessionLocal
from app.models.article import Article

logger = logging.getLogger(__name__)


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
        logger.info('Ingest scheduler started, interval=%ss', self.interval_seconds)

    async def stop(self) -> None:
        self._stopped.set()
        if self._task:
            await self._task
        logger.info('Ingest scheduler stopped')

    async def _run_loop(self) -> None:
        while not self._stopped.is_set():
            try:
                await asyncio.to_thread(run_ingest_once)
            except Exception:
                logger.exception('Ingest cycle failed')
            try:
                await asyncio.wait_for(self._stopped.wait(), timeout=self.interval_seconds)
            except TimeoutError:
                continue


def run_ingest_once() -> dict[str, int]:
    collector = RSSCollector()
    sources = [source for source in list_high_priority_sources() if source.kind == CollectorKind.RSS]

    fetched = 0
    inserted = 0
    skipped = 0

    with SessionLocal() as db:
        for source in sources:
            try:
                articles = collector.collect(source)
            except Exception:
                logger.exception('Collect failed for source=%s', source.name)
                continue

            fetched += len(articles)
            for item in articles:
                db.add(
                    Article(
                        source_name=item.source_name,
                        title=item.title,
                        url=item.url,
                        author=item.author,
                        language=item.language,
                        content_raw=item.content_raw,
                        published_at=item.published_at,
                    )
                )
                try:
                    db.commit()
                    inserted += 1
                except IntegrityError:
                    db.rollback()
                    skipped += 1

    result = {'sources': len(sources), 'fetched': fetched, 'inserted': inserted, 'skipped': skipped}
    logger.info('Ingest cycle done: %s', result)
    return result
