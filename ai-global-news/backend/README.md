# backend

FastAPI 后端骨架。

## 快速开始

1. 创建虚拟环境并安装依赖：
   - `python3 -m venv .venv`
   - `source .venv/bin/activate`
   - `pip install -r requirements.txt`
2. 配置环境变量：
   - `cp .env.example .env`
   - 按需修改 `AIGN_*` 配置
3. 启动服务：
   - `uvicorn app.main:app --reload`
4. 健康检查：
   - `GET /health`

## 配置体系（env/dev/prod）

- 统一前缀：`AIGN_`
- 环境变量：`AIGN_APP_ENV`
  - `dev`：默认开发配置（`debug=true`，`log_level=DEBUG`）
  - `prod`：生产配置（`debug=false`，`log_level=INFO`）
- 配置入口：`app/core/config.py`
- 运行时可通过 `/health` 返回的 `env` 字段确认当前环境。
