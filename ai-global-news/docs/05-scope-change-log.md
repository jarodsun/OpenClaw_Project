# 05 Scope Change Log（范围基线与变更）

## Baseline v1（冻结）

- 冻结时间：2026-03-05
- 范围：
  - 多源采集（>=20）
  - 清洗、去重、标签、中文摘要
  - API（列表/详情/搜索/过滤）
  - 前端（列表/详情/标签筛选）
- 上线门禁：参见 `04-acceptance-test-plan.md`

## 变更规则

- P0 变更（影响上线门禁）：必须评审并更新验收计划
- P1 变更（影响排期）：需记录风险与回滚方案
- P2 变更（优化项）：可进入待办池

## 变更记录

### 2026-03-05

- 变更：新增评审闭环文档（需求评审、指标评审、验收计划）
- 原因：原需求文档缺少评审闭环与可测口径
- 影响：开发开始前需先按评审结论修订指标口径
- 状态：已纳入 v1 基线

### 2026-03-06 17:57（执行问题与修复）

- 时间：2026-03-06 17:57 CST
- 现象：按约定尝试使用 `exec + apply_patch` 修改项目文件时，终端返回 `command not found: apply_patch`。
- 根因：当前运行环境未提供 `apply_patch` 可执行命令。
- 处理：立即回退为 `exec` 下 `cat/heredoc` 覆写与新建文件策略，继续完成 SQLite3 模型与 Alembic 迁移脚本落地；已通过 `python3 -m compileall app alembic` 验证语法。

### 2026-03-06 18:00（执行问题与修复）

- 时间：2026-03-06 18:00 CST
- 现象：一次性执行“heredoc + && git commit”的复合命令时报 `parse error near '&&'`。
- 根因：zsh 对该段复合命令的换行拼接解析失败。
- 处理：拆分为多条独立命令（清理缓存、写 `.gitignore`、再 `git add/commit`）后成功。

### 2026-03-06 18:05（执行问题与修复）

- 时间：2026-03-06 18:05 CST
- 现象：执行仓库扫描命令 `rg --files` 时报错 `command not found: rg`。
- 根因：当前运行环境未安装 ripgrep。
- 处理：立即切换为 `find . -type f` 完成文件枚举，不阻塞本次任务推进。

### 2026-03-06 18:34（执行问题与修复）

- 时间：2026-03-06 18:34 CST
- 现象：写入 `backend/scripts/seed_high_priority_sources.py` 首次失败，报错 `no such file or directory`。
- 根因：`backend/scripts/` 目录尚未创建。
- 处理：先执行 `mkdir -p backend/scripts`，随后使用 heredoc 重试写入成功。

### 2026-03-06 18:35（执行问题与修复）

- 时间：2026-03-06 18:35 CST
- 现象：尝试使用 `apply_patch` 命令更新 `__init__.py`，报错 `command not found: apply_patch`。
- 根因：当前环境未提供 `apply_patch` 可执行程序。
- 处理：回退为 `cat/heredoc` 直接重写目标文件并继续执行。

### 2026-03-06 18:36（执行问题与修复）

- 时间：2026-03-06 18:36 CST
- 现象：执行 `python scripts/seed_high_priority_sources.py` 报错 `command not found: python`；改用 `python3` 后再次报错 `ModuleNotFoundError: No module named 'sqlalchemy'`。
- 根因：环境仅提供 `python3`，且未安装后端依赖。
- 处理：改用 `python3 -m compileall` 做语法级验证；将“安装依赖后执行种子脚本”登记为下一步阻塞解除动作。

### 2026-03-06 18:45（执行问题与修复）

- 时间：2026-03-06 18:45 CST
- 现象：按流程尝试用 `exec` 调用 `apply_patch` 修改 `backend/app/main.py`，返回 `command not found: apply_patch`。
- 根因：当前环境无 `apply_patch` shell 命令，仅支持常规 shell 与 heredoc 写入。
- 处理：立即回退为 `cat/heredoc` 直接覆写文件并继续执行；随后用 `python3 -m compileall backend/app` 完成语法验证。

### 2026-03-06 18:56（执行问题与修复）

- 时间：2026-03-06 18:56 CST
- 现象：执行仓库文件扫描命令 `rg --files` 时报错 `command not found: rg`。
- 根因：当前执行环境未安装 ripgrep。
- 处理：即时回退为 `find . -maxdepth 4 -type f` 完成文件发现，未影响本次“失败重试闭环”实现。
