# 09 Open Questions（待你拍板）

> 仅记录“必须由你决策”的问题；不阻塞执行者推进其他可做事项。

## 状态说明
- `open`：待决策
- `decided`：已决策（同步到 `08-decision-register.md`）
- `obsolete`：问题失效

## 模板

### Q-XXX 标题（status: open）
- 提出时间：
- 触发场景：
- 选项：
  - A：
  - B：
  - C：
- 建议：
- 若不决策的默认处理：
- 影响范围：

### Q-001 离线收益最终口径（status: open）
- 提出时间：2026-03-07 04:20（Asia/Shanghai）
- 触发场景：`02-game-design-core-loop.md` 已给出默认值（8h、70%），但需产品最终拍板以避免后续联调返工。
- 选项：
  - A：离线时长上限 8h，效率 70%（稳健平衡）
  - B：离线时长上限 12h，效率 60%（照顾轻度玩家）
  - C：离线时长上限 8h，效率 80%（更快成长、节奏偏激进）
- 建议：A
- 最晚拍板时间：2026-03-10 18:00（Asia/Shanghai）
- 若不决策的默认处理：按 A 继续推进后续文档与接口设计
- 超期默认处理：超过最晚拍板时间仍未决策，则继续按 A 执行，直至出现明确拍板结论
- 影响范围：`13-system-offline-rewards.md`、`20-balance-framework.md`、`34-api-contract.md`

