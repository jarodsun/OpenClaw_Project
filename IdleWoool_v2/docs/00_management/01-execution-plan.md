# v2 执行方案（可执行版）

## 0. 目标与边界

### 0.1 目标
在 v2 阶段产出完整的“游戏设计包”，可直接交给 v3（策划细化）与 v5（开发实现）使用。

### 0.2 不做事项
- 不进入前后端实现
- 不做数据库与 API 代码落地
- 不做上线部署

## 1. 工作流（持续推进）

每轮执行固定流程：
1) 选择一个设计子主题
2) 产出文档增量
3) 执行评审清单
4) 记录评审结果
5) 做出必要决策并登记
6) 提交留痕（文档变更 + 记录）

## 2. 阶段任务拆解（v2）

### P1：竞品与题材调研
- 交付物：
  - `docs/10_research/11-idle-mmo-core-loop-analysis.md`
  - `docs/10_research/12-idle-mmo-system-analysis.md`
  - `docs/10_research/13-legend-of-mir-style-reference.md`
- 验收：形成可复用的“机制清单 + 命名语料库 + 风险点”。

### P2：设计基线
- 交付物：
  - `docs/20_design/21-design-principles.md`
  - `docs/20_design/22-game-loop-v2.md`
  - `docs/20_design/23-progression-framework.md`
- 验收：明确“玩什么、为什么持续玩、如何长期增长”。

### P3：系统设计（核心）
- 交付物：
  - `docs/20_design/31-combat-system.md`
  - `docs/20_design/32-profession-skill-system.md`
  - `docs/20_design/33-item-loot-system.md`
  - `docs/20_design/34-player-trade-economy.md`
  - `docs/20_design/35-world-map-region-design.md`
- 验收：每个系统都有输入/规则/输出/边界/异常处理。

### P4：平衡与体验
- 交付物：
  - `docs/20_design/41-balance-model.md`
  - `docs/20_design/42-engagement-retention-hooks.md`
- 验收：形成可调参框架与体验指标。

### P5：v2 封版
- 交付物：
  - `docs/20_design/51-v2-design-package-index.md`
  - `docs/20_design/52-v2-to-v3-handover.md`
  - `docs/20_design/53-v2-to-v5-technical-handover.md`
- 验收：v3/v5 可无歧义接力。

## 3. 评审机制（调整后）

仅保留 3 份治理文档：
- `docs/00_management/02-review-checklist.md`
- `docs/00_management/03-review-log.md`
- `docs/00_management/04-decision-register.md`

规则：
- 无需人工拍板等待
- 执行者可自主决策，但必须记录“决策依据 + 影响范围 + 回滚条件”

## 4. 留痕要求（强制）

每轮至少更新：
- 至少 1 份设计文档
- `03-review-log.md`（记录本轮评审）
- `04-decision-register.md`（如有决策）

建议提交信息格式：
- `IdleWoool_v2: <本轮主题> + review log`
