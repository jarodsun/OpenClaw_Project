import unittest

from app.services.classifier import classify_tags


class ClassifierTests(unittest.TestCase):
    def test_classify_tags_matches_multiple_rules(self) -> None:
        tags = classify_tags('OpenAI 发布新 GPT 推理模型', 'model release with lower latency')
        self.assertIn('llm', tags)
        self.assertIn('infra', tags)
        self.assertIn('product', tags)

    def test_classify_tags_returns_general_for_empty_text(self) -> None:
        self.assertEqual(classify_tags(None, '   '), ['general'])


if __name__ == '__main__':
    unittest.main()
