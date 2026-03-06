# 03 Execution Plan（文档完善优先）

## 当前阶段目标

先完成“文档到位”，再进入代码实现。当前仅聚焦文档完善，不进行大规模功能开发。

## Phase D1：文档基线建立

- [x] 建立文档索引（`00-docs-index.md`）
- [x] 归档原始需求（`README.from_02_IdleWoool.md`）
- [x] 引入参考数值数据（`data/reference/woool_data/`）
- [x] 建立执行计划与范围变更日志（本文件 + `05-scope-change-log.md`）

## Phase D2：核心文档完善（当前）

- [x] 完成 `01-product-requirements.md`
- [ ] 完成 `02-game-design-core-loop.md`
- [ ] 完成 `03-feature-scope-mvp.md`
- [ ] 完成 `20-balance-framework.md`
- [ ] 完成 `21-content-config-schema.md`
- [ ] 完成 `34-api-contract.md`

## Phase D3：工程与交付文档完善

- [ ] 完成 `31-frontend-nextjs-architecture.md`
- [ ] 完成 `32-backend-fastapi-architecture.md`
- [ ] 完成 `33-database-sqlite3-schema.md`
- [ ] 完成 `40-dev-environment-and-commands.md`
- [ ] 完成 `41-testing-strategy.md`
- [ ] 完成 `44-release-plan-and-milestones.md`

## 执行规则

1. 每次执行至少完成 1 个可交付文档改进（新增章节、补齐关键内容、修订结构）。
2. 每次执行后同步更新：
   - `docs/03-execution-plan.md`（勾选进度）
   - `docs/05-scope-change-log.md`（记录变更与原因）
   - `memory/projects.md`（跨项目总览进度）
3. 若出现阻塞（信息缺失、冲突、优先级变化），必须记录“阻塞项 + 解除方案”。
