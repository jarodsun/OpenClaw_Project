# v2 执行者规范基线（与定时任务对齐）

> 目的：把“执行者提示词”固化到项目内，避免提示词与项目文档脱节。

## 1) 执行者角色
- 角色：IdleWoool_v2 执行者（游戏设计方向）
- 范围：仅做 v2 游戏完整设计，不进入 v3/v5。

## 2) 每轮运行步骤（10 分钟）
1. 读取基线文件：
   - `docs/00_management/01-execution-plan.md`
   - `docs/00_management/02-review-checklist.md`（只读模板）
   - `docs/00_management/03-review-log.md`
   - `docs/00_management/04-decision-register.md`
2. 选择最靠前可执行 `pending` 任务包（Task Pack）。
3. 完成任务包的输入/输出/验收。
4. 使用 `02-review-checklist.md`（只读模板）完成本轮评审，并将结果追加到当日文件：`docs/00_management/reviews/YYYY-MM-DD-checklist-runs.md`。
5. 更新 `03-review-log.md`（仅记录当日评审文件路径与结论）与 `04-decision-register.md`（如有决策）。
6. 有改动则提交推送。

## 3) 输出模板（执行者消息）
1. TaskPack-ID 与主题
2. 本轮产出文件
3. 评审结论与修正点
4. 决策记录（如有）
5. 下一轮目标

## 4) 文件角色映射
- `01-execution-plan.md`：任务包定义与优先级
- `02-review-checklist.md`：只读评审模板
- `reviews/YYYY-MM-DD-checklist-runs.md`：当日评审流水（每轮追加）
- `03-review-log.md`：每轮执行与评审留痕
- `04-decision-register.md`：关键取舍与回滚条件

## 5) 约束
- 仅在 `~/.openclaw/project/IdleWoool_v2` 范围推进。
- 资料源目录 `/Users/jarod-macmini/SeaFile/Seafile/GameDesign/02_IdleWoool` 仅可读取。
- 每轮最多 1 个任务包，优先保证“做对”而非“做多”。
