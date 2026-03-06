# 内容配置与数据 Schema

> 状态：v1.0（可执行基线）

## 1. 目标与范围

### 1.1 目标
- 为 `10/11/12/13/20` 文档中的规则提供统一、可校验、可热更新的配置 Schema。
- 明确“配置文件结构 -> 校验规则 -> 运行时加载 -> 灰度回滚”全链路约束。
- 为后续 `34-api-contract.md`、`33-database-sqlite3-schema.md`、`41-testing-strategy.md` 提供字段口径。

### 1.2 范围
- In Scope：战斗成长、职业技能、装备掉落、离线收益、平衡参数的配置模型。
- Out of Scope：运营活动后台 UI、动态脚本执行引擎、多服差异化自动分发系统。

## 2. 配置分层与目录约定

### 2.1 分层
- `base`：通用基础参数（版本、全局倍率、默认上限）。
- `system`：系统规则参数（战斗、职业、装备、离线）。
- `content`：可扩展内容数据（关卡、怪物池、掉落池、技能树节点）。
- `tuning`：平衡调参覆盖层（用于 A/B 或紧急修正）。

### 2.2 目录建议
```text
configs/
  base/
    global.json
  system/
    combat.json
    professions.json
    equipment.json
    offline_rewards.json
  content/
    stages.json
    monsters.json
    loot_pools.json
    skills.json
  tuning/
    live_patch.json
```

## 3. 统一字段规范

### 3.1 通用元数据
- `config_version`：语义化版本（如 `1.2.0`）。
- `revision`：递增整型修订号（用于缓存失效与幂等更新）。
- `updated_at`：UTC 时间戳（ISO 8601）。
- `checksum`：配置内容哈希（SHA-256）。

### 3.2 命名与 ID 规则
- 所有主键 ID 使用 `snake_case` 字符串（如 `warrior`, `skill_power_strike`）。
- 业务枚举统一小写字符串；禁止前后端各自定义 magic number。
- 引用字段命名统一为 `<target>_id` 或 `<target>_ids`。

### 3.3 数值类型约束
- 概率字段统一使用 `[0,1]` 浮点（如 `drop_rate`），禁止 `%` 字符串。
- 比例增益字段统一使用小数（`0.15` 代表 `+15%`）。
- 时间字段统一秒（`s`），离线上限等长时段可补充小时冗余字段仅用于展示。

## 4. 核心 Schema（最小可执行集）

### 4.1 global.json
```json
{
  "config_version": "1.0.0",
  "revision": 1,
  "offline_cap_seconds": 28800,
  "offline_efficiency": 0.7,
  "combat_tick_ms": 1000,
  "default_crit_damage_multiplier": 1.5
}
```

### 4.2 combat.json
```json
{
  "damage_formula": "max(1, (atk * skill_coeff) - def)",
  "crit_chance_cap": 0.75,
  "crit_damage_cap": 3.0,
  "stage_power_curve": [
    {"stage_from": 1, "stage_to": 20, "hp_growth": 1.08, "atk_growth": 1.06},
    {"stage_from": 21, "stage_to": 50, "hp_growth": 1.1, "atk_growth": 1.08}
  ]
}
```

### 4.3 professions.json
```json
{
  "professions": [
    {
      "profession_id": "warrior",
      "base_stats": {"hp": 120, "atk": 12, "def": 8},
      "skill_tree_root_ids": ["skill_slash", "skill_guard"]
    }
  ]
}
```

### 4.4 skills.json
```json
{
  "skills": [
    {
      "skill_id": "skill_power_strike",
      "profession_id": "warrior",
      "type": "active",
      "unlock_level": 5,
      "max_level": 10,
      "cooldown_seconds": 8,
      "coeff_by_level": [1.2, 1.28, 1.36]
    }
  ]
}
```

### 4.5 loot_pools.json
```json
{
  "loot_pools": [
    {
      "pool_id": "stage_1_common",
      "guarantee_counter_limit": 30,
      "entries": [
        {"item_id": "iron_sword", "rarity": "common", "weight": 7000},
        {"item_id": "silver_sword", "rarity": "rare", "weight": 2500},
        {"item_id": "gold_sword", "rarity": "epic", "weight": 500}
      ]
    }
  ]
}
```

### 4.6 offline_rewards.json
```json
{
  "reward_rules": {
    "coin_per_min_formula": "stage_base_coin * efficiency",
    "exp_per_min_formula": "stage_base_exp * efficiency",
    "drop_roll_interval_seconds": 60
  },
  "degrade_policy": {
    "missing_stage_config": "fallback_previous_stage",
    "missing_loot_pool": "currency_only"
  }
}
```

## 5. 校验与加载策略

### 5.1 静态校验（CI 必过）
- JSON Schema 校验：字段类型、必填项、枚举值。
- 语义校验：ID 唯一性、引用完整性（`skill.profession_id` 必须存在）。
- 区间校验：概率和倍率在合法范围，成长曲线单调性满足约束。

### 5.2 运行时校验（服务启动/热更）
- 启动阶段：全量校验失败则拒绝启动并保留上次稳定版本。
- 热更阶段：先在影子实例加载，校验通过后再原子切换。
- 客户端：仅消费已签名版本号与摘要，不直接信任本地配置。

### 5.3 版本兼容策略
- 小版本（`x.y+1.z`）：只允许向后兼容新增字段。
- 大版本（`x+1.0.0`）：允许破坏性变更，必须提供迁移脚本与回滚点。
- 任何版本升级必须在 `05-scope-change-log.md` 留痕。

## 6. 默认容错与回滚

- 缺少非关键字段：按 `global.json` 默认值补齐并告警。
- 丢失关键配置（战斗公式、掉落池主键）：阻断发布并回滚至上一 `revision`。
- 线上异常触发阈值（5 分钟内结算失败率 > 1%）：自动切回上一稳定配置。

## 7. 验收标准（DoD）

- 可覆盖 `10/11/12/13/20` 文档全部参数入口并可映射到 API 字段。
- 提供最小样例配置且可通过静态校验。
- 明确热更流程、回滚策略与兼容边界。
- 在 `07-review-log.md` 留存本轮执行闭环记录。

## 8. 与后续文档衔接

- `34-api-contract.md`：字段命名、枚举值、版本号透出策略。
- `33-database-sqlite3-schema.md`：配置快照表、revision 索引、回滚记录表。
- `41-testing-strategy.md`：配置校验测试、兼容性回归、热更与回滚演练。
