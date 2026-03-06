import Link from 'next/link';

const API_BASE = process.env.NEXT_PUBLIC_API_BASE || 'http://127.0.0.1:8000';

async function getArticles(searchParams) {
  const params = new URLSearchParams();
  const q = typeof searchParams.q === 'string' ? searchParams.q.trim() : '';
  const source = typeof searchParams.source === 'string' ? searchParams.source.trim() : '';
  const tag = typeof searchParams.tag === 'string' ? searchParams.tag.trim() : '';

  if (q) params.set('q', q);
  if (source) params.set('source', source);
  if (tag) params.set('tag', tag);
  params.set('limit', '20');

  const response = await fetch(`${API_BASE}/api/articles?${params.toString()}`, {
    cache: 'no-store',
  });

  if (!response.ok) {
    throw new Error(`资讯列表加载失败 (${response.status})`);
  }

  return response.json();
}

export default async function HomePage({ searchParams }) {
  const result = await getArticles(searchParams || {});
  const items = result.items || [];

  return (
    <main>
      <h1>AI Global News</h1>

      <div className="card">
        <form className="filters" method="get">
          <input name="q" placeholder="关键词（标题/摘要）" defaultValue={searchParams?.q || ''} />
          <input name="source" placeholder="来源（如 OpenAI）" defaultValue={searchParams?.source || ''} />
          <input name="tag" placeholder="标签（如 llm）" defaultValue={searchParams?.tag || ''} />
          <button type="submit">筛选</button>
          <Link href="/">重置</Link>
          <Link href="/admin">管理页</Link>
        </form>
      </div>

      <div className="card">
        <h2>资讯流</h2>
        <p>共 {result.total || 0} 条，当前展示 {items.length} 条</p>
        {items.length === 0 ? (
          <p>暂无数据</p>
        ) : (
          <ul className="news-list">
            {items.map((article) => (
              <li key={article.id} className="news-item">
                <h3>
                  <Link href={`/articles/${article.id}`}>{article.title}</Link>
                </h3>
                <p className="news-meta">
                  来源：{article.source_name || '-'} · 发布时间：{article.published_at || '-'}
                </p>
                <p>{article.summary || '暂无摘要'}</p>
                <p className="tags-line">
                  {(article.tags || []).map((oneTag) => (
                    <Link key={`${article.id}-${oneTag}`} href={`/tags/${encodeURIComponent(oneTag)}`} className="tag-link">
                      #{oneTag}
                    </Link>
                  ))}
                </p>
              </li>
            ))}
          </ul>
        )}
      </div>
    </main>
  );
}
