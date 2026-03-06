# 03 Execution Plan（阶段化细化版）

## 当前总目标

先完成“文档可执行化”，再进入代码实现与联调。当前阶段仅聚焦文档完善与评审闭环。

## Phase D1：基线建立（已完成）

- [x] 建立文档索引（`docs/00-docs-index.md`）
- [x] 归档原始需求（`docs/README.from_02_IdleWoool.md`）
- [x] 引入参考数值数据（`data/reference/woool_data/`）
- [x] 建立管理与跟踪文档（`00_management/03,05,06,07,08,09`）

## Phase D2：核心产品与玩法文档（进行中）

### D2.1 产品与范围
- [ ] 完成 `docs/10_game_design/01-product-requirements.md`
- [x] 完成 `docs/10_game_design/03-feature-scope-mvp.md`
- [x] 完成 `docs/10_game_design/02-game-design-core-loop.md`

### D2.2 系统与数值
- [x] 完成 `docs/10_game_design/10-system-combat-and-progression.md`
- [x] 完成 `docs/10_game_design/11-system-professions-and-skills.md`
- [x] 完成 `docs/10_game_design/12-system-equipment-and-loot.md`
- [x] 完成 `docs/10_game_design/13-system-offline-rewards.md`
- [x] 完成 `docs/10_game_design/20-balance-framework.md`
- [x] 完成 `docs/10_game_design/21-content-config-schema.md`

### D2.3 评审闭环沉淀
- [ ] 每轮执行更新 `docs/00_management/07-review-log.md`
- [ ] 将需拍板事项写入 `docs/00_management/09-open-questions.md`
- [ ] 将已决策事项归档到 `docs/00_management/08-decision-register.md`

## Phase D3：技术架构与接口文档

### D3.1 架构蓝图
- [x] 完成 `docs/10_game_design/30-architecture-overview.md`
- [x] 完成 `docs/10_game_design/31-frontend-nextjs-architecture.md`
- [x] 完成 `docs/10_game_design/32-backend-fastapi-architecture.md`
- [x] 完成 `docs/10_game_design/33-database-sqlite3-schema.md`

### D3.2 接口与数据流
- [x] 完成 `docs/10_game_design/34-api-contract.md`
- [x] 完成 `docs/10_game_design/35-save-and-sync-strategy.md`

## Phase D4：工程交付与上线准备文档

### D4.1 开发与质量
- [x] 完成 `docs/10_game_design/40-dev-environment-and-commands.md`
- [x] 完成 `docs/10_game_design/41-testing-strategy.md`
- [x] 完成 `docs/10_game_design/42-observability-and-logs.md`
- [x] 完成 `docs/10_game_design/43-security-and-cheat-prevention.md`

### D4.2 发布与风险
- [x] 完成 `docs/10_game_design/44-release-plan-and-milestones.md`
- [x] 完成 `docs/10_game_design/45-risk-register.md`

## Phase D5：体验与运营文档

- [x] 完成 `docs/10_game_design/50-ui-ux-guidelines.md`
- [ ] 完成 `docs/10_game_design/51-audio-visual-style-guide.md`
- [ ] 完成 `docs/10_game_design/52-liveops-and-monetization.md`

## 每轮执行规则（自动执行版）

1. 每轮至少完成 1 个文档的有效改进（新增章节、补齐关键内容、修订结构）。
2. 每轮必须执行评审闭环：执行 -> 自评审 -> 自动修正 -> 复评审 -> 记录。
3. 每轮后必须同步更新：
   - `docs/00_management/03-execution-plan.md`（进度勾选）
   - `docs/00_management/05-scope-change-log.md`（变更与原因）
   - `docs/00_management/07-review-log.md`（评审闭环记录）
   - `memory/projects.md`（项目总览）
4. 需人工拍板的问题写入 `docs/00_management/09-open-questions.md`，不阻塞其他可推进任务。
5. 若有改动，执行 `git add -A && git commit && git push`。
