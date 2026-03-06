# AI Global News 部署与回滚预案（最小可执行版）

更新时间：2026-03-06 23:58 (Asia/Shanghai)

## 1. 上线前检查（必须全部通过）

- 后端健康检查可用：`GET /health` 返回 200
- 前端首页、详情页、标签页可访问
- 数据库备份完成（SQLite 文件快照）
- 管理端可读取来源状态与任务状态
- 最近 24 小时无持续失败任务（允许偶发重试）

## 2. 标准部署步骤

1. 拉取主分支最新代码并确认工作区干净：
   - `git pull`
   - `git status --short`
2. 安装后端依赖（虚拟环境内）：
   - `python3 -m venv .venv`（如不存在）
   - `source .venv/bin/activate`
   - `pip3 install -r backend/requirements.txt`
3. 构建并启动前端：
   - `cd frontend && npm install && npm run build`
4. 启动后端服务并检查健康：
   - `cd backend && uvicorn app.main:app --host 0.0.0.0 --port 8000`
   - `curl -f http://127.0.0.1:8000/health`
5. 烟雾验证：
   - 列表 API：`/api/articles`
   - 搜索 API：`/api/articles?query=OpenAI`
   - 管理 API：`/api/admin/sources`

## 3. 回滚触发条件

满足任一条件立即回滚：

- 关键 API 连续 5 分钟不可用
- 抓取任务失败率持续 > 20% 且无恢复趋势
- 前端关键路径（首页/详情）出现阻断性错误
- 数据异常写入（重复激增、摘要大面积为空）

## 4. 回滚步骤（10 分钟内）

1. 记录当前版本号与故障时间窗口
2. 切换到上一稳定提交：
   - `git log --oneline -n 10`
   - `git checkout <last_stable_commit>`
3. 重启后端与前端服务
4. 恢复部署前数据库快照（如涉及数据污染）
5. 复测健康检查与 3 个关键 API
6. 在 `docs/05-scope-change-log.md` 记录故障与回滚结论

## 5. 监控与告警（最小要求）

- 每 5 分钟探测一次 `/health`
- 每小时统计抓取成功率与摘要成功率
- 连续两次探测失败触发告警
- 告警至少发送到一个即时通道（如 Discord/Telegram）

## 6. 值班处置原则

- 先恢复可用性，再做根因修复
- 回滚优先级高于在线热修（除非热修风险更低且可验证）
- 所有异常必须在变更日志留痕
