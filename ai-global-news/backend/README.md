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
  - 生产建议：`mysql+pymysql://user:pass@host:3306/db`
- 配置入口：`app/core/config.py`
- 运行时可通过 `/health` 返回的 `env` 字段确认当前环境。
