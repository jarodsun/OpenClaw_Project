# 33 数据库设计（SQLite3 Schema）

更新时间：2026-03-07

## 1. 目标与范围

- 为 IdleWoool 单机/轻在线场景提供可落地的 SQLite3 数据模型。
- 对齐 `30-architecture-overview.md` 与 `32-backend-fastapi-architecture.md` 的分层和一致性约束。
- 覆盖账号、角色进度、战斗快照、离线结算、背包装备、配置版本、审计日志等核心域。
- 不包含跨服分库分表与复杂 BI 数仓建模（后续阶段再扩展）。

## 2. 设计原则

### 2.1 一致性优先
- 所有影响资源与进度的写操作必须在事务内完成。
- 结算类接口必须落 `idempotency_key`，确保重试不重放。

### 2.2 可追溯优先
- 核心状态表保留 `created_at` / `updated_at`。
- 关键结算链路记录审计日志（请求摘要、结果码、耗时、追踪 ID）。

### 2.3 演进兼容
- 采用 Alembic 迁移管理，禁止手工改线上库结构。
- 配置版本通过 `content_version` 关联到玩家快照，支持回放与回滚定位。

## 3. 实体关系概览

- `player_account`（账号）1 - N `player_profile`（角色）
- `player_profile` 1 - 1 `player_progress`（主进度）
- `player_profile` 1 - 1 `player_resources`（货币与体力）
- `player_profile` 1 - N `inventory_item`（背包物品）
- `player_profile` 1 - N `equipment_instance`（装备实例）
- `player_profile` 1 - N `battle_record`（战斗记录）
- `player_profile` 1 - N `offline_reward_record`（离线结算记录）
- `player_profile` 1 - N `idempotency_record`（幂等记录）
- `player_profile` 1 - N `audit_log`（审计日志）

## 4. 核心表结构

### 4.1 player_account

- `id` TEXT PK（UUID）
- `device_id` TEXT NOT NULL UNIQUE
- `channel` TEXT NOT NULL DEFAULT 'official'
- `register_at` INTEGER NOT NULL
- `last_login_at` INTEGER NOT NULL

约束：
- `device_id` 唯一，首版按“单设备单账号”处理。

### 4.2 player_profile

- `id` TEXT PK（UUID）
- `account_id` TEXT NOT NULL FK -> `player_account.id`
- `nickname` TEXT NOT NULL
- `profession` TEXT NOT NULL
- `level` INTEGER NOT NULL DEFAULT 1
- `vip_level` INTEGER NOT NULL DEFAULT 0
- `content_version` TEXT NOT NULL
- `created_at` INTEGER NOT NULL
- `updated_at` INTEGER NOT NULL

索引：
- `idx_profile_account_id(account_id)`

### 4.3 player_progress

- `profile_id` TEXT PK FK -> `player_profile.id`
- `current_stage` INTEGER NOT NULL DEFAULT 1
- `max_stage` INTEGER NOT NULL DEFAULT 1
- `power_score` INTEGER NOT NULL DEFAULT 0
- `last_battle_at` INTEGER
- `last_offline_calc_at` INTEGER
- `updated_at` INTEGER NOT NULL

### 4.4 player_resources

- `profile_id` TEXT PK FK -> `player_profile.id`
- `gold` INTEGER NOT NULL DEFAULT 0
- `gem` INTEGER NOT NULL DEFAULT 0
- `energy` INTEGER NOT NULL DEFAULT 0
- `updated_at` INTEGER NOT NULL

约束：
- 资源字段均要求 `>= 0`（数据库 CHECK + 服务端双重校验）。

### 4.5 inventory_item

- `id` TEXT PK（UUID）
- `profile_id` TEXT NOT NULL FK -> `player_profile.id`
- `item_type` TEXT NOT NULL
- `item_id` TEXT NOT NULL
- `quantity` INTEGER NOT NULL
- `expire_at` INTEGER
- `created_at` INTEGER NOT NULL
- `updated_at` INTEGER NOT NULL

索引：
- `idx_inventory_profile_type(profile_id, item_type)`
- `idx_inventory_profile_item(profile_id, item_id)`

### 4.6 equipment_instance

