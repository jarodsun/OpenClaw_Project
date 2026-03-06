# 07 Review Log（评审记录）

> 规则：每轮执行至少一条记录，记录“执行-评审-修正-复评审”闭环。

## 模板

### YYYY-MM-DD HH:mm（Asia/Shanghai）
- 执行项：
- 评审发现：
- 自动修正：
- 复评审结论：通过 / 需继续修正
- 需用户拍板：无 / 见 `09-open-questions.md`
- 证据文件：

### 2026-03-07 04:20（Asia/Shanghai）
- 执行项：完成 `docs/10_game_design/02-game-design-core-loop.md` v1.0，补齐目标、循环流程、状态机、规则口径、异常处理、验收标准与后续衔接。
- 评审发现：
  1) 原文档为占位内容，无法支撑研发落地；
  2) PRD 中存在历史路径 `docs/02-*`、`docs/03-*`，与当前分层目录不一致。
- 自动修正：
  1) 重写核心循环文档为可执行版本并补充默认参数口径（tick、离线上限、离线效率）；
  2) 修正 `01-product-requirements.md` 的交叉引用到 `docs/10_game_design/*`。
- 复评审结论：通过（与执行计划阶段 D2.1 一致，未引入范围漂移，且无需外部依赖即可继续推进）。
- 需用户拍板：见 `09-open-questions.md`（离线收益上限与效率系数最终值待确认）。
- 证据文件：`docs/10_game_design/02-game-design-core-loop.md`、`docs/10_game_design/01-product-requirements.md`、`docs/00_management/03-execution-plan.md`、`docs/00_management/05-scope-change-log.md`

### 2026-03-07 04:30（Asia/Shanghai）
- 执行项：完成 `docs/10_game_design/03-feature-scope-mvp.md` v1.0，补齐目标、MVP 范围边界、验收标准、风险默认处理与文档衔接。
- 评审发现：
  1) 旧文件为占位稿，缺少 In/Out Scope，易导致范围漂移；
  2) 对离线收益口径、技术栈约束、性能口径缺少显式声明，后续实现易出现理解分叉。
- 自动修正：
  1) 新增 In Scope/Out of Scope 清单并给出可执行条目；
  2) 补充“默认处理”并与 Q-001 对齐（未拍板前按 8h/70%推进）；
  3) 增加性能目标与文档衔接章节，降低实现与评审歧义。
- 复评审结论：通过（与 D2.1 阶段一致，未引入范围外功能，且可直接衔接系统与接口文档）。
- 需用户拍板：无新增（沿用 `09-open-questions.md` 现有 Q-001）。
- 证据文件：`docs/10_game_design/03-feature-scope-mvp.md`、`docs/00_management/03-execution-plan.md`、`docs/00_management/05-scope-change-log.md`

### 2026-03-07 04:40（Asia/Shanghai）
- 执行项：完成 `docs/10_game_design/10-system-combat-and-progression.md` v1.0，补齐战斗计算顺序、伤害公式、成长曲线、战力公式、推进规则与验收标准。
- 评审发现：
  1) 占位文档缺少可实现口径，无法直接用于后端结算设计；
  2) 初版小节层级存在 `##` 误用，影响结构一致性与可读性。
- 自动修正：
  1) 将占位稿升级为可执行系统文档，补齐配置入口与实现约束；
  2) 将 `3.1~4.3` 小节统一修正为 `###` 层级，保持章节规范。
- 复评审结论：通过（与 D2.2 阶段一致，未引入范围外内容，可直接衔接接口与测试文档）。
- 需用户拍板：无新增（继续沿用 `Q-001` 默认口径）。
- 证据文件：`docs/10_game_design/10-system-combat-and-progression.md`、`docs/00_management/03-execution-plan.md`、`docs/00_management/05-scope-change-log.md`

### 2026-03-07 04:50（Asia/Shanghai）
- 执行项：完成 `docs/10_game_design/11-system-professions-and-skills.md` v1.0，补齐职业定位、技能树结构、解锁/升级规则、技能结算口径、配置约束与验收标准。
- 评审发现：
  1) 原文档为占位内容，缺少可执行规则，无法直接用于接口与测试设计；
  2) 初稿中技能结算策略描述偏抽象，存在前后端理解分歧风险。
- 自动修正：
  1) 将文档重构为目标-规则-结算-配置-验收的可执行结构；
  2) 明确“伤害被动快照、防御被动实时”的默认口径，并指定在 `34-api-contract.md` 固化字段。
