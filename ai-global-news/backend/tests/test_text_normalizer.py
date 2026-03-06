import unittest

from app.services.text_normalizer import normalize_text


class NormalizeTextTestCase(unittest.TestCase):
    def test_normalize_text_collapses_whitespace_and_null_char(self) -> None:
        raw = "  hello\x00\n\tworld   "
        self.assertEqual(normalize_text(raw), "hello world")

    def test_normalize_text_returns_none_for_blank_text(self) -> None:
        self.assertIsNone(normalize_text(" \n\t "))
        self.assertIsNone(normalize_text(None))


if __name__ == '__main__':
    unittest.main()
