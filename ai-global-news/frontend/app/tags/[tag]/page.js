import Link from 'next/link';

const API_BASE = process.env.NEXT_PUBLIC_API_BASE || 'http://127.0.0.1:8000';

async function getTagArticles(tag) {
  const params = new URLSearchParams({ tag, limit: '20' });
  const response = await fetch(`${API_BASE}/api/articles?${params.toString()}`, { cache: 'no-store' });

  if (!response.ok) {
    throw new Error(`标签页加载失败 (${response.status})`);
  }

  return response.json();
}

export default async function TagPage({ params }) {
  const tag = decodeURIComponent(params.tag);
  const result = await getTagArticles(tag);
  const items = result.items || [];

  return (
    <main>
      <div className="card">
        <h1>标签：#{tag}</h1>
        <p>匹配文章：{result.total || 0}</p>
        <Link href="/">← 返回资讯流</Link>
      </div>

      <div className="card">
        {items.length === 0 ? (
          <p>该标签暂无文章</p>
        ) : (
          <ul className="news-list">
            {items.map((article) => (
              <li key={article.id} className="news-item">
                <h3>
                  <Link href={`/articles/${article.id}`}>{article.title}</Link>
                </h3>
                <p className="news-meta">来源：{article.source_name || '-'} · 发布时间：{article.published_at || '-'}</p>
                <p>{article.summary || '暂无摘要'}</p>
              </li>
            ))}
          </ul>
        )}
      </div>
    </main>
  );
}
