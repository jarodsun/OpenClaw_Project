import unittest
from datetime import datetime

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool

from app.db.base import Base
from app.main import app, get_db
from app.models.article import Article
from app.models.source import Source


class ArticleApiTests(unittest.TestCase):
    def setUp(self) -> None:
        self.engine = create_engine(
            'sqlite+pysqlite://',
            connect_args={'check_same_thread': False},
            poolclass=StaticPool,
        )
        self.testing_session_local = sessionmaker(
            bind=self.engine, autocommit=False, autoflush=False
        )
        Base.metadata.create_all(bind=self.engine)

        def override_get_db():
            db = self.testing_session_local()
            try:
                yield db
            finally:
                db.close()

        app.dependency_overrides[get_db] = override_get_db
        self.client = TestClient(app)
        self._seed_sources()
        self._seed_articles()

    def tearDown(self) -> None:
        app.dependency_overrides.clear()
        Base.metadata.drop_all(bind=self.engine)
        self.engine.dispose()

    def _seed_sources(self) -> None:
        with self.testing_session_local() as db:
            db.add_all(
                [
                    Source(
                        name='OpenAI',
                        category='llm',
                        homepage_url='https://openai.com',
                        feed_url='https://openai.com/news/rss.xml',
                        enabled=True,
                        note='primary',
                    ),
                    Source(
                        name='Anthropic',
                        category='llm',
                        homepage_url='https://anthropic.com',
                        feed_url='https://anthropic.com/news/rss.xml',
                        enabled=False,
                        note=None,
                    ),
                ]
            )
            db.commit()

    def _seed_articles(self) -> None:
        with self.testing_session_local() as db:
            db.add_all(
                [
                    Article(
                        source_name='OpenAI',
                        title='OpenAI 发布多模态 Agent',
                        url='https://example.com/a1',
                        author='team',
                        language='zh',
                        tags='["llm", "agent"]',
                        summary='这是第一条摘要。',
                        content_raw='正文A',
                        published_at=datetime(2026, 3, 6, 10, 0, 0),
                        ingested_at=datetime(2026, 3, 6, 10, 5, 0),
                    ),
                    Article(
                        source_name='Anthropic',
                        title='Claude 新版本发布',
                        url='https://example.com/a2',
                        author='lab',
                        language='en',
                        tags='["llm"]',
                        summary='Second summary.',
                        content_raw='正文B',
                        published_at=datetime(2026, 3, 6, 11, 0, 0),
                        ingested_at=datetime(2026, 3, 6, 11, 5, 0),
                    ),
                    Article(
                        source_name='OpenAI',
                        title='OpenAI Agent 平台更新',
                        url='https://example.com/a3',
                        author='team',
                        language='zh',
                        tags='["llm", "infra"]',
                        summary='第三条摘要。',
                        content_raw='正文C',
                        published_at=datetime(2026, 3, 6, 12, 0, 0),
                        ingested_at=datetime(2026, 3, 6, 12, 5, 0),
                    ),
                ]
            )
            db.commit()

    def test_list_articles_with_filters(self) -> None:
        response = self.client.get('/api/articles', params={'q': 'Claude', 'tag': 'llm'})
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload['total'], 1)
        self.assertEqual(len(payload['items']), 1)
        self.assertEqual(payload['items'][0]['source_name'], 'Anthropic')

    def test_list_articles_with_published_range(self) -> None:
        response = self.client.get(
            '/api/articles',
            params={
                'published_from': '2026-03-06T10:30:00',
                'published_to': '2026-03-06T11:10:00',
            },
        )
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload['total'], 1)
        self.assertEqual(payload['items'][0]['title'], 'Claude 新版本发布')

    def test_list_articles_with_combined_filters_and_order(self) -> None:
        response = self.client.get(
            '/api/articles',
            params={
                'source': 'OpenAI',
                'tag': 'llm',
                'published_from': '2026-03-06T09:00:00',
                'published_to': '2026-03-06T12:30:00',
            },
        )
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload['total'], 2)
        self.assertEqual(
            [item['title'] for item in payload['items']],
            ['OpenAI Agent 平台更新', 'OpenAI 发布多模态 Agent'],
        )

    def test_article_detail_success(self) -> None:
        response = self.client.get('/api/articles/1')
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload['id'], 1)
        self.assertEqual(payload['tags'], ['llm', 'agent'])
        self.assertEqual(payload['content_raw'], '正文A')

    def test_article_detail_not_found(self) -> None:
        response = self.client.get('/api/articles/999')
        self.assertEqual(response.status_code, 404)

    def test_admin_list_sources(self) -> None:
        response = self.client.get('/api/admin/sources')
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload['total'], 2)
        self.assertEqual([item['name'] for item in payload['items']], ['Anthropic', 'OpenAI'])
        self.assertFalse(payload['items'][0]['enabled'])

    def test_admin_jobs_status(self) -> None:
        response = self.client.get('/api/admin/jobs/status')
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertIn('scheduler_running', payload)
        self.assertIn('interval_seconds', payload)
        self.assertIn('uptime_seconds', payload)


if __name__ == '__main__':
    unittest.main()
