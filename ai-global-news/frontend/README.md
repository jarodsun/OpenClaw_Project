# Frontend (Next.js)

## 启动

```bash
cd frontend
npm install
NEXT_PUBLIC_API_BASE=http://127.0.0.1:8000 npm run dev
```

访问：
- `http://127.0.0.1:3000/`
- `http://127.0.0.1:3000/admin`

## 当前范围

- 已完成：
  - 资讯流页面（`app/page.js`）
  - 详情页（`app/articles/[id]/page.js`）
  - 标签页（`app/tags/[tag]/page.js`）
  - 管理页（`app/admin/page.js`，来源状态、任务状态、鉴权与手动触发）
- 待完成：
  - 前端体验优化（加载态/空态/错误态细化）
  - 设计一致性与可访问性优化
