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

## 日志机制（结构化 + 分文件）

- 默认启用 JSON 结构化日志，公共字段包含：`ts`、`level`、`service`、`trace_id`、`event`、`message`、`extra`。
- 日志目录：`AIGN_LOG_DIR`（默认 `backend/logs`）。
- 日志轮转：`AIGN_LOG_MAX_BYTES`（默认 10MB）+ `AIGN_LOG_BACKUP_COUNT`（默认 7）。
- 分文件输出：
  - `app.log`：API 请求与应用日志
  - `ingest.log`：采集链路（来源级成功/失败、重试、入库）
  - `scheduler.log`：调度启动/停止与周期任务结果
- 每次 API 请求会返回 `X-Trace-Id`，可用于全链路排查。

常用查看命令：
- `tail -f logs/app.log`
- `tail -f logs/ingest.log`
- `tail -f logs/scheduler.log`

## 文本清洗（Phase 3 启动）

- 清洗模块：`app/services/text_normalizer.py`
  - 去除 `\x00` 空字符
  - 统一压缩空白符（空格/换行/制表）
  - 空白内容归一化为 `None`
- 入库前在 `ingest_scheduler` 对 `title/author/language/content_raw` 做基础规范化。

## 摘要生成（Phase 3 完成）

- 摘要服务：`app/services/summarizer.py`
  - 优先提炼首句生成摘要
  - 失败自动降级到 `summary/content/title`
  - 内置 LRU 缓存，避免重复文本重复计算
- 入库链路：`ingest_scheduler` 已将摘要写入 `articles.summary` 字段。
- 迁移脚本：`alembic/versions/20260306_2040_add_article_summary.py`

## 采集器接口（Phase 2）

- 抽象定义：`app/collectors/base.py`
  - `CollectorKind`：支持 `rss/api/web`
  - `SourceConfig`：统一来源配置（名称、分类、endpoint、超时）
  - `CollectedArticle`：统一采集结果结构
  - `Collector`：采集器协议（`collect`）
- RSS 实现：`app/collectors/rss.py`
  - 基于标准库 `urllib + ElementTree` 拉取并解析 RSS
  - 输出统一 `CollectedArticle` 列表
- API 实现：`app/collectors/api.py`
  - 支持 `hn.algolia.com` JSON 与 arXiv Atom API 解析
  - 输出统一 `CollectedArticle` 列表
- 调度执行：`app/services/ingest_scheduler.py`
  - 已接入 `rss + api + web` 来源执行链路
  - 支持手动触发接口：`GET /jobs/ingest/run-once`
  - 入库失败重试支持指数退避（`AIGN_INGEST_DB_BACKOFF_SECONDS`）
  - 运行结果包含重试与失败写入统计（如 `db_retried`、`failed_writes`）

## 首批 12 来源种子数据（Phase 2 推进）

- 来源定义：`app/collectors/sources.py`
- 入库脚本：`scripts/seed_high_priority_sources.py`
- 执行方式（在 `backend/` 目录）：
  - `python3 -m app.main`（可选，先验证环境）
  - `python3 scripts/seed_high_priority_sources.py`

脚本会按来源名称进行幂等更新：
- 新来源不存在时创建
- 已存在来源会更新分类、主页、RSS 地址与采集器类型备注
