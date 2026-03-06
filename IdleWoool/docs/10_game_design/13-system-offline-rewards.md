# 系统设计：离线收益

> 状态：已完成 v1.0（默认口径，待最终拍板）

## 1. 目标与范围

### 1.1 目标
- 定义离线收益的统一结算口径，确保前后端与配置同口径实现。
- 在用户短时离线期间提供稳定成长反馈，不破坏在线游玩收益优势。
- 为后续 `20-balance-framework.md` 与 `34-api-contract.md` 提供可直接落地的输入。

### 1.2 范围
- In Scope：离线时长计量、收益计算、奖励发放、上限与容错策略。
- Out of Scope：离线挂机加速道具、广告双倍、跨服离线托管等运营能力。

## 2. 核心规则

### 2.1 触发与时长
- 触发条件：玩家从“在线战斗/在线空闲”进入离线状态并完成状态持久化。
- 计时起点：`last_online_at`（服务端时间戳）。
- 计时终点：玩家下次登录时的 `now`（服务端时间戳）。
- 有效离线时长：`offline_seconds = clamp(now - last_online_at, 0, offline_cap_seconds)`。

### 2.2 默认参数（未拍板前执行口径）
- 离线时长上限：`offline_cap_seconds = 28800`（8 小时）。
- 离线收益效率：`offline_efficiency = 0.70`。
- 最小结算粒度：60 秒（不足 60 秒不发放）。
- 默认来源：`09-open-questions.md` 的 `Q-001` 未决前，按 A 档继续推进。

### 2.3 结算公式
- 基准在线产出（每秒）：
  - `base_gold_per_sec`
  - `base_exp_per_sec`
  - `base_drop_points_per_sec`
- 离线折算后产出：
  - `offline_gold = floor(base_gold_per_sec * offline_seconds * offline_efficiency)`
  - `offline_exp = floor(base_exp_per_sec * offline_seconds * offline_efficiency)`
  - `offline_drop_points = floor(base_drop_points_per_sec * offline_seconds * offline_efficiency)`

### 2.4 掉落与保底
- 装备掉落不做“逐秒模拟战斗”，改用离线掉落点数池统一结算。
- 当 `offline_drop_points` 达到配置阈值时，按 `12-system-equipment-and-loot.md` 掉落规则生成奖励。
- 保底计数参与离线累计，但单次离线结算最多触发一次保底，避免爆发式超额奖励。

### 2.5 发放与幂等
- 离线奖励在“登录结算阶段”一次性发放。
- 每次结算生成 `offline_settlement_id`（基于 user_id + last_online_at + now）。
- 后端必须幂等：同一 `offline_settlement_id` 重放请求只返回已发放结果，不重复入账。

## 3. 异常与自动降级

### 3.1 数据缺失
- 若缺少 `last_online_at`，本次离线收益记为 0，并记录告警日志。
- 若角色快照缺失基准产出字段，回退到“角色等级默认产出表”。

### 3.2 配置异常
- 若离线参数配置缺失，回退默认值：8h、70%、60 秒粒度。
- 若掉落阈值配置异常，本次仅发放金币与经验，不发放装备并打点告警。

### 3.3 风险防护
- 若检测到设备时间回拨或异常跳变，以服务端时间为准并截断负数时长。
- 对超高收益账户增加审计日志：记录离线时长、结算前后资产、奖励明细。

## 4. 配置与字段约束

### 4.1 配置项
- `offline.cap_seconds`：离线上限秒数。
- `offline.efficiency`：离线收益效率（0~1）。
- `offline.min_granularity_seconds`：最小结算粒度。
- `offline.drop_point_thresholds`：离线掉落点阈值表。

### 4.2 接口字段（待在 API 文档固化）
- 请求：无需客户端上传离线开始时间（统一由服务端会话状态推导），`client_login_at` 仅用于排障展示。
- 响应：`offline_seconds`、`offline_gold`、`offline_exp`、`offline_drops`、`offline_settlement_id`。

## 5. 验收标准（DoD）
- 给定 30 分钟、2 小时、8 小时、12 小时离线样例，结算结果满足上限截断与效率折算规则。
- 重复提交同一结算请求不重复入账（幂等通过）。
- 配置缺失时系统可降级发放基础奖励，不阻断登录流程。
- 与 `12-system-equipment-and-loot.md` 掉落规则一致，无字段冲突。

## 6. 关联与后续
- 直接输入：`20-balance-framework.md`（离线/在线收益比目标）。
- 直接输入：`21-content-config-schema.md`（离线参数配置 schema）。
- 直接输入：`34-api-contract.md`（离线结算接口字段与幂等语义）。
