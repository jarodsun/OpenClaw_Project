from __future__ import annotations

import json
from datetime import UTC, datetime
from urllib.request import Request, urlopen
from xml.etree import ElementTree as ET

from app.collectors.base import CollectedArticle, CollectorKind, SourceConfig


class APICollector:
    kind = CollectorKind.API

    def collect(self, source: SourceConfig) -> list[CollectedArticle]:
        if source.kind != CollectorKind.API:
            raise ValueError(f'APICollector only supports api source, got={source.kind}')

        request = Request(
            source.endpoint,
            headers={
                'User-Agent': 'ai-global-news-bot/0.1 (+https://example.local)',
                'Accept': 'application/json, application/atom+xml, application/xml, text/xml;q=0.9,*/*;q=0.8',
            },
        )
        with urlopen(request, timeout=source.timeout_seconds) as response:
            body = response.read()
            content_type = (response.headers.get('Content-Type') or '').lower()

        if 'json' in content_type or source.endpoint.startswith('https://hn.algolia.com/'):
            return self._collect_hn(source, body)

        return self._collect_arxiv(source, body)

    def _collect_hn(self, source: SourceConfig, body: bytes) -> list[CollectedArticle]:
        payload = json.loads(body.decode('utf-8'))
        hits = payload.get('hits', [])

        results: list[CollectedArticle] = []
        for item in hits:
            title = item.get('title') or item.get('story_title')
            url = item.get('url') or item.get('story_url')
            if not title or not url:
                continue

            published_at = _parse_datetime(item.get('created_at'))
            results.append(
                CollectedArticle(
                    source_name=source.name,
                    title=title.strip(),
                    url=url,
                    summary=(item.get('story_text') or item.get('comment_text')),
                    author=item.get('author'),
                    published_at=published_at,
                    content_raw=item.get('_highlightResult', {}).get('title', {}).get('value'),
                )
            )
        return results

    def _collect_arxiv(self, source: SourceConfig, body: bytes) -> list[CollectedArticle]:
        root = ET.fromstring(body)
        ns = {'atom': 'http://www.w3.org/2005/Atom'}

        results: list[CollectedArticle] = []
        for entry in root.findall('atom:entry', ns):
            title = _node_text(entry, 'atom:title', ns)
            url = _entry_link(entry, ns)
            if not title or not url:
                continue

            summary = _node_text(entry, 'atom:summary', ns)
            author = _node_text(entry, 'atom:author/atom:name', ns)
            published_at = _parse_datetime(_node_text(entry, 'atom:published', ns))

            results.append(
                CollectedArticle(
                    source_name=source.name,
                    title=' '.join(title.split()),
                    url=url,
                    summary=' '.join(summary.split()) if summary else None,
                    author=author,
                    published_at=published_at,
                    content_raw=ET.tostring(entry, encoding='unicode'),
                )
            )
        return results


def _node_text(node: ET.Element, path: str, ns: dict[str, str]) -> str | None:
    child = node.find(path, ns)
    if child is None or child.text is None:
        return None
    return child.text.strip()


def _entry_link(entry: ET.Element, ns: dict[str, str]) -> str | None:
    for link in entry.findall('atom:link', ns):
        href = link.attrib.get('href')
        rel = link.attrib.get('rel')
        if href and (rel is None or rel == 'alternate'):
            return href
    return None


def _parse_datetime(raw: str | None) -> datetime | None:
    if not raw:
        return None
    value = raw.strip()
    if value.endswith('Z'):
        value = value[:-1] + '+00:00'
    try:
        dt = datetime.fromisoformat(value)
    except ValueError:
        return None
    if dt.tzinfo is None:
        return dt.replace(tzinfo=UTC)
    return dt.astimezone(UTC)
