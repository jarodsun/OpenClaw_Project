# 00-execution-plan-v2

## 目标
按“开发项目”方式推进 AI 资讯来源扩展调研：先规划、再按单项任务逐个完成，每项可验收。

## 本轮已纳入的用户修正（来自上一轮对话）
1. 验证 Google DeepMind Blog 是否可覆盖 Gemini 全系列资讯（结论预期：不能单源覆盖）。
2. 评估 `anthropic.com/news` 与 `claude.com/blog` 重合度，决定抓一个还是两个。
3. 微软来源不能只看 Azure，需细化到产品/研究/公司发布多线来源。
4. 英文其他来源暂维持。
5. 新智元域名修正为：`https://aiera.com.cn/`。
6. 雷峰网 AI 与 AI 科技评论 URL 重复，需合并来源策略。
7. 中文资讯重复率偏高，需单独做去重策略调研。
8. 以“AI每日资讯”为关键词再检索一轮，给出质量更高的 Top10 站点。

## 执行策略（单项完成制）
- 原则：每次只完成一个任务，完成后给出结果与下一任务建议。
- 验收：每个任务都有明确产出文件和可执行结论。

## 任务分解（WBS）
### T1（当前执行）
- 内容：固化 v2 规划 + 上一轮对话修正摘要。
- 产出：`00-execution-plan-v2.md`、`99-round2-summary.md`。
- 验收标准：8 条修正全部入文档并可追溯。

### T2
- 内容：Gemini 资讯覆盖链路调研（DeepMind vs Google Blog vs Google Cloud 等）。
- 产出：`11-gemini-coverage-analysis.md`。
- 验收标准：给出“必抓来源最小集合 + 采集方式”。

### T3
- 内容：Anthropic News vs Claude Blog 重合度评估。
- 产出：`12-anthropic-claude-overlap.md`。
- 验收标准：给出重合率区间估计、双抓/单抓决策。

### T4
- 内容：微软 AI 资讯多源拆分与完整性评估。
- 产出：`13-microsoft-ai-source-map.md`。
- 验收标准：形成微软来源矩阵（平台/产品/研究/官方）。

### T5
- 内容：中文来源清洗（域名修正、重复来源合并）。
- 产出：`14-cn-source-normalization.md`。
- 验收标准：去重后中文来源清单可直接落配置。

### T6
- 内容：“AI每日资讯”关键词二次调研并选 Top10。
- 产出：`15-ai-daily-top10.md`。
- 验收标准：Top10 含评分维度（原创率/更新频率/噪音/稳定性/重复率）。

### T7
- 内容：中文高重复专项去重策略。
- 产出：`16-cn-dedup-strategy.md`。
- 验收标准：给出 URL/标题/语义三级去重参数建议。

### T8
- 内容：汇总决策并更新主文档。
- 产出：更新 `02-analysis.md`、`03-decision.md`、`04-next-actions.md` 与 `sources/*`。
- 验收标准：形成可直接实施的来源策略 V2。
