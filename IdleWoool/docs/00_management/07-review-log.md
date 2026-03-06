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

### 2026-03-07 05:40（Asia/Shanghai）
- 执行项：完成 `docs/10_game_design/30-architecture-overview.md` v1.0，补齐总体架构目标、模块边界、关键数据流、非功能基线、部署与演进路线。
- 评审发现：
  1) 原文档为占位稿，无法为 D3.1 提供统一架构约束；
  2) 初稿接入层写死为 `JWT`，对首版认证实现绑定过早，影响后续方案弹性。
- 自动修正：
  1) 将占位稿重构为可执行架构蓝图并补齐 DoD 与后续文档衔接；
  2) 将“`JWT Session`”修正为“`Session Token`”中性表述，避免过早技术拍板。
- 复评审结论：通过（与 D3.1 阶段一致，未引入范围漂移，可直接衔接 `31~35` 文档）。
- 需用户拍板：无新增（继续沿用 `09-open-questions.md` 的 `Q-001` 默认口径）。
- 证据文件：`docs/10_game_design/30-architecture-overview.md`、`docs/00_management/03-execution-plan.md`、`docs/00_management/05-scope-change-log.md`

### 2026-03-07 05:50（Asia/Shanghai）
- 执行项：完成 `docs/10_game_design/31-frontend-nextjs-architecture.md` v1.0，补齐前端分层、目录约束、渲染策略、状态管理、BFF 职责、性能与可观测基线。
- 评审发现：
  1) 原文档为占位稿，无法支撑 D3.1 到 D3.2 的接口与联调衔接；
  2) 初稿缺少“更新时间”元信息，不利于评审追踪与版本对齐。
- 自动修正：
  1) 将占位稿重构为可执行前端架构文档，并补齐 DoD 与后续文档衔接；
  2) 在文档头部新增“更新时间：2026-03-07”，统一管理文档可追溯性。
- 复评审结论：通过（与 D3.1 阶段一致，未引入范围漂移，可直接衔接 `34/35/41` 文档）。
- 需用户拍板：无新增（继续沿用 `09-open-questions.md` 的 `Q-001` 默认口径）。
- 证据文件：`docs/10_game_design/31-frontend-nextjs-architecture.md`、`docs/00_management/03-execution-plan.md`、`docs/00_management/05-scope-change-log.md`

### 2026-03-07 06:00（Asia/Shanghai）
- 执行项：完成 `docs/10_game_design/32-backend-fastapi-architecture.md` v1.0，补齐后端分层、模块职责、战斗/离线结算流程、幂等一致性、错误模型、观测与安全基线。
- 评审发现：
  1) 原文档仅为占位内容，无法支撑 D3.2 的 API 与数据流文档落地；
  2) 初稿在“失败降级”中未区分关键链路与非关键链路，存在执行歧义。
- 自动修正：
  1) 将占位稿重构为可执行架构文档，并明确与 `30/33/34/35` 的衔接；
  2) 补充降级策略分层（配置读取失败回退、埋点失败不阻塞、审计失败补偿标记），确保可落地。
- 复评审结论：通过（与 D3.1 阶段一致，未引入范围漂移，可直接衔接 `33/34/35/41` 文档）。
- 需用户拍板：无新增（继续沿用 `09-open-questions.md` 的 `Q-001` 默认口径）。
- 证据文件：`docs/10_game_design/32-backend-fastapi-architecture.md`、`docs/00_management/03-execution-plan.md`、`docs/00_management/05-scope-change-log.md`

### 2026-03-07 06:10（Asia/Shanghai）
- 执行项：完成 `docs/10_game_design/33-database-sqlite3-schema.md` v1.0，补齐 SQLite3 核心表结构、索引策略、事务一致性、幂等记录、迁移与容量基线。
- 评审发现：
  1) 原文档为占位稿，无法支撑 API 契约与存档同步设计；
  2) 初稿中 `4.1~4.10` 标题层级使用 `##`，破坏章节结构一致性。
- 自动修正：
  1) 将占位稿重构为可执行数据库设计文档，并对齐 `30/32` 架构约束；
  2) 将 `4.1~4.10` 子节统一修正为 `###` 层级，恢复文档结构规范。
- 复评审结论：通过（与 D3.1 阶段一致，未引入范围漂移，可直接衔接 `34/35/41` 文档）。
- 需用户拍板：无新增（继续沿用 `09-open-questions.md` 的 `Q-001` 默认口径）。
- 证据文件：`docs/10_game_design/33-database-sqlite3-schema.md`、`docs/00_management/03-execution-plan.md`、`docs/00_management/05-scope-change-log.md`

