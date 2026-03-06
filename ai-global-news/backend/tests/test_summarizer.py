import unittest

from app.services.summarizer import SummaryService


class SummaryServiceTestCase(unittest.TestCase):
    def test_generate_prefers_first_sentence(self) -> None:
        service = SummaryService(max_chars=120)
        result = service.generate(
            title='标题',
            summary='这是第一句。这里是第二句。',
            content='补充正文',
        )
        self.assertEqual(result, '这是第一句。')

    def test_generate_fallback_to_title(self) -> None:
        service = SummaryService(max_chars=120)
        result = service.generate(title='只有标题', summary=None, content=None)
        self.assertEqual(result, '只有标题')

    def test_generate_uses_cache(self) -> None:
        service = SummaryService(max_chars=120)
        payload = {
            'title': '缓存标题',
            'summary': '缓存摘要。',
            'content': '缓存正文',
        }
        first = service.generate(**payload)
        second = service.generate(**payload)
        self.assertEqual(first, second)
        self.assertEqual(len(service._cache), 1)


if __name__ == '__main__':
    unittest.main()
