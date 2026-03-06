import Link from 'next/link';
import { notFound } from 'next/navigation';

const API_BASE = process.env.NEXT_PUBLIC_API_BASE || 'http://127.0.0.1:8000';

async function getArticle(id) {
  const response = await fetch(`${API_BASE}/api/articles/${id}`, { cache: 'no-store' });

  if (response.status === 404) {
    return null;
  }
  if (!response.ok) {
    throw new Error(`资讯详情加载失败 (${response.status})`);
  }

  return response.json();
}

export default async function ArticleDetailPage({ params }) {
  const article = await getArticle(params.id);

  if (!article) {
    notFound();
  }

  return (
    <main>
      <div className="card">
        <h1>{article.title}</h1>
        <p className="news-meta">来源：{article.source_name || '-'} · 发布时间：{article.published_at || '-'}</p>
        <p>{article.summary || '暂无摘要'}</p>
        <p>
          原文：
          <a href={article.url} target="_blank" rel="noreferrer">
            {article.url}
          </a>
        </p>
        <p className="tags-line">
          {(article.tags || []).map((tag) => (
            <Link key={tag} href={`/tags/${encodeURIComponent(tag)}`} className="tag-link">
              #{tag}
            </Link>
          ))}
        </p>
      </div>

      <div className="card">
        <h2>原始内容</h2>
        <pre className="raw-content">{article.content_raw || '无'}</pre>
      </div>

      <Link href="/">← 返回资讯流</Link>
    </main>
  );
}