### 2026-03-07 06:20（Asia/Shanghai）
- 执行项：完成 `docs/10_game_design/34-api-contract.md` v1.0，补齐统一响应信封、认证会话、核心业务接口、存档与配置接口、错误码、幂等并发约束与离线领取示例。
- 评审发现：
  1) 原文档为占位稿，无法支撑前后端联调与测试映射；
  2) 初稿中离线领取幂等键命名同时出现 `claim_id` 与 `X-Request-Id`，存在实现歧义。
- 自动修正：
  1) 将占位稿重构为可执行 API 契约文档，并对齐 `32/33` 架构与数据约束；
  2) 明确 `X-Request-Id` 为写接口唯一幂等键，`claim_id` 仅保留语义说明，消除字段口径冲突。
- 复评审结论：通过（与 D3.2 阶段一致，未引入范围漂移，可直接衔接 `35/41` 文档与实现拆分）。
- 需用户拍板：无新增（继续沿用 `09-open-questions.md` 的 `Q-001` 默认口径）。
- 证据文件：`docs/10_game_design/34-api-contract.md`、`docs/00_management/03-execution-plan.md`、`docs/00_management/05-scope-change-log.md`

### 2026-03-07 06:30（Asia/Shanghai）
- 执行项：完成 `docs/10_game_design/35-save-and-sync-strategy.md` v1.0，补齐存档权威边界、保存触发策略、在线/离线同步流程、版本冲突处理、幂等防重、异常降级与 DoD。
- 评审发现：
  1) 原文档为占位稿，无法支撑 D3.2 阶段“接口->数据->同步”闭环；
  2) 初版保存策略中“页面隐藏即提交”未限制为“尝试提交”，在弱网环境下表达过强。
- 自动修正：
  1) 重构文档为可执行结构并对齐 `13/33/34` 口径；
  2) 将会话结束策略修正为“进入隐藏态时尝试提交一次”，并在异常章节补充超时后“查询再重试”规则。
- 复评审结论：通过（与 D3.2 阶段一致，未引入范围漂移，可直接衔接 `41-testing-strategy.md`）。
- 需用户拍板：无新增（继续沿用 `09-open-questions.md` 的 `Q-001` 默认口径）。
- 证据文件：`docs/10_game_design/35-save-and-sync-strategy.md`、`docs/00_management/03-execution-plan.md`、`docs/00_management/05-scope-change-log.md`

### 2026-03-07 06:40（Asia/Shanghai）
- 执行项：完成 `docs/10_game_design/40-dev-environment-and-commands.md` v1.0，补齐环境基线、初始化步骤、启动命令、联调命令、故障排查与 DoD。
- 评审发现：
  1) 初版环境变量约束未覆盖 CI 依赖安装一致性，存在“本地可装、CI 失败”风险；
  2) 占位文档无可执行命令，无法直接用于新人 onboarding。
- 自动修正：
  1) 在“2.3 环境变量约定”补充 CI 锁文件安装规则（`pnpm install --frozen-lockfile`）；
  2) 将占位稿重构为可执行命令手册，并补齐联调最小命令集与异常处理。
- 复评审结论：通过（与 D4.1 阶段一致，未引入范围漂移，可直接衔接 `41-testing-strategy.md`）。
- 需用户拍板：无新增（继续沿用 `09-open-questions.md` 的 `Q-001` 默认口径）。
- 证据文件：`docs/10_game_design/40-dev-environment-and-commands.md`、`docs/00_management/03-execution-plan.md`、`docs/00_management/05-scope-change-log.md`

### 2026-03-07 06:50（Asia/Shanghai）
- 执行项：完成 `docs/10_game_design/41-testing-strategy.md` v1.0，补齐测试分层、用例设计、质量门禁、自动化策略与缺陷分级。
- 评审发现：
  1) 原文档为占位稿，缺少可执行测试策略，无法支撑 D4.1 阶段落地；
  2) 初稿评审时发现未显式定义“提测门禁/发布门禁”分层标准，存在执行口径分叉风险。
- 自动修正：
  1) 重构为可执行测试策略文档，并补齐与 `10~13/20~21/32~35/40` 的映射关系；
  2) 增补“4.1 提测门禁 / 4.2 发布门禁”并固化阈值与缺陷清零要求。
- 复评审结论：通过（与 D4.1 阶段一致，未引入范围漂移，可直接衔接 `42-observability-and-logs.md`）。
- 需用户拍板：无新增（继续沿用 `09-open-questions.md` 的 `Q-001` 默认口径）。
- 证据文件：`docs/10_game_design/41-testing-strategy.md`、`docs/00_management/03-execution-plan.md`、`docs/00_management/05-scope-change-log.md`

