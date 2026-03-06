# API 契约与接口规范

- 更新时间：2026-03-07
- 适用阶段：D3.2 接口与数据流
- 关联文档：`30-architecture-overview.md`、`31-frontend-nextjs-architecture.md`、`32-backend-fastapi-architecture.md`、`33-database-sqlite3-schema.md`、`35-save-and-sync-strategy.md`

## 1. 目标与原则

### 1.1 目标
- 为 IdleWoool MVP 提供可联调、可测试、可回放的统一 API 契约。
- 明确请求/响应字段、错误模型、幂等策略与版本兼容边界。
- 保障“战斗结算 + 离线领取 + 存档同步”三条核心链路口径一致。

### 1.2 设计原则
- 服务端权威：收益、掉落、战斗关键值均由服务端计算。
- 读写分离：读取接口无副作用，结算接口必须显式幂等。
- 向前兼容：`v1` 小版本字段仅新增不删除，破坏性变更走 `v2`。

## 2. 通用规范

### 2.1 协议与路径
- 协议：HTTPS + JSON。
- 基础路径：`/api/v1`。
- 时间口径：统一使用 UTC ISO8601 字符串，响应额外返回本地展示建议时间戳。

### 2.2 通用请求头
- `Authorization: Bearer <session_token>`
- `Content-Type: application/json`
- `X-Request-Id: <uuid>`（写接口必填；读接口可选）

### 2.3 通用响应信封

```json
{
  "trace_id": "a2f7c6f0-3f17-4b5b-91a2-9d30b1e7e0a4",
  "server_time": "2026-03-07T06:20:00Z",
  "config_version": "2026.03.07.1",
  "data": {},
  "error": null
}
```

- 成功：`error=null` 且 `data` 非空对象或数组。
- 失败：`data=null` 且 `error` 包含错误详情。

### 2.4 错误对象

```json
{
  "code": "COMBAT_STATE_CONFLICT",
  "message": "battle is already settled",
  "details": {
    "battle_id": "bt_123"
  },
  "retryable": false
}
```

## 3. 认证与会话

### 3.1 `POST /api/v1/auth/guest-login`
- 用途：游客登录并创建/恢复玩家会话。
- 请求体：
  - `device_id: string`（必填，设备唯一标识）
  - `client_version: string`（必填）
- 响应 `data`：
  - `player_id: string`
  - `session_token: string`
  - `expires_at: string`

### 3.2 `POST /api/v1/auth/refresh`
- 用途：刷新会话令牌。
- 请求体：空。
- 响应 `data`：`session_token`、`expires_at`。

## 4. 核心业务接口

### 4.1 `GET /api/v1/player/state`
- 用途：拉取玩家当前聚合状态。
- 查询参数：无。
- 响应 `data`：
  - `player`：等级、经验、战力、货币
  - `progress`：章节、关卡、解锁内容
  - `team`：职业、技能、装备摘要
  - `offline`：`last_active_at`、`claimable_seconds`

### 4.2 `POST /api/v1/combat/settle`
- 用途：提交一次战斗结算请求（服务端重算）。
- 幂等键：`X-Request-Id`（必填）。
- 请求体：
  - `stage_id: string`（必填）
  - `team_snapshot_id: string`（必填，前端战前快照引用）
  - `client_battle_ms: number`（可选，仅监控）
- 响应 `data`：
  - `battle_id: string`
  - `result: "win" | "lose"`
  - `rewards`：经验、金币、掉落列表
  - `progress_delta`：关卡推进、解锁变化

### 4.3 `POST /api/v1/offline/claim`
- 用途：领取离线收益。
- 幂等键：`X-Request-Id`（必填，语义等同 `claim_id`）。
- 请求体：
  - `expected_config_version: string`（可选，用于前端提示配置漂移）
- 响应 `data`：
  - `offline_seconds: number`（服务端确认）
  - `effective_ratio: number`（默认 0.7，受 `Q-001` 约束）
  - `rewards`：金币、经验、材料、装备
  - `idempotent_replayed: boolean`

### 4.4 `POST /api/v1/equipment/enhance`
- 用途：装备强化。
- 幂等键：`X-Request-Id`（必填）。
- 请求体：`equipment_id`、`material_item_ids[]`。
- 响应 `data`：强化前后等级、消耗、战力变化。

