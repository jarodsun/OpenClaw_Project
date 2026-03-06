from __future__ import annotations

import unittest

from app.collectors.base import CollectorKind, SourceConfig
from app.collectors.web import WEBCollector, _AnchorParser


class AnchorParserTests(unittest.TestCase):
    def test_extracts_absolute_and_relative_links(self) -> None:
        parser = _AnchorParser(base_url='https://example.com/news/')
        parser.feed(
            '<a href="/a1"> Article One </a>'
            '<a href="https://foo.bar/p">Article Two</a>'
            '<a href="mailto:test@example.com">Skip Mail</a>'
        )

        self.assertEqual(
            parser.links,
            [
                ('Article One', 'https://example.com/a1'),
                ('Article Two', 'https://foo.bar/p'),
            ],
        )


class WebCollectorTests(unittest.TestCase):
    def test_raises_on_non_web_source(self) -> None:
        collector = WEBCollector()
        source = SourceConfig(
            name='x',
            category='x',
            homepage_url='https://example.com',
            endpoint='https://example.com/feed.xml',
            kind=CollectorKind.RSS,
        )

        with self.assertRaises(ValueError):
            collector.collect(source)


if __name__ == '__main__':
    unittest.main()