- 复评审结论：通过（与 D2.2 阶段一致，未引入范围漂移，可直接衔接 `12/20/34` 文档）。
- 需用户拍板：无新增（继续沿用 `Q-001` 默认口径）。
- 证据文件：`docs/10_game_design/11-system-professions-and-skills.md`、`docs/00_management/03-execution-plan.md`、`docs/00_management/05-scope-change-log.md`

### 2026-03-07 05:00（Asia/Shanghai）
- 执行项：完成 `docs/10_game_design/12-system-equipment-and-loot.md` v1.0，补齐装备部位、稀有度权重、词条生成、掉落流程、保底机制、强化分解与配置约束。
- 评审发现：
  1) 占位稿无法支撑后端掉落结算与配置建模；
  2) 初版未声明异常场景降级策略，存在“配置缺失导致结算中断”风险。
- 自动修正：
  1) 将占位稿重构为可执行规则文档并补齐 DoD 与衔接章节；
  2) 新增“5.3 自动降级默认值”，明确掉落池失效与副词条生成失败时的容错策略。
- 复评审结论：通过（与 D2.2 阶段一致，未引入范围外功能，可直接衔接 `20/21/34` 文档）。
- 需用户拍板：无新增（继续沿用 `Q-001` 默认口径）。
- 证据文件：`docs/10_game_design/12-system-equipment-and-loot.md`、`docs/00_management/03-execution-plan.md`、`docs/00_management/05-scope-change-log.md`

### 2026-03-07 05:10（Asia/Shanghai）
- 执行项：完成 `docs/10_game_design/13-system-offline-rewards.md` v1.0，补齐离线时长计量、收益公式、掉落折算、幂等发放、异常降级与验收标准。
- 评审发现：
  1) 占位稿缺少离线收益统一口径，无法直接支撑后端结算与联调；
  2) 初版接口字段描述包含 `last_online_at` 客户端入参，存在被篡改风险与职责边界不清问题。
- 自动修正：
  1) 将文档重构为可执行规则结构（目标/规则/异常/配置/DoD/衔接）；
  2) 修正接口约束为“离线开始时间仅由服务端推导”，客户端时间仅用于排障展示。
- 复评审结论：通过（与 D2.2 阶段一致，未引入范围漂移，且可直接衔接 `20/21/34` 文档）。
- 需用户拍板：无新增（继续沿用 `09-open-questions.md` 的 `Q-001` 默认口径）。
- 证据文件：`docs/10_game_design/13-system-offline-rewards.md`、`docs/00_management/03-execution-plan.md`、`docs/00_management/05-scope-change-log.md`

### 2026-03-07 05:20（Asia/Shanghai）
- 执行项：完成 `docs/10_game_design/20-balance-framework.md` v1.0，补齐平衡目标、指标体系、公式框架、资源闭环约束、调参流程与回滚策略。
- 评审发现：
  1) 原文档为占位内容，无法支撑后续配置建模与联调验收；
  2) 初稿中“关卡强度曲线”描述未明确分段策略与校验锚点，执行层面可操作性不足。
- 自动修正：
  1) 将占位稿重构为可执行文档，明确体验指标、数值健康指标、技术指标与 DoD；
  2) 新增分段强度曲线与“每 10 关校验锚点”规则，并补充调参回滚阈值。
- 复评审结论：通过（与 D2.2 阶段一致，未引入范围漂移，可直接衔接 `21/34/41` 文档）。
- 需用户拍板：无新增（继续沿用 `09-open-questions.md` 的 `Q-001` 默认口径）。
- 证据文件：`docs/10_game_design/20-balance-framework.md`、`docs/00_management/03-execution-plan.md`、`docs/00_management/05-scope-change-log.md`

### 2026-03-07 05:30（Asia/Shanghai）
- 执行项：完成 `docs/10_game_design/21-content-config-schema.md` v1.0，补齐配置分层、统一字段规范、核心 Schema 样例、静态/运行时校验、热更回滚与 DoD。
- 评审发现：
  1) 初版章节层级存在 `## 2.1/2.2` 误用，结构一致性不足；
  2) 初版未显式约束“版本兼容边界”，可能导致后续配置升级策略歧义。
- 自动修正：
  1) 将 `2.1/2.2` 调整为 `###` 层级，统一文档结构；
  2) 新增“5.3 版本兼容策略”，明确小版本兼容与大版本迁移要求。
- 复评审结论：通过（与 D2.2 阶段一致，未引入范围漂移，可直接衔接 `33/34/41` 文档）。
- 需用户拍板：无新增（继续沿用 `09-open-questions.md` 的 `Q-001`）。
- 证据文件：`docs/10_game_design/21-content-config-schema.md`、`docs/00_management/03-execution-plan.md`、`docs/00_management/05-scope-change-log.md`
