'use client';

import { useEffect, useMemo, useState } from 'react';

const API_BASE = process.env.NEXT_PUBLIC_API_BASE || 'http://127.0.0.1:8000';

async function getJson(path, token) {
  const headers = token ? { 'x-admin-token': token } : undefined;
  const response = await fetch(`${API_BASE}${path}`, { cache: 'no-store', headers });
  if (!response.ok) {
    throw new Error(`请求失败: ${path} (${response.status})`);
  }
  return response.json();
}

export default function AdminPage() {
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');
  const [sources, setSources] = useState([]);
  const [jobStatus, setJobStatus] = useState(null);
  const [token, setToken] = useState('');

  const enabledCount = useMemo(() => sources.filter((item) => item.enabled).length, [sources]);

  async function loadData() {
    setLoading(true);
    setError('');
    try {
      const [sourcesResult, jobsResult] = await Promise.all([
        getJson('/api/admin/sources', token),
        getJson('/api/admin/jobs/status', token)
      ]);
      setSources(sourcesResult.items || []);
      setJobStatus(jobsResult);
    } catch (err) {
      setError(err.message || '加载失败');
    } finally {
      setLoading(false);
    }
  }

  useEffect(() => {
    loadData();
  }, []);

  return (
    <main>
      <h1>管理面板</h1>
      <div className="card">
        <div className="filters">
          <input
            type="password"
            placeholder="管理员 Token（可选）"
            value={token}
            onChange={(event) => setToken(event.target.value)}
          />
          <button onClick={loadData} disabled={loading}>
            {loading ? '刷新中...' : '刷新状态'}
          </button>
        </div>
        <p>API Base: {API_BASE}</p>
        {error ? <p style={{ color: '#b91c1c' }}>{error}</p> : null}
      </div>

      <div className="card">
        <h2>任务状态</h2>
        {jobStatus ? (
          <>
            <p>
              调度器状态：
              <span className={`badge ${jobStatus.scheduler_running ? 'badge-ok' : 'badge-off'}`}>
                {jobStatus.scheduler_running ? '运行中' : '未运行'}
              </span>
            </p>
            <p>执行间隔（秒）：{jobStatus.interval_seconds}</p>
            <p>服务运行时长（秒）：{jobStatus.uptime_seconds}</p>
          </>
        ) : (
          <p>暂无数据</p>
        )}
      </div>

      <div className="card">
        <h2>来源状态</h2>
        <p>来源总数：{sources.length}，启用：{enabledCount}</p>
        <table className="table">
          <thead>
            <tr>
              <th>名称</th>
              <th>分类</th>
              <th>状态</th>
              <th>Feed</th>
            </tr>
          </thead>
          <tbody>
            {sources.map((source) => (
              <tr key={source.id}>
                <td>{source.name}</td>
                <td>{source.category || '-'}</td>
                <td>
                  <span className={`badge ${source.enabled ? 'badge-ok' : 'badge-off'}`}>
                    {source.enabled ? '启用' : '停用'}
                  </span>
                </td>
                <td>
                  {source.feed_url ? (
                    <a href={source.feed_url} target="_blank" rel="noreferrer">
                      feed
                    </a>
                  ) : (
                    '-'
                  )}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </main>
  );
}
