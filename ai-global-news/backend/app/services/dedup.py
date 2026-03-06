from __future__ import annotations

import re
from dataclasses import dataclass
from typing import TYPE_CHECKING
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

if TYPE_CHECKING:
    from app.models.article import Article

_WORD_RE = re.compile(r"[a-z0-9\u4e00-\u9fff]+", re.IGNORECASE)
_TRACKING_QUERY_KEYS = {
    'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content',
    'utm_id', 'utm_name', 'utm_reader', 'utm_referrer', 'utm_social',
    'gclid', 'fbclid', 'igshid', 'mc_cid', 'mc_eid',
}


def canonicalize_url(url: str) -> str:
    parts = urlsplit((url or '').strip())
    scheme = (parts.scheme or 'https').lower()
    netloc = parts.netloc.lower()
    if netloc.endswith(':80') and scheme == 'http':
        netloc = netloc[:-3]
    if netloc.endswith(':443') and scheme == 'https':
        netloc = netloc[:-4]

    path = re.sub(r'/+', '/', parts.path or '/')
    if len(path) > 1 and path.endswith('/'):
        path = path[:-1]

    query_pairs = [
        (key, value)
        for key, value in parse_qsl(parts.query, keep_blank_values=False)
        if key.lower() not in _TRACKING_QUERY_KEYS
    ]
    query_pairs.sort()
    query = urlencode(query_pairs)

    return urlunsplit((scheme, netloc, path, query, ''))


def title_key(title: str | None) -> str:
    if not title:
        return ''
    words = _WORD_RE.findall(title.lower())
    if not words:
        return ''
    return ' '.join(words)


def simhash64(text: str | None) -> int:
    words = _WORD_RE.findall((text or '').lower())
    if not words:
        return 0

    vector = [0] * 64
    for word in words:
        word_hash = hash(word) & ((1 << 64) - 1)
        for bit in range(64):
            if word_hash & (1 << bit):
                vector[bit] += 1
            else:
                vector[bit] -= 1

    result = 0
    for bit, weight in enumerate(vector):
        if weight >= 0:
            result |= 1 << bit
    return result


def hamming_distance(left: int, right: int) -> int:
    return (left ^ right).bit_count()


@dataclass
class DedupSnapshot:
    canonical_url: str
    title_key: str
    title_hash: int


class Deduplicator:
    def __init__(self, existing_articles: list[Article], max_hamming_distance: int = 3) -> None:
        self._max_hamming_distance = max_hamming_distance
        self._seen_urls: set[str] = set()
        self._seen_titles: set[str] = set()
        self._seen_hashes: list[int] = []

        for article in existing_articles:
            self._register(
                DedupSnapshot(
                    canonical_url=canonicalize_url(article.url),
                    title_key=title_key(article.title),
                    title_hash=simhash64(title_key(article.title)),
                )
            )

    def build_snapshot(self, url: str, title: str | None) -> DedupSnapshot:
        normalized_title = title_key(title)
        return DedupSnapshot(
            canonical_url=canonicalize_url(url),
            title_key=normalized_title,
            title_hash=simhash64(normalized_title),
        )

    def is_duplicate(self, snapshot: DedupSnapshot) -> bool:
        if snapshot.canonical_url in self._seen_urls:
            return True
        if snapshot.title_key and snapshot.title_key in self._seen_titles:
            return True
        if snapshot.title_hash:
            for seen_hash in self._seen_hashes:
                if hamming_distance(snapshot.title_hash, seen_hash) <= self._max_hamming_distance:
                    return True
        return False

    def remember(self, snapshot: DedupSnapshot) -> None:
        self._register(snapshot)

    def _register(self, snapshot: DedupSnapshot) -> None:
        if snapshot.canonical_url:
            self._seen_urls.add(snapshot.canonical_url)
        if snapshot.title_key:
            self._seen_titles.add(snapshot.title_key)
        if snapshot.title_hash:
            self._seen_hashes.append(snapshot.title_hash)