### 4.5 `POST /api/v1/skills/upgrade`
- 用途：技能升级。
- 幂等键：`X-Request-Id`（必填）。
- 请求体：`skill_id`、`target_level`。
- 响应 `data`：技能等级变化、消耗、战力变化。

## 5. 存档与配置接口

### 5.1 `GET /api/v1/save/snapshot`
- 用途：获取用于诊断与回放的轻量快照。
- 响应 `data`：`snapshot_id`、`player_state_hash`、`updated_at`。

### 5.2 `POST /api/v1/save/sync`
- 用途：多端场景下触发手动同步（MVP 保留接口位，默认单端）。
- 幂等键：`X-Request-Id`（必填）。
- 请求体：`base_snapshot_id`、`client_ops[]`（可为空）。
- 响应 `data`：`resolved_snapshot_id`、`merge_strategy`、`conflicts[]`。

### 5.3 `GET /api/v1/config/version`
- 用途：拉取当前生效配置版本与兼容范围。
- 响应 `data`：
  - `config_version: string`
  - `min_client_version: string`
  - `compatible_schema_major: number`

## 6. 错误码清单（v1）

### 6.1 通用错误
- `AUTH_UNAUTHORIZED`：会话无效或过期（401）。
- `REQUEST_INVALID`：请求字段校验失败（400）。
- `REQUEST_DUPLICATED`：幂等键冲突且载荷不一致（409）。
- `CONFIG_VERSION_MISMATCH`：配置版本不兼容（409）。

### 6.2 业务错误
- `COMBAT_STATE_CONFLICT`：战斗状态已结算或不可结算（409）。
- `OFFLINE_NOT_READY`：无可领取离线收益（400）。
- `RESOURCE_NOT_ENOUGH`：资源不足（400）。
- `EQUIPMENT_NOT_FOUND`：装备不存在或不归属玩家（404）。
- `SKILL_UPGRADE_FORBIDDEN`：技能升级前置条件不满足（400）。

### 6.3 系统错误
- `INTERNAL_ERROR`：未分类内部错误（500）。
- `STORAGE_UNAVAILABLE`：数据库不可用（503）。
- `CONFIG_UNAVAILABLE`：配置服务不可用（503）。

## 7. 幂等与并发约束

- 所有写接口必须提供 `X-Request-Id` 且在 24h 内全局唯一（按玩家维度）。
- 重放请求行为：
  - 请求体哈希一致：返回首次成功结果，`idempotent_replayed=true`。
  - 请求体哈希不一致：返回 `REQUEST_DUPLICATED`。
- 状态并发冲突通过乐观锁版本号返回 `409`，前端需先 `GET /player/state` 再重试。

## 8. 示例（离线领取）

### 8.1 请求示例

```http
POST /api/v1/offline/claim
Authorization: Bearer xxx
X-Request-Id: 79a6de7c-f94d-4f1f-a6fe-8f55d2bd7ef1
Content-Type: application/json

{
  "expected_config_version": "2026.03.07.1"
}
```

### 8.2 成功响应示例

```json
{
  "trace_id": "f3eb9f5a-a5b6-4c7f-85a6-6f7f2d7404cf",
  "server_time": "2026-03-07T06:20:00Z",
  "config_version": "2026.03.07.1",
  "data": {
    "offline_seconds": 14400,
    "effective_ratio": 0.7,
    "rewards": {
      "gold": 1580,
      "exp": 640,
      "items": [{"item_id": "mat_iron", "count": 12}],
      "equipments": []
    },
    "idempotent_replayed": false
  },
  "error": null
}
```

## 9. 验收标准（DoD）

- 已覆盖 MVP 核心链路接口：认证、状态读取、战斗结算、离线领取、成长操作、存档与配置。
- 每个写接口已定义幂等要求、关键请求字段与响应结构。
- 错误码分层完整，可直接用于前后端联调与测试用例映射。
- 与 `32/33/35` 口径一致，无字段命名冲突与职责重叠。

## 10. 后续衔接

- 下一步：完善 `35-save-and-sync-strategy.md`，细化冲突合并算法与重试策略。
- 并行：在 `41-testing-strategy.md` 建立“幂等重放/配置漂移/并发冲突”用例组。
- 待决策对齐：`Q-001` 未拍板前，离线收益继续按 `8h + 70%` 默认口径执行。
