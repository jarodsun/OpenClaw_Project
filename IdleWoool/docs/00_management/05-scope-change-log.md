# 05 Scope Change Log（范围基线与变更记录）

## Baseline v1（文档优先）

- 冻结时间：2026-03-07
- 当前范围：
  - 文档体系搭建与完善（需求、系统、架构、测试、发布）
  - 参考数据归档（`data/reference/woool_data/`）
- 暂不纳入：
  - 前后端大规模功能开发
  - 在线服务部署与压测

## 变更记录

### 2026-03-07

- 变更：完成并落地 `docs/10_game_design/42-observability-and-logs.md` v1.0（日志分层、指标与告警阈值、链路耗时字段、Runbook、留存与脱敏策略）。
- 原因：D4.1 缺少可观测与日志基线，无法形成“测试门禁 -> 线上告警 -> 故障回溯”的执行闭环。
- 影响：`43-security-and-cheat-prevention.md` 与后续实现阶段可按统一观测口径落地埋点、告警与排障流程。
- 状态：生效

- 变更：完成并落地 `docs/10_game_design/41-testing-strategy.md` v1.0（分层测试策略、质量门禁、自动化执行、缺陷分级与响应）。
- 原因：D4.1 缺少测试入口与门禁标准，导致后续实现阶段无法统一“提测/发布”质量口径。
- 影响：`42-observability-and-logs.md`、`43-security-and-cheat-prevention.md` 与后续实现任务可按统一质量约束推进。
- 状态：生效

- 变更：完成并落地 `docs/10_game_design/40-dev-environment-and-commands.md` v1.0（环境基线、初始化流程、联调命令、故障排查、DoD）。
- 原因：D4.1 缺少统一开发环境与命令口径，阻塞后续测试策略与开发执行的一致性。
- 影响：`41-testing-strategy.md`、实际开发 onboarding 与日常联调可按统一命令基线推进。
- 状态：生效

- 变更：完成 `docs/10_game_design/03-feature-scope-mvp.md` v1.0，明确 In Scope / Out of Scope、验收边界、默认风险处理与后续衔接。
- 原因：将“产品目标”收敛为可执行 MVP 边界，避免实现阶段范围漂移。
- 影响：D2.1 产品与范围进一步收敛，可直接驱动 10~13 系统文档与 34 接口文档编写。
- 状态：生效

- 变更：新增 `03-execution-plan.md` 与 `05-scope-change-log.md`
- 原因：需要建立可追踪的执行进度与范围管理机制
- 影响：后续执行任务可按阶段推进并留痕
- 状态：生效

- 变更：曾记录“完成 PRD 并勾选完成”，现回退为未完成状态
- 原因：当前 PRD 质量与评审结果未达到“完成”标准，需要继续细化
- 影响：执行计划中 `01-product-requirements.md` 已调整为未完成，后续按评审闭环继续迭代
- 状态：生效

- 变更：`03-execution-plan.md` 按“阶段（D1~D5）”完成细化，并统一管理文档路径为 `docs/00_management/*`
- 原因：提高自动执行可操作性，避免旧路径与状态冲突
- 影响：执行者后续可按阶段推进并持续留痕
- 状态：生效

- 变更：完成并落地 `docs/10_game_design/02-game-design-core-loop.md` v1.0（状态机、在线/离线循环、结算口径、验收标准）
- 原因：将 PRD 目标转为可执行玩法文档，降低实现歧义
- 影响：D2.1 核心玩法文档推进，后续可对接系统、接口与测试文档
- 状态：生效

- 变更：修正 `01-product-requirements.md` 内部引用路径至 `docs/10_game_design/*`
- 原因：历史目录迁移后链接路径失配
- 影响：文档交叉引用可直接跳转，避免评审误判为缺失文档
- 状态：生效

- 变更：完成并落地 `docs/10_game_design/10-system-combat-and-progression.md` v1.0（战斗 Tick、伤害口径、成长曲线、战力公式、区域推进与验收标准）
- 原因：D2.2 系统与数值缺少可执行基线，无法稳定衔接 API 与测试文档
- 影响：后续可直接推进 `11/12/13` 系统文档与 `34-api-contract.md`、`41-testing-strategy.md`
- 状态：生效

- 变更：完成并落地 `docs/10_game_design/11-system-professions-and-skills.md` v1.0（职业定位、技能树结构、解锁与升级规则、技能结算口径、配置约束与验收标准）
- 原因：D2.2 缺少职业与技能的实现口径，无法稳定衔接装备、平衡与接口文档
- 影响：`12-system-equipment-and-loot.md`、`20-balance-framework.md`、`34-api-contract.md` 可按统一口径继续推进
- 状态：生效

