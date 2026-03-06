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

### 2026-03-06 19:06（执行问题与修复）

- 时间：2026-03-06 19:06 CST
- 现象：执行 `rg -n ...` 进行代码检索时报错 `command not found: rg`。
- 根因：当前环境未安装 ripgrep。
- 处理：回退为 `grep -RIn` 完成检索，任务继续推进。

### 2026-03-06 19:07（执行问题与修复）

- 时间：2026-03-06 19:07 CST
- 现象：执行 `apply_patch` 新增 `APICollector` 时报错 `command not found: apply_patch`。
- 根因：当前终端环境不提供 `apply_patch` 可执行命令。
- 处理：按容错策略回退为 `exec + cat/heredoc` 写入文件并继续执行。

### 2026-03-06 19:07（执行问题与修复）

- 时间：2026-03-06 19:07 CST
- 现象：使用 `perl -0777 -i -pe` 更新 `backend/README.md` 时触发反引号命令替换，产生多条 `command not found`。
- 根因：shell 双引号中包含 markdown 反引号，导致 zsh 将反引号内容当作命令执行。
- 处理：改用 `python3` 脚本进行安全文本替换，文档更新成功。

### 2026-03-06 19:15（执行问题与修复）

- 时间：2026-03-06 19:15 CST
- 现象：执行代码检索命令 `rg -n` 时报错 `command not found: rg`，导致该条复合命令提前失败。
- 根因：当前运行环境未安装 ripgrep（rg）。
- 处理：立即回退为 `find/sed` 组合完成文件检索与状态确认，并继续本次任务。

### 2026-03-06 19:25（执行问题与修复）

- 时间：2026-03-06 19:25 CST
- 现象：执行代码检索命令 `rg -n` 时报错 `command not found: rg`。
- 根因：当前运行环境未安装 ripgrep（rg）。
- 处理：立即回退为 `grep -Rin` 完成检索，并继续本次任务实现（入库重试退避与指标补充）。

### 2026-03-06 19:36（执行问题与修复）

- 时间：2026-03-06 19:36 CST
- 现象：写入 `backend/tests/test_text_normalizer.py` 时报错 `no such file or directory`。
- 根因：`backend/tests/` 目录尚未创建即直接写入文件。
- 处理：按容错策略先执行 `mkdir -p backend/tests`，再用 heredoc 重试写入成功。

### 2026-03-06 19:37（执行问题与修复）

- 时间：2026-03-06 19:37 CST
- 现象：执行 `python3 -m pytest ...` 时报错 `No module named pytest`。
- 根因：当前后端环境未安装 pytest 依赖。
- 处理：回退为标准库 `unittest` 用例并执行 `python3 -m unittest tests/test_text_normalizer.py` 验证通过。

### 2026-03-06 19:46（执行问题与修复）

- 时间：2026-03-06 19:46 CST
- 现象：执行仓库检索命令 `rg --files` 时报错 `command not found: rg`。
- 根因：当前运行环境未安装 ripgrep。
- 处理：回退为 `find ... -type f` 完成文件检索，任务继续。

### 2026-03-06 19:47（执行问题与修复）

- 时间：2026-03-06 19:47 CST
- 现象：执行 `find ... | sed` 时返回 `bad flag in substitute command`。
- 根因：sed 替换表达式包含换行，导致 BSD sed 解析失败。
- 处理：移除该 sed 步骤，直接使用 `find ... | head` 输出文件列表。

### 2026-03-06 19:48（执行问题与修复）

- 时间：2026-03-06 19:48 CST
- 现象：请求未加引号的 URL（包含 `?`）时 zsh 报错 `no matches found`。
- 根因：zsh 将 `?` 解释为通配符并尝试路径展开。
- 处理：为 URL 参数增加单引号，避免通配符展开。

### 2026-03-06 19:50（执行问题与修复）

- 时间：2026-03-06 19:50 CST
- 现象：用 `perl -pe` 更新计划文档时出现 `command not found: WEBCollector`。
- 根因：双引号字符串内含 markdown 反引号，触发 shell 命令替换。
- 处理：去除反引号后重试替换成功，并固定后续文本替换避免反引号出现在双引号命令体中。

### 2026-03-06 19:55（执行问题与修复）

