from __future__ import annotations

from datetime import UTC, datetime
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse
from urllib.request import Request, urlopen

from app.collectors.base import CollectedArticle, CollectorKind, SourceConfig


class WEBCollector:
    kind = CollectorKind.WEB

    def collect(self, source: SourceConfig) -> list[CollectedArticle]:
        if source.kind != CollectorKind.WEB:
            raise ValueError(f'WEBCollector only supports web source, got={source.kind}')

        request = Request(
            source.endpoint,
            headers={
                'User-Agent': 'ai-global-news/0.1 (+https://local.ai-global-news)',
                'Accept': 'text/html,application/xhtml+xml;q=0.9,*/*;q=0.8',
            },
        )
        with urlopen(request, timeout=source.timeout_seconds) as response:
            payload = response.read().decode('utf-8', errors='ignore')

        parser = _AnchorParser(base_url=source.homepage_url)
        parser.feed(payload)

        results: list[CollectedArticle] = []
        seen_urls: set[str] = set()
        for title, url in parser.links:
            if url in seen_urls:
                continue
            seen_urls.add(url)
            results.append(
                CollectedArticle(
                    source_name=source.name,
                    title=title,
                    url=url,
                    content_raw=None,
                    fetched_at=datetime.now(UTC),
                )
            )

        return results


class _AnchorParser(HTMLParser):
    def __init__(self, base_url: str) -> None:
        super().__init__(convert_charrefs=True)
        self.base_url = base_url
        self.links: list[tuple[str, str]] = []
        self._href: str | None = None
        self._text_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != 'a':
            return
        attr_map = dict(attrs)
        href = attr_map.get('href')
        if not href:
            return
        self._href = href.strip()
        self._text_parts = []

    def handle_data(self, data: str) -> None:
        if self._href is None:
            return
        cleaned = ' '.join(data.split())
        if cleaned:
            self._text_parts.append(cleaned)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() != 'a' or self._href is None:
            return

        title = ' '.join(self._text_parts).strip()
        resolved = urljoin(self.base_url, self._href)
        self._href = None
        self._text_parts = []

        if not title:
            return
        parsed = urlparse(resolved)
        if parsed.scheme not in {'http', 'https'}:
            return

        self.links.append((title, resolved))
