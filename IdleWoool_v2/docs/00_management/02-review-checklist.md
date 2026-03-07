# v2 评审清单模板（只读）

> 用法：本文件为只读模板，不直接勾选。
> 每轮复制到 `docs/00_management/reviews/YYYYMMDD-HHMM-<TaskPack-ID>-checklist.md` 后再填写与勾选。
> `03-review-log.md` 仅记录该轮 checklist 文件路径。

## 0. 本轮任务包信息
- TaskPack-ID：
- 主题：
- 目标输出文件：
- 本轮状态目标：`done` / `in_progress` / `blocked`

## A. 设计完整性
- [ ] 目标用户与场景明确
- [ ] 规则具备可执行性（不是概念描述）
- [ ] 边界与异常已定义
- [ ] 若为调研层任务包（TP-R*），文档完整性阈值满足（核心章节 >= 8）

## B. 一致性
- [ ] 与其他设计文档术语一致
- [ ] 与 v2 总目标一致（只做设计，不进入开发）
- [ ] 与 `01-execution-plan.md` 的任务包定义一致

## C. 可交接性
- [ ] v3 可据此继续策划细化
- [ ] v5 可据此拆解工程实现
- [ ] 输出里包含可交接字段（输入/规则/输出/约束）

## D. 决策与回滚
- [ ] 本轮关键取舍已记录到 `04-decision-register.md`（如有）
- [ ] 决策记录包含依据/影响范围/回滚条件

## E. TaskPack 验收映射（关键增强）
- [ ] 已核对本任务包“输入”要求
- [ ] 已核对本任务包“输出”文件与章节
- [ ] 已核对本任务包“验收标准”逐条满足
- [ ] 任务包状态已更新（`done` / `in_progress` / `blocked`）

## F. 留痕完整性
- [ ] `03-review-log.md` 已记录本轮 checklist 文件路径
- [ ] `04-decision-register.md` 已更新（如有决策）
- [ ] 本轮提交信息与 TaskPack-ID 一致