- 时间：2026-03-06 19:55 CST
- 现象：执行仓库扫描命令 `rg --files` 时报错 `command not found: rg`。
- 根因：当前运行环境未安装 ripgrep。
- 处理：按容错策略立即回退为 `find` 完成文件检索，未阻塞本次执行计划推进。

### 2026-03-06 20:05（执行问题与修复）

- 时间：2026-03-06 20:05 CST
- 现象：执行仓库扫描命令 `rg -n ...` 时报错 `command not found: rg`，命令中断。
- 根因：当前运行环境未安装 ripgrep。
- 处理：按容错策略回退为 `grep -RIn` 与 `find` 完成检索，继续推进去重策略实现。

### 2026-03-06 20:07（执行问题与修复）

- 时间：2026-03-06 20:07 CST
- 现象：执行 `python3 -m unittest tests/test_dedup.py` 报错 `ModuleNotFoundError: No module named 'sqlalchemy'`。
- 根因：新增测试直接导入 `Article` ORM 模型，触发对 SQLAlchemy 的运行时依赖；当前环境未安装该依赖。
- 处理：重构 `dedup.py` 为 `TYPE_CHECKING` 条件导入，测试改为 `ArticleStub`，消除该测试路径对 SQLAlchemy 的硬依赖并验证通过。

### 2026-03-06 20:18（执行问题与修复）

- 时间：2026-03-06 20:18 CST
- 现象：执行 `exec + apply_patch` 修改计划文档时报错 `command not found: apply_patch`；执行 `pytest` 报错 `command not found: pytest`；首次执行 `python3 -m unittest tests/test_dedup.py` 报错 `No module named 'tests/test_dedup'`。
- 根因：当前环境未提供 `apply_patch` 可执行命令，且未安装 pytest；另外 unittest 模块路径使用了文件路径写法。
- 处理：按容错策略改为 `exec + python3` 直接修改文档；测试回退为内置 `unittest` 并在 `backend/` 目录使用模块路径 `python3 -m unittest tests.test_dedup`，验证通过。

### 2026-03-06 20:25（执行问题与修复）

- 时间：2026-03-06 20:25 CST
- 现象：执行仓库扫描命令 `rg --files` 时报错 `command not found: rg`。
- 根因：当前运行环境未安装 ripgrep。
- 处理：按容错策略立即回退为 `find` 完成文件检索并继续本次任务。

### 2026-03-06 20:29（执行问题与修复）

- 时间：2026-03-06 20:29 CST
- 现象：执行 `python3 -m unittest tests.test_classifier ...` 首轮失败，断言 `product` 标签未命中。
- 根因：规则分类器 `product` 关键词仅含英文词，未覆盖“发布/上线/更新”等中文高频词。
- 处理：补充中文关键词后重跑同一测试集通过（8/8）。

### 2026-03-06 20:41（执行问题与修复）

- 时间：2026-03-06 20:41 CST
- 现象：执行 `rg --files` 时报错 `command not found: rg`。
- 根因：当前运行环境未安装 ripgrep。
- 处理：按容错策略回退为 `find -maxdepth ... -type f` 完成文件扫描，继续任务。

### 2026-03-06 20:42（执行问题与修复）

- 时间：2026-03-06 20:42 CST
- 现象：执行 `find ... | sed` 时报错 `bad flag in substitute command`。
- 根因：BSD sed 对该替换表达式解析失败。
- 处理：移除不必要 `sed` 步骤，改为直接 `find ... | head` 输出结果。

### 2026-03-06 20:56（执行问题与修复）

- 时间：2026-03-06 20:56 CST
- 现象：执行 `exec + apply_patch` 更新 `backend/app/main.py` 时报错 `command not found: apply_patch`。
- 根因：当前终端环境不提供 `apply_patch` 可执行命令。
- 处理：按容错策略回退为 `exec + cat/heredoc` 覆写文件并继续执行。

### 2026-03-06 20:57（执行问题与修复）

- 时间：2026-03-06 20:57 CST
- 现象：执行 `python3 -m unittest tests/test_api_articles.py` 时报错 `starlette.testclient module requires httpx`。
- 根因：`fastapi.testclient` 依赖 `httpx`，`backend/requirements.txt` 未声明该依赖。
- 处理：补充 `httpx==0.28.1` 到 `backend/requirements.txt`，重新安装依赖后继续测试。

### 2026-03-06 20:58（执行问题与修复）

