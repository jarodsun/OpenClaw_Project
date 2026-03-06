# backend

FastAPI 后端骨架。

## 快速开始

1. 创建虚拟环境并安装依赖：
   - `python3 -m venv .venv`
   - `source .venv/bin/activate`
   - `pip install -r requirements.txt`
2. 配置环境变量：
   - `cp .env.example .env`
   - 默认已使用 SQLite（`AIGN_DATABASE_URL=sqlite:///./ai_global_news_dev.db`）
3. 执行迁移：
   - `alembic upgrade head`
4. 启动服务：
   - `uvicorn app.main:app --reload`
5. 健康检查：
   - `GET /health`

## 配置体系（env/dev/prod）

- 统一前缀：`AIGN_`
- 环境变量：`AIGN_APP_ENV`
  - `dev`：默认开发配置（`debug=true`，`log_level=DEBUG`）
  - `prod`：生产配置（`debug=false`，`log_level=INFO`）
- 数据库连接：`AIGN_DATABASE_URL`
  - 默认开发：`sqlite:///./ai_global_news_dev.db`
  - 生产建议（当前统一 SQLite3）：`sqlite:///./ai_global_news_dev.db`
- 配置入口：`app/core/config.py`
- 运行时可通过 `/health` 返回的 `env`、`version`、`uptime_seconds` 字段确认当前状态。

## 基础日志

- 启动时根据 `AIGN_LOG_LEVEL` 初始化标准库 logging。
- 每个 HTTP 请求输出方法、路径、状态码、耗时（毫秒）。

## 采集器接口（Phase 2）

- 抽象定义：`app/collectors/base.py`
  - `CollectorKind`：支持 `rss/api/web`
  - `SourceConfig`：统一来源配置（名称、分类、endpoint、超时）
  - `CollectedArticle`：统一采集结果结构
  - `Collector`：采集器协议（`collect`）
- RSS 实现：`app/collectors/rss.py`
  - 基于标准库 `urllib + ElementTree` 拉取并解析 RSS
  - 输出统一 `CollectedArticle` 列表
- 暂未接入调度与数据库写入，当前用于后续来源接入的接口基线。