- `id` TEXT PK（UUID）
- `profile_id` TEXT NOT NULL FK -> `player_profile.id`
- `template_id` TEXT NOT NULL
- `slot` TEXT NOT NULL
- `rarity` TEXT NOT NULL
- `level` INTEGER NOT NULL DEFAULT 1
- `main_stat_json` TEXT NOT NULL
- `sub_stat_json` TEXT NOT NULL
- `equipped` INTEGER NOT NULL DEFAULT 0
- `lock_flag` INTEGER NOT NULL DEFAULT 0
- `created_at` INTEGER NOT NULL
- `updated_at` INTEGER NOT NULL

索引：
- `idx_equipment_profile_slot(profile_id, slot)`
- `idx_equipment_profile_equipped(profile_id, equipped)`

### 4.7 battle_record

- `id` TEXT PK（UUID）
- `profile_id` TEXT NOT NULL FK -> `player_profile.id`
- `stage_id` INTEGER NOT NULL
- `result` TEXT NOT NULL
- `duration_ms` INTEGER NOT NULL
- `damage_done` INTEGER NOT NULL
- `damage_taken` INTEGER NOT NULL
- `reward_json` TEXT NOT NULL
- `trace_id` TEXT NOT NULL
- `created_at` INTEGER NOT NULL

索引：
- `idx_battle_profile_created(profile_id, created_at DESC)`
- `idx_battle_trace_id(trace_id)`

### 4.8 offline_reward_record

- `id` TEXT PK（UUID）
- `profile_id` TEXT NOT NULL FK -> `player_profile.id`
- `offline_seconds` INTEGER NOT NULL
- `efficiency_rate` REAL NOT NULL
- `reward_json` TEXT NOT NULL
- `calc_start_at` INTEGER NOT NULL
- `calc_end_at` INTEGER NOT NULL
- `idempotency_key` TEXT NOT NULL UNIQUE
- `created_at` INTEGER NOT NULL

索引：
- `idx_offline_profile_created(profile_id, created_at DESC)`

### 4.9 idempotency_record

- `id` TEXT PK（UUID）
- `profile_id` TEXT NOT NULL FK -> `player_profile.id`
- `api_name` TEXT NOT NULL
- `idempotency_key` TEXT NOT NULL
- `request_hash` TEXT NOT NULL
- `response_json` TEXT NOT NULL
- `status` TEXT NOT NULL
- `expired_at` INTEGER NOT NULL
- `created_at` INTEGER NOT NULL

唯一索引：
- `uk_idempotency_api_key(api_name, idempotency_key)`

### 4.10 audit_log

- `id` TEXT PK（UUID）
- `profile_id` TEXT
- `action` TEXT NOT NULL
- `result_code` TEXT NOT NULL
- `latency_ms` INTEGER NOT NULL
- `trace_id` TEXT NOT NULL
- `detail_json` TEXT
- `created_at` INTEGER NOT NULL

索引：
- `idx_audit_profile_created(profile_id, created_at DESC)`
- `idx_audit_trace_id(trace_id)`

## 5. 事务与一致性约束

- 战斗结算事务：写入 `battle_record` + 更新 `player_progress` + 更新 `player_resources`，三者同事务提交。
- 离线领取事务：校验 `idempotency_key` -> 写 `offline_reward_record` -> 更新资源与背包 -> 回写 `player_progress.last_offline_calc_at`。
- 任一子步骤失败必须回滚，错误码按 `32-backend-fastapi-architecture.md` 统一模型返回。

## 6. 迁移与版本策略

- 迁移命名：`YYYYMMDDHHMM_<topic>.py`。
- 每次迁移必须包含：前向迁移、回滚迁移、数据兼容说明。
- 大版本配置切换时，先升级 schema 再切内容版本；若失败按迁移版本回滚，不直接手改。

## 7. 性能与容量基线

- 单玩家常用查询（背包、装备、进度）目标 P95 <= 30ms。
- 结算事务目标 P95 <= 80ms。
- 审计日志默认保留 30 天，超期按批处理清理。

## 8. DoD（完成定义）

- 关键业务表与索引已定义，字段口径与系统文档一致。
- 幂等、事务、审计三类约束可映射到实现代码与测试用例。
- 可直接衔接 `34-api-contract.md` 与 `35-save-and-sync-strategy.md`。

## 9. 后续衔接

- API 字段与错误码：`docs/10_game_design/34-api-contract.md`
- 存档与同步策略：`docs/10_game_design/35-save-and-sync-strategy.md`
- 测试覆盖：`docs/10_game_design/41-testing-strategy.md`
