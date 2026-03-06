# 42-可观测性与日志（Observability & Logs）

更新时间：2026-03-07

## 1. 文档目标与范围

### 1.1 目标
- 为 IdleWoool 首版建立“可定位、可告警、可追溯”的观测基线。
- 在不引入重型平台的前提下，先实现本地与单机部署可落地的最小闭环。
- 与 `32-backend-fastapi-architecture.md`、`34-api-contract.md`、`41-testing-strategy.md` 对齐，保证联调与上线验收口径一致。

### 1.2 范围
- In Scope：后端 API、战斗结算、离线收益领取、存档同步、前端关键页面交互与错误采集。
- Out of Scope：复杂分布式追踪平台、自建大数据日志仓库、跨地域多集群可观测体系。

## 2. 可观测模型

### 2.1 三支柱（Logs / Metrics / Traces）
- Logs：结构化业务日志与审计日志，支持按 `request_id` 与 `player_id` 检索。
- Metrics：服务健康、性能、业务产出与错误率指标，用于告警与趋势观察。
- Traces：首版采用“轻量链路字段透传”替代完整 APM，记录关键耗时分段。

### 2.2 统一上下文字段
- `timestamp`：ISO8601（UTC 存储，展示按 Asia/Shanghai 转换）。
- `level`：`DEBUG` / `INFO` / `WARN` / `ERROR`。
- `service`：固定 `idlewoool-backend` / `idlewoool-frontend`。
- `env`：`local` / `staging` / `prod`。
- `request_id`：由网关或后端生成并全链路透传（写接口强制）。
- `player_id`：匿名化后记录（明文禁止入日志）。
- `session_id`：会话标识（可空）。
- `event`：业务事件名（如 `offline_reward_claimed`）。
- `error_code`：与 `34-api-contract.md` 错误码一致。

## 3. 日志设计

### 3.1 日志分层
- 应用日志：接口请求、响应摘要、关键业务动作、性能统计。
- 业务审计日志：资源变更、领奖发放、配置生效、异常回滚。
- 安全日志：登录失败、频率限制触发、疑似篡改参数拒绝。

### 3.2 结构化日志格式（JSON Lines）

```json
{
  "timestamp": "2026-03-07T06:55:12Z",
  "level": "INFO",
  "service": "idlewoool-backend",
  "env": "staging",
  "request_id": "req_7f9a...",
  "player_id": "p_hash_9bc...",
  "event": "offline_reward_claimed",
  "cost_ms": 24,
  "result": "success",
  "reward_gold": 1280
}
```

### 3.3 日志脱敏与禁止项
- 禁止记录：明文 token、手机号、邮箱、完整 IP、支付敏感信息。
- 玩家标识统一哈希化，哈希算法与盐值由后端配置控制。
- 错误堆栈默认采集，但返回客户端时只暴露标准错误码与简述。

### 3.4 日志留存与轮转
- 本地开发：保留 7 天，单文件上限 100MB，按天切分。
- 预发环境：保留 14 天，支持 grep 与 `request_id` 快速检索。
- 生产首版：保留 30 天，按级别分流（`ERROR` 单独索引）。

## 4. 指标体系与告警

### 4.1 技术指标
- API 可用性：`http_success_rate`（5 分钟窗口）。
- 延迟：`http_p95_ms`、`http_p99_ms`（按接口拆分）。
- 错误率：`http_5xx_rate`、`business_error_rate`。
- 资源：CPU、内存、磁盘使用率与 SQLite 锁等待时长。

### 4.2 业务指标
- `combat_tick_success_rate`：战斗 tick 成功率。
- `offline_claim_success_rate`：离线领取成功率。
- `save_conflict_rate`：存档冲突率。
- `new_player_10min_retention_proxy`：新玩家 10 分钟留存代理指标。

### 4.3 告警阈值（首版）
- P1：`http_5xx_rate > 3%` 持续 5 分钟。
- P1：`offline_claim_success_rate < 97%` 持续 10 分钟。
- P2：核心接口 `p95 > 400ms` 持续 10 分钟。
- P2：`save_conflict_rate > 1%` 持续 10 分钟。
- P3：磁盘使用率 > 80% 持续 30 分钟。

## 5. 链路追踪最小实现

### 5.1 后端关键分段耗时
- `parse_request_ms`
- `load_player_state_ms`
- `compute_reward_or_combat_ms`
- `db_commit_ms`
- `serialize_response_ms`

### 5.2 前端性能采样
- 首屏渲染时间（FCP/LCP 简化采样）。
- 关键操作耗时：进入战斗、领取离线收益、装备切换。
- 上报失败不阻塞主流程，失败仅记录本地降级日志。

## 6. 运行手册（Runbook）

### 6.1 故障定位标准流程
1. 按告警事件找到时间窗口与影响接口。
2. 以 `request_id` 检索后端应用日志与审计日志。
3. 对照关键分段耗时确认瓶颈位置（计算 / DB / 序列化）。
4. 需要回放时使用脱敏请求样本在 staging 复现。
5. 产出事故记录：根因、影响范围、修复与预防项。

### 6.2 常见场景处理
- 离线领奖失败激增：优先检查幂等键冲突、离线时长计算与配置加载状态。
- 存档冲突率上升：检查版本号推进、客户端重试风暴、DB 锁等待。
- 接口尾延迟上升：检查慢 SQL、日志 I/O 放大、频繁全量序列化。

## 7. 与测试和发布流程的衔接
- 测试阶段必须覆盖观测断言：关键接口有日志、有指标、有错误码映射。
- 提测门禁：核心链路日志字段完整率 100%，关键指标采集可见。
- 发布门禁：连续 24h 无 P1 告警，P2 告警已闭环。
- 与 `41-testing-strategy.md` 联动：回归用例需包含日志与告警校验步骤。

## 8. DoD（完成定义）
- 已定义统一日志字段、脱敏规则、留存与轮转策略。
- 已定义技术/业务指标与首版告警阈值。
- 已提供可执行故障排查 Runbook 与常见场景处理。
- 已明确与测试、发布门禁的观测联动要求。

## 9. 后续衔接
- 下一文档：`43-security-and-cheat-prevention.md`（将安全事件接入同一观测体系）。
- 实装阶段优先任务：在 FastAPI 中间件落地 `request_id` 透传与结构化日志输出。