- 变更：完成并落地 `docs/10_game_design/12-system-equipment-and-loot.md` v1.0（装备部位、稀有度权重、词条规则、掉落流程、保底机制、强化分解与配置约束）
- 原因：D2.2 缺少装备与掉落统一口径，导致后续平衡与接口字段无法稳定收口
- 影响：`20-balance-framework.md`、`21-content-config-schema.md`、`34-api-contract.md` 可按统一规则继续推进
- 状态：生效

- 变更：完成并落地 `docs/10_game_design/13-system-offline-rewards.md` v1.0（离线时长计量、收益公式、掉落折算、幂等发放、异常降级与 DoD）
- 原因：D2.2 中离线收益规则缺失，无法闭合“在线/离线循环”与后续平衡、接口设计
- 影响：`20-balance-framework.md`、`21-content-config-schema.md`、`34-api-contract.md` 可基于统一离线结算口径继续推进
- 状态：生效

- 变更：完成并落地 `docs/10_game_design/20-balance-framework.md` v1.0（指标体系、公式框架、资源闭环约束、调参与回滚策略、DoD）
- 原因：D2.2 缺少统一平衡框架，导致战斗/装备/离线/成长文档难以形成可联调的共同口径
- 影响：`21-content-config-schema.md`、`34-api-contract.md`、`41-testing-strategy.md` 可基于统一指标与公式继续推进
- 状态：生效

- 变更：完成并落地 `docs/10_game_design/21-content-config-schema.md` v1.0（配置分层、核心 Schema、校验流程、热更回滚、兼容策略）
- 原因：D2.2 缺少统一配置模型，导致系统文档难以收敛到可验证的数据契约
- 影响：`34-api-contract.md`、`33-database-sqlite3-schema.md`、`41-testing-strategy.md` 可按统一字段与版本策略推进
- 状态：生效

- 变更：完成并落地 `docs/10_game_design/30-architecture-overview.md` v1.0（架构目标、模块边界、关键数据流、非功能基线、部署与演进路径）
- 原因：D3.1 缺少总体架构蓝图，导致前后端/数据库/API 文档缺乏统一约束
- 影响：`31-frontend-nextjs-architecture.md`、`32-backend-fastapi-architecture.md`、`33-database-sqlite3-schema.md`、`34-api-contract.md`、`35-save-and-sync-strategy.md` 可按统一边界推进
- 状态：生效

- 变更：完成并落地 `docs/10_game_design/31-frontend-nextjs-architecture.md` v1.0（前端分层、路由渲染策略、状态管理、BFF 约束、性能与埋点基线）
- 原因：D3.1 缺少前端实现蓝图，导致页面分层、状态流转与接口编排口径不统一
- 影响：`34-api-contract.md`、`35-save-and-sync-strategy.md`、`41-testing-strategy.md` 可基于统一前端约束继续推进
- 状态：生效

- 变更：完成并落地 `docs/10_game_design/32-backend-fastapi-architecture.md` v1.0（分层架构、关键流程、幂等一致性、错误模型、观测与安全基线）
- 原因：D3.1 缺少后端实现蓝图，导致接口契约、数据库设计与结算一致性约束无法收敛
- 影响：`33-database-sqlite3-schema.md`、`34-api-contract.md`、`35-save-and-sync-strategy.md`、`41-testing-strategy.md` 可按统一后端约束继续推进
- 状态：生效

- 变更：完成并落地 `docs/10_game_design/33-database-sqlite3-schema.md` v1.0（核心表结构、索引策略、事务约束、幂等记录、迁移与容量基线）
- 原因：D3.1 缺少数据库实现基线，导致 API 契约与存档同步文档无法收敛到可实现字段模型
- 影响：`34-api-contract.md`、`35-save-and-sync-strategy.md`、`41-testing-strategy.md` 可按统一数据模型继续推进
- 状态：生效

- 变更：完成并落地 `docs/10_game_design/34-api-contract.md` v1.0（认证会话、核心业务接口、存档与配置接口、错误码、幂等并发约束、示例报文与 DoD）
- 原因：D3.2 缺少统一 API 字段与错误模型，前后端联调与测试用例无法按同一口径执行
- 影响：`35-save-and-sync-strategy.md`、`41-testing-strategy.md`、后续实现任务可按统一契约直接拆分开发与联调
- 状态：生效

- 变更：完成并落地 `docs/10_game_design/35-save-and-sync-strategy.md` v1.0（存档权威边界、在线/离线同步流程、版本冲突处理、幂等防重、异常降级与 DoD）
- 原因：D3.2 仍缺少存档同步闭环规则，无法将 API 与数据库约束收敛为可联调实现策略
- 影响：D3.2 接口与数据流阶段闭合，`41-testing-strategy.md` 可基于明确冲突/幂等口径设计用例
- 状态：生效
