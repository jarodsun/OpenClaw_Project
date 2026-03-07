# v2 执行方案（任务包细化版）

## 0. 目标与边界

### 0.1 目标
在 v2 阶段产出完整的“游戏设计包”，可直接交给 v3（策划细化）与 v5（开发实现）使用。

### 0.2 不做事项
- 不进入前后端实现
- 不做数据库与 API 代码落地
- 不做上线部署

## 1. 执行规则（强约束）

1. 每轮只完成 **1 个任务包（Task Pack）**。
2. 每轮必须更新：
   - `docs/00_management/03-review-log.md`
   - `docs/00_management/04-decision-register.md`（如有决策）
3. 任务包完成标准：输入已读、输出已写、验收已通过、留痕已完成。
4. 无需人工拍板等待，可自决，但必须记录依据与回滚条件。

## 2. 任务包清单（按优先级）

### P1 调研层（Research）

#### TP-R1：Idle MMO 核心循环拆解
- 状态：`pending`
- 输入：`https://web.idle-mmo.com/`、`https://wiki.idle-mmo.com/`
- 输出：`docs/10_research/11-idle-mmo-core-loop-analysis.md`
- 验收：至少包含“循环步骤、关键资源、停留动机、风险点”4节

#### TP-R2：Idle MMO 系统矩阵拆解
- 状态：`pending`
- 输入：同上
- 输出：`docs/10_research/12-idle-mmo-system-analysis.md`
- 验收：至少覆盖“战斗/成长/交易/地图/社交”5个系统

#### TP-R3：传奇世界语料清单
- 状态：`pending`
- 输入：公开资料调研
- 输出：`docs/10_research/13-legend-of-mir-style-reference.md`
- 验收：至少包含“职业、技能、怪物、道具、地图区名”命名池

### P2 设计基线（Foundation）

#### TP-D1：设计原则定义
- 状态：`pending`
- 输出：`docs/20_design/21-design-principles.md`
- 验收：至少 8 条设计原则，含“反例/不做什么”

#### TP-D2：核心循环设计
- 状态：`pending`
- 输出：`docs/20_design/22-game-loop-v2.md`
- 验收：包含“在线循环、离线循环、回流触发、反疲劳机制”

#### TP-D3：成长框架设计
- 状态：`pending`
- 输出：`docs/20_design/23-progression-framework.md`
- 验收：包含“等级、战力、稀有度、经济闭环”

### P3 核心系统（Systems）

#### TP-S1：战斗系统
- 状态：`pending`
- 输出：`docs/20_design/31-combat-system.md`
- 验收：包含“结算公式、时序、异常与防滥用”

#### TP-S2：职业与技能
- 状态：`pending`
- 输出：`docs/20_design/32-profession-skill-system.md`
- 验收：包含“职业定位、技能树、升级与平衡入口”

#### TP-S3：道具与掉落
- 状态：`pending`
- 输出：`docs/20_design/33-item-loot-system.md`
- 验收：包含“掉落池、稀有度、保底、回收”

#### TP-S4：玩家交易与经济
- 状态：`pending`
- 输出：`docs/20_design/34-player-trade-economy.md`
- 验收：包含“交易机制、税率/手续费、反操纵规则”

#### TP-S5：世界地图与区域
- 状态：`pending`
- 输出：`docs/20_design/35-world-map-region-design.md`
- 验收：包含“区域分层、进入条件、风险收益梯度”

### P4 平衡与体验（Balance & Experience）

#### TP-B1：平衡模型
- 状态：`pending`
- 输出：`docs/20_design/41-balance-model.md`
- 验收：包含“关键指标、调参旋钮、回滚策略”

#### TP-B2：留存与参与钩子
- 状态：`pending`
- 输出：`docs/20_design/42-engagement-retention-hooks.md`
- 验收：包含“短中长期目标与奖励闭环”

### P5 封版与交接（Handover）

#### TP-H1：v2 设计包索引
- 状态：`pending`
- 输出：`docs/20_design/51-v2-design-package-index.md`
- 验收：所有文档有索引、状态、责任与版本

#### TP-H2：v2 -> v3 交接
- 状态：`pending`
- 输出：`docs/20_design/52-v2-to-v3-handover.md`
- 验收：可直接指导策划细化

#### TP-H3：v2 -> v5 交接
- 状态：`pending`
- 输出：`docs/20_design/53-v2-to-v5-technical-handover.md`
- 验收：可直接指导工程实现拆解

## 2.1 TaskPack 命名规范

- 统一格式：`TP-<类别字母><序号>`（如 `TP-R1`、`TP-S4`）
- 类别字母定义：
  - `R` = Research（调研）
  - `D` = Design Foundation（设计基线）
  - `S` = Systems（核心系统）
  - `B` = Balance & Experience（平衡与体验）
  - `H` = Handover（封版与交接）
- 使用要求：
  - `03-review-log.md` 每条记录必须带 TaskPack-ID
  - `04-decision-register.md` 若为某任务包决策，标题需包含对应 TaskPack-ID
  - commit message 建议包含 TaskPack-ID，便于追溯

## 3. 本轮选包策略

1. 优先选择最靠前的 `pending` 任务包。
2. 若任务包依赖未满足，写入 `03-review-log.md` 并跳到下一个可执行包。
3. 每轮完成后将任务包状态更新为：`done` / `in_progress` / `blocked`。
