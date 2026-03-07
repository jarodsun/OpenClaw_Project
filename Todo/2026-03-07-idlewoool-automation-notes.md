# 2026-03-07 对话纪要：IdleWoool 自动化与治理

## 背景
本次对话围绕 `IdleWoool` 项目文档治理、执行者定时任务、评审闭环机制、记忆文件维护策略展开。

## 关键决策

### 1) 项目与资料管理
- 新项目路径：`~/.openclaw/project/IdleWoool`
- 资料源目录：`/Users/jarod-macmini/SeaFile/Seafile/GameDesign/02_IdleWoool`
- 资料源目录约束：**仅可读取，不可写入/移动/删除**。
- `woool_data` 已复制到项目内参考目录：
  - `IdleWoool/data/reference/woool_data/`

### 2) 文档结构重构
- `docs` 下分层为两类：
  - `docs/00_management/`：管理与跟踪文档
  - `docs/10_game_design/`：游戏开发文档
- `docs/00-docs-index.md` 已更新为新结构并纳入参考数据路径。

### 3) 执行者定时任务策略
- 只保留“执行者”，不启用监督者。
- 任务：`idlewoool-doc-executor-10min`
- jobId：`17afb69f-392b-4d6b-9d40-09d8ea4f7ec1`
- 输出频道固定：`1478835503024574545`
- 任务支持启停，当前最近状态按用户指令进行切换（最终以 cron 实时状态为准）。

### 4) 评审机制（最终版）
- 采用：**持续执行 + 评审闭环 + 待拍板问题池**。
- 不要求每步停下等待人工确认。
- 每轮流程：执行 -> 自评审 -> 自动修正 -> 复评审 -> 归档。
- 需用户拍板的问题沉淀到 `docs/00_management/09-open-questions.md`，不阻塞其他可推进事项。
- 管理文档补齐：
  - `06-review-checklist.md`
  - `07-review-log.md`
  - `08-decision-register.md`
  - `09-open-questions.md`

### 5) 执行计划细化
- `03-execution-plan.md` 已改为“按阶段（D1~D5）”推进，不按周。
- 用户明确要求：
  - `完成 01-product-requirements.md` 状态应为未完成（`[ ]`）。
- 相关联动已同步到 `05-scope-change-log.md`。

### 6) 记忆维护规则调整
- `memory/projects.md` 改为“覆盖式快照”维护：
  - 每个项目仅保留：最新进展 / 当前状态 / 硬性要求
- 过程增量记录统一写入各项目：
  - `docs/00_management/05-scope-change-log.md`
- 上述规则已写入 `MEMORY.md` 存储规范。

## 过程中的修正点
- 曾将 README 误按“移动”处理，后按用户澄清改为“复制”语义并恢复源文件。
- 文档重构后出现 GitHub 与本地显示不一致，原因是旧路径删除未提交；后续已补提删除记录并推送。

## 额外问答结论
- 能力对比：编码能力整体更稳定；在“把策划转为可执行方案并持续推进”方面具备优势。
- 多 Agent 运行建议：
  - 多会话并行 / 子代理并行 / 多 cron 并行
  - 强调职责隔离、目录隔离、通道明确、状态落盘。

## 后续建议
- 继续按 D2->D5 阶段推进文档完善与评审闭环。
- 用户有空时处理 `09-open-questions.md` 中待拍板项。
- 根据文档收敛情况再启动代码实现与联调。
