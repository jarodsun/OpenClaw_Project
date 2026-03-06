from __future__ import annotations

from datetime import UTC, datetime
from email.utils import parsedate_to_datetime
from urllib.request import Request, urlopen
from xml.etree import ElementTree

from app.collectors.base import CollectedArticle, CollectorKind, SourceConfig


class RSSCollector:
    kind = CollectorKind.RSS

    def collect(self, source: SourceConfig) -> list[CollectedArticle]:
        if source.kind != CollectorKind.RSS:
            raise ValueError(f'RSSCollector only supports rss source, got={source.kind}')

        request = Request(
            source.endpoint,
            headers={
                'User-Agent': 'ai-global-news/0.1 (+https://local.ai-global-news)',
            },
        )
        with urlopen(request, timeout=source.timeout_seconds) as response:
            payload = response.read()

        root = ElementTree.fromstring(payload)
        items = root.findall('.//item')
        articles: list[CollectedArticle] = []
        for item in items:
            title = _text(item, 'title')
            url = _text(item, 'link')
            if not title or not url:
                continue

            articles.append(
                CollectedArticle(
                    source_name=source.name,
                    title=title,
                    url=url,
                    summary=_text(item, 'description'),
                    author=_text(item, 'author') or _text(item, '{http://purl.org/dc/elements/1.1/}creator'),
                    published_at=_parse_datetime(_text(item, 'pubDate')),
                    content_raw=_text(item, '{http://purl.org/rss/1.0/modules/content/}encoded'),
                    fetched_at=datetime.now(UTC),
                )
            )
        return articles


def _text(element: ElementTree.Element, tag: str) -> str | None:
    node = element.find(tag)
    if node is None or node.text is None:
        return None
    return node.text.strip() or None


def _parse_datetime(raw_value: str | None) -> datetime | None:
    if not raw_value:
        return None
    try:
        dt = parsedate_to_datetime(raw_value)
    except (TypeError, ValueError, IndexError):
        return None
    if dt.tzinfo is None:
        return dt.replace(tzinfo=UTC)
    return dt.astimezone(UTC)
