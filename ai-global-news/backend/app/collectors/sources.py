from __future__ import annotations

from app.collectors.base import CollectorKind, SourceConfig


HIGH_PRIORITY_SOURCES: tuple[SourceConfig, ...] = (
    SourceConfig(
        name='OpenAI Blog',
        category='official_blog',
        homepage_url='https://openai.com/news/',
        endpoint='https://openai.com/news/rss.xml',
        kind=CollectorKind.RSS,
    ),
    SourceConfig(
        name='Google DeepMind Blog',
        category='official_blog',
        homepage_url='https://deepmind.google/discover/blog/',
        endpoint='https://deepmind.google/discover/blog/rss.xml',
        kind=CollectorKind.RSS,
    ),
    SourceConfig(
        name='Anthropic News',
        category='official_blog',
        homepage_url='https://www.anthropic.com/news',
        endpoint='https://www.anthropic.com/news/rss.xml',
        kind=CollectorKind.RSS,
    ),
    SourceConfig(
        name='Meta AI Blog',
        category='official_blog',
        homepage_url='https://ai.meta.com/blog/',
        endpoint='https://ai.meta.com/blog/',
        kind=CollectorKind.WEB,
    ),
    SourceConfig(
        name='Azure AI Blog',
        category='official_blog',
        homepage_url='https://azure.microsoft.com/blog/',
        endpoint='https://azure.microsoft.com/en-us/blog/topics/ai-machine-learning/feed/',
        kind=CollectorKind.RSS,
    ),
    SourceConfig(
        name='NVIDIA AI Blog',
        category='official_blog',
        homepage_url='https://blogs.nvidia.com/blog/category/ai/',
        endpoint='https://blogs.nvidia.com/blog/category/ai/feed/',
        kind=CollectorKind.RSS,
    ),
    SourceConfig(
        name='Hugging Face Blog',
        category='official_blog',
        homepage_url='https://huggingface.co/blog',
        endpoint='https://huggingface.co/blog/feed.xml',
        kind=CollectorKind.RSS,
    ),
    SourceConfig(
        name='arXiv AI/ML',
        category='research',
        homepage_url='https://arxiv.org/',
        endpoint='https://export.arxiv.org/api/query?search_query=cat:cs.AI+OR+cat:cs.LG+OR+cat:cs.CL&sortBy=submittedDate&sortOrder=descending&max_results=100',
        kind=CollectorKind.API,
    ),
    SourceConfig(
        name='GitHub Trending AI',
        category='community',
        homepage_url='https://github.com/trending',
        endpoint='https://github.com/trending?since=daily',
        kind=CollectorKind.WEB,
    ),
    SourceConfig(
        name='Hacker News AI',
        category='community',
        homepage_url='https://news.ycombinator.com/',
        endpoint='https://hn.algolia.com/api/v1/search_by_date?query=AI&tags=story',
        kind=CollectorKind.API,
    ),
    SourceConfig(
        name='TechCrunch AI',
        category='media',
        homepage_url='https://techcrunch.com/category/artificial-intelligence/',
        endpoint='https://techcrunch.com/category/artificial-intelligence/feed/',
        kind=CollectorKind.RSS,
    ),
    SourceConfig(
        name='The Verge AI',
        category='media',
        homepage_url='https://www.theverge.com/ai-artificial-intelligence',
        endpoint='https://www.theverge.com/ai-artificial-intelligence/rss/index.xml',
        kind=CollectorKind.RSS,
    ),
)


def list_high_priority_sources() -> list[SourceConfig]:
    return list(HIGH_PRIORITY_SOURCES)
