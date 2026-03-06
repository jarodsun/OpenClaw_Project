# 开发环境与启动命令

> 更新时间：2026-03-07
> 状态：v1.0（可执行基线）

## 1. 文档目标与适用范围

- 目标：提供 IdleWoool 本地开发、联调、排障的统一环境与命令基线，降低“我这边能跑/你那边不能跑”的差异。
- 适用范围：`Next.js` 前端 + `FastAPI` 后端 + `SQLite3` 本地数据库。
- 非目标：生产环境部署命令与云资源编排（由 `44-release-plan-and-milestones.md` 覆盖）。

## 2. 环境基线

### 2.1 版本要求

- Node.js：`>=22 LTS`
- Python：`>=3.11`
- 包管理：前端使用 `pnpm`，后端使用 `uv`（或 `pip + venv` 兼容）
- 数据库：SQLite3（本地文件）
- 操作系统：macOS / Linux 优先，Windows 通过 WSL2

### 2.2 目录约定（建议）

```text
IdleWoool/
  apps/
    web/                 # Next.js 前端
    api/                 # FastAPI 后端
  packages/
    shared/              # 共享类型与常量
  scripts/               # 开发辅助脚本
  data/
    dev/idlewoool.db     # 本地 SQLite 数据库
```

### 2.3 环境变量约定

前端（`apps/web/.env.local`）：

```env
NEXT_PUBLIC_API_BASE_URL=http://127.0.0.1:8000
NEXT_PUBLIC_BUILD_CHANNEL=dev
```

后端（`apps/api/.env`）：

```env
APP_ENV=dev
APP_PORT=8000
DATABASE_URL=sqlite+aiosqlite:///../../data/dev/idlewoool.db
LOG_LEVEL=DEBUG
CORS_ALLOW_ORIGINS=http://127.0.0.1:3000,http://localhost:3000
```

约束：

- `.env*` 不提交到仓库，统一维护 `.env.example`。
- CI 安装依赖时统一使用锁文件模式（前端 `pnpm install --frozen-lockfile`）。
- 不在前端暴露任何服务端私有密钥。

## 3. 一次性初始化

### 3.1 前端初始化

```bash
cd apps/web
pnpm install
cp .env.example .env.local
```

### 3.2 后端初始化

```bash
cd apps/api
uv venv
source .venv/bin/activate
uv sync
cp .env.example .env
```

兼容方案（无 `uv`）：

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 3.3 数据库初始化

```bash
cd apps/api
source .venv/bin/activate
alembic upgrade head
python -m app.tools.seed_dev_data
```

要求：

- 任意开发分支首次启动前必须完成迁移；
- `seed` 脚本必须幂等，可重复执行而不破坏已有测试数据。

## 4. 日常开发命令

### 4.1 启动后端

```bash
cd apps/api
source .venv/bin/activate
uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

### 4.2 启动前端

```bash
cd apps/web
pnpm dev --host 127.0.0.1 --port 3000
```

### 4.3 代码质量与测试

后端：

```bash
cd apps/api
source .venv/bin/activate
ruff check .
ruff format .
pytest -q
```

前端：

```bash
cd apps/web
pnpm lint
pnpm test
pnpm typecheck
```

### 4.4 联调最小命令集

```bash
# 终端1：后端
cd apps/api && source .venv/bin/activate && uvicorn app.main:app --reload

# 终端2：前端
cd apps/web && pnpm dev

# 终端3：契约冒烟（示例）
curl http://127.0.0.1:8000/healthz
curl http://127.0.0.1:8000/api/v1/config/bootstrap
```

## 5. 常见故障与处理

- 端口冲突：改用 `--port` 指定空闲端口，并同步更新前端 `NEXT_PUBLIC_API_BASE_URL`。
- 迁移失败：执行 `alembic current` 与 `alembic history` 核对版本，再决定 `downgrade/upgrade`。
- 本地数据库损坏：删除 `data/dev/idlewoool.db` 后重跑迁移 + seed（仅限本地开发环境）。
- CORS 报错：检查后端 `CORS_ALLOW_ORIGINS` 是否包含前端实际访问地址。

## 6. DoD（文档完成标准）

- 新成员可按本文在 30 分钟内完成本地启动并打开可用页面。
- 前后端均有明确初始化、启动、测试、排障命令。
- 与 `31/32/33/34/35` 文档的环境与协议约束不冲突。
- 无需外部付费服务即可完成本地开发闭环。

## 7. 关联文档

- `docs/10_game_design/31-frontend-nextjs-architecture.md`
- `docs/10_game_design/32-backend-fastapi-architecture.md`
- `docs/10_game_design/33-database-sqlite3-schema.md`
- `docs/10_game_design/34-api-contract.md`
- `docs/10_game_design/41-testing-strategy.md`