- 时间：2026-03-06 20:58 CST
- 现象：API 单测首次运行报错 `sqlite3.OperationalError: no such table: articles`。
- 根因：测试使用内存 SQLite 时，每连接独立数据库导致表结构未共享到请求线程。
- 处理：改为 `sqlite+pysqlite:// + StaticPool` 共享连接池，重跑测试通过。

### 2026-03-06 21:26（执行问题与修复）

- 时间：2026-03-06 21:26 CST
- 现象：执行 `exec + apply_patch` 修改 `backend/tests/test_api_articles.py` 时，终端报错 `command not found: apply_patch`。
- 根因：当前终端环境未提供 `apply_patch` 可执行命令。
- 处理：按容错策略回退为可用文件编辑方式继续完成测试用例补充，未中断任务。

### 2026-03-06 21:27（执行问题与修复）

- 时间：2026-03-06 21:27 CST
- 现象：执行 `python3 -m unittest backend/tests/test_api_articles.py` 报错 `ModuleNotFoundError: No module named 'app'`。
- 根因：未设置 `PYTHONPATH=backend`，导致测试运行时找不到后端包路径。
- 处理：改用 `PYTHONPATH=backend python3 -m unittest backend/tests/test_api_articles.py` 重跑，验证通过。

### 2026-03-06 21:36（执行问题与修复）

- 时间：2026-03-06 21:36 CST
- 现象：执行 `exec + apply_patch` 修改 `backend/app/main.py` 时，终端报错 `command not found: apply_patch`。
- 根因：当前终端环境未提供 `apply_patch` 可执行命令。
- 处理：按容错策略立即回退为 `exec + cat/heredoc` 写入方式，后续修改与测试流程正常完成。

### 2026-03-06 21:46（执行问题与修复）

- 时间：2026-03-06 21:46 CST
- 现象：执行 `exec + apply_patch` 更新计划文档时报错 `command not found: apply_patch`。
- 根因：当前终端环境未提供 `apply_patch` 可执行命令。
- 处理：按容错策略立即回退为 `exec + sed/heredoc` 写入方式，后续文档更新与任务交付正常完成。

### 2026-03-06 21:47（执行问题与修复）

- 时间：2026-03-06 21:47 CST
- 现象：尝试使用 `edit` 精确替换 `memory/projects.md` 时返回 `Could not find the exact text`。
- 根因：目标文本与当前文件内容存在细微差异，导致精确匹配失败。
- 处理：按容错策略回退为 `exec + heredoc` 全量写入，进度与阻塞信息已成功更新。

### 2026-03-06 22:27（执行问题与修复）

- 时间：2026-03-06 22:27 CST
- 现象：执行 `exec + apply_patch` 修改 `frontend/app/admin/page.js` 时，终端报错 `command not found: apply_patch`。
- 根因：当前终端环境未提供 `apply_patch` 可执行命令。
- 处理：按容错策略回退为 `exec + cat/heredoc` 重写目标文件，已完成请求地址修复与 token 请求头保留。

### 2026-03-06 22:06（执行问题与修复）

- 时间：2026-03-06 22:06 CST
- 现象：执行 `exec + apply_patch` 修改 `backend/app/core/config.py` 时，终端报错 `command not found: apply_patch`。
- 根因：当前终端环境未提供 `apply_patch` 可执行命令。
- 处理：按容错策略立即回退为 `exec + perl/sed` 直改文件方式，继续完成本次“管理接口鉴权”任务交付。

### 2026-03-06 23:37（执行问题与修复）

- 时间：2026-03-06 23:37 CST
- 现象：执行 `npm -C frontend run lint` 报错 `Missing script: "lint"`。
- 根因：`frontend/package.json` 未定义 `lint` 脚本，仅包含 `dev/build/start`。
- 处理：改为执行 `npm -C frontend run build` 作为本轮前端改动的可执行校验；后续可补充 ESLint 配置与 `lint` 脚本。

### 2026-03-06 23:46（执行问题与修复）

- 时间：2026-03-06 23:46 CST
- 现象：按约定尝试使用 `exec + apply_patch` 更新计划文档时，终端返回 `command not found: apply_patch`。
- 根因：当前环境未提供 `apply_patch` 可执行命令。
- 处理：按容错策略回退为 `exec + perl -0777 -i` 文本替换，完成 `docs/03-execution-plan.md` 更新并校验生效。