### 2026-03-07 07:00（Asia/Shanghai）
- 执行项：完成 `docs/10_game_design/42-observability-and-logs.md` v1.0，补齐日志分层、结构化字段、脱敏留存、指标与告警阈值、Runbook 与 DoD。
- 评审发现：
  1) 原文档为占位稿，缺少可执行观测基线，无法支撑 D4.1 阶段落地；
  2) 初稿自评审发现“日志留存策略与告警阈值”未显式量化，执行时仍有口径歧义。
- 自动修正：
  1) 重构为可执行文档并对齐 `32/34/41` 约束，补齐统一上下文字段与链路耗时分段；
  2) 明确留存时长（7/14/30 天）与首版告警阈值（P1/P2/P3），消除运维与测试口径分叉。
- 复评审结论：通过（与 D4.1 阶段一致，未引入范围漂移，可直接衔接 `43-security-and-cheat-prevention.md`）。
- 需用户拍板：无新增（继续沿用 `09-open-questions.md` 的 `Q-001` 默认口径）。
- 证据文件：`docs/10_game_design/42-observability-and-logs.md`、`docs/00_management/03-execution-plan.md`、`docs/00_management/05-scope-change-log.md`

### 2026-03-07 07:10（Asia/Shanghai）
- 执行项：完成 `docs/10_game_design/43-security-and-cheat-prevention.md` v1.0，补齐威胁模型、安全基线、反作弊检测规则、分级处置与安全事件响应流程。
- 评审发现：
  1) 初版自评审发现仅定义检测规则，未显式约束误杀控制门槛；
  2) 接口限流若只保留 IP 维度，存在 NAT 场景误伤与账号刷接口漏检风险。
- 自动修正：
  1) 新增“4.3 误杀控制”，固化“双规则命中才冻结 + 规则灰度 + 误报率目标”；
  2) 将限流策略修正为“账号维度 + IP 维度”双层控制，并明确高价值接口串行化。
- 复评审结论：通过（与 D4.1 阶段一致，未引入范围漂移，可直接衔接 `44/45` 文档）。
- 需用户拍板：无新增（继续沿用 `09-open-questions.md` 的 `Q-001` 默认口径）。
- 证据文件：`docs/10_game_design/43-security-and-cheat-prevention.md`、`docs/00_management/03-execution-plan.md`、`docs/00_management/05-scope-change-log.md`

### 2026-03-07 07:20（Asia/Shanghai）
- 执行项：完成 `docs/10_game_design/44-release-plan-and-milestones.md` v1.0，补齐发布节奏、里程碑、Go/No-Go 门禁、灰度策略、回滚阈值与职责分工。
- 评审发现：
  1) 初稿自评审发现“质量门禁”标题层级误设为 `## 4.1`，结构一致性不足；
  2) 初稿未量化回滚触发阈值，发布执行仍存在口径歧义。
- 自动修正：
  1) 将 `4.1` 修正为 `###` 层级并统一章节结构；
  2) 新增可执行阈值（`5xx`、误报率、接口 P95、经济异常）与回滚顺序，固化应急流程。
- 复评审结论：通过（与 D4.2 阶段一致，未引入范围漂移，可直接衔接 `45-risk-register.md`）。
- 需用户拍板：无新增（继续沿用 `09-open-questions.md` 的 `Q-001` 默认口径）。
- 证据文件：`docs/10_game_design/44-release-plan-and-milestones.md`、`docs/00_management/03-execution-plan.md`、`docs/00_management/05-scope-change-log.md`

### 2026-03-07 07:30（Asia/Shanghai）
- 执行项：完成 `docs/10_game_design/45-risk-register.md` v1.0，补齐风险分级与时效、Top10 风险台账、门禁映射、响应与归档流程。
- 评审发现：
  1) 首版虽有分级定义，但缺少统一量化评分模型，跨角色评审时存在等级判定偏差风险；
  2) D4.2 进度尚未在执行计划勾选，管理面留痕不完整。
- 自动修正：
  1) 在 `45-risk-register.md` 新增“2.4 量化评分模型（Impact × Probability）”与冲突从高处理原则；
  2) 同步勾选 `03-execution-plan.md` 的 `45-risk-register.md` 完成状态，并在 `05-scope-change-log.md` 追加变更记录。
- 复评审结论：通过（与 D4.2 阶段一致，文档可直接用于 Go/No-Go 风险评审，未引入范围漂移）。
- 需用户拍板：无新增（继续沿用 `09-open-questions.md` 现有 `Q-001`）。
- 证据文件：`docs/10_game_design/45-risk-register.md`、`docs/00_management/03-execution-plan.md`、`docs/00_management/05-scope-change-log.md`
