import unittest
from dataclasses import dataclass

from app.services.dedup import Deduplicator, canonicalize_url, title_key


@dataclass
class ArticleStub:
    title: str
    url: str


class DedupTests(unittest.TestCase):
    def test_canonicalize_url_removes_tracking_query(self) -> None:
        raw = "https://example.com/news?id=1&utm_source=x&fbclid=abc"
        self.assertEqual(canonicalize_url(raw), "https://example.com/news?id=1")

    def test_title_key_normalizes_spaces_and_case(self) -> None:
        self.assertEqual(title_key(" AI   Breakthrough! "), "ai breakthrough")

    def test_deduplicator_detects_url_duplicate(self) -> None:
        existing = [ArticleStub(title="A", url="https://example.com/a?utm_source=x")]
        dedup = Deduplicator(existing)
        snapshot = dedup.build_snapshot("https://example.com/a", "Another")
        self.assertTrue(dedup.is_duplicate(snapshot))

    def test_deduplicator_detects_title_duplicate(self) -> None:
        existing = [ArticleStub(title="OpenAI launches model", url="https://example.com/a")]
        dedup = Deduplicator(existing)
        snapshot = dedup.build_snapshot("https://example.com/b", "OpenAI   launches MODEL")
        self.assertTrue(dedup.is_duplicate(snapshot))


if __name__ == "__main__":
    unittest.main()
