from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from enum import StrEnum
from typing import Protocol


class CollectorKind(StrEnum):
    RSS = 'rss'
    API = 'api'
    WEB = 'web'


@dataclass(slots=True)
class SourceConfig:
    name: str
    category: str
    homepage_url: str
    endpoint: str
    kind: CollectorKind
    timeout_seconds: float = 10.0


@dataclass(slots=True)
class CollectedArticle:
    source_name: str
    title: str
    url: str
    summary: str | None = None
    author: str | None = None
    published_at: datetime | None = None
    language: str | None = None
    content_raw: str | None = None
    fetched_at: datetime = datetime.now(UTC)


class Collector(Protocol):
    kind: CollectorKind

    def collect(self, source: SourceConfig) -> list[CollectedArticle]:
        ...
