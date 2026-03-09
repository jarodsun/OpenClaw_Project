# 21-round3-niche-vertical-sources

## 第三轮调研目标
聚焦“小众、垂直细分”的 AI 资讯来源，补齐主流站点之外的高信噪比来源池。

## 你给的线索核查（ai-bot）
- 已核查：`https://ai-bot.cn/daily-ai-news/`
- 观察：该页面本身是“聚合快讯页”，内容来自多源并带来源标注。
- 本轮结果：**未在页面中直接抽取到公开 Notion 页面链接**。
- 判断：你提到的“作者把一手资讯放 Notion 再做网页”这条线索很可能存在，但可能已迁移、隐藏在脚本、或需浏览器交互后才可见。

## 可用的小众/垂直来源（英文）

### A. 技术研究与前沿解读（高质量、偏深度）
1. Import AI（Jack Clark）
   - https://www.importai.net/
   - 特点：政策+研究+产业交叉，信噪比高
2. Interconnects AI（Nathan Lambert）
   - https://www.interconnects.ai/
   - 特点：前沿实验室动态与技术解读
3. Latent.Space
   - https://www.latent.space/
   - 特点：AI Engineer 视角，模型/Agent/Infra
4. Last Week in AI
   - https://lastweekin.ai/
   - 特点：周报型汇总，覆盖面广、复盘友好
5. The Batch（DeepLearning.AI）
   - https://www.deeplearning.ai/the-batch/
   - 特点：新闻+洞察，偏稳健

### B. 产业链垂直（芯片/算力/基础设施）
6. SemiAnalysis
   - https://semianalysis.com/
   - 特点：AI算力、芯片、供应链、商业化分析
7. Turing Post
   - https://www.turingpost.com/
   - 特点：技术与产业交叉，专题化较强

## 可用的小众/垂直来源（中文）
1. AI工具集每日AI资讯（聚合枢纽）
   - https://ai-bot.cn/daily-ai-news/
2. 机器之心（技术偏深）
   - https://www.jiqizhixin.com/
3. 新智元（产业+技术）
   - https://aiera.com.cn/
4. InfoQ AI（工程实践偏多）
   - https://www.infoq.cn/topic/AI

## 关于“Notion一手资讯页”的处理建议
- 当前结论：线索可信，但未完成直接定位。
- 下一步建议（可执行）：
  1) 用浏览器人工检索（登录态/交互态）追踪 `notion.site` / `notion.so` 链接；
  2) 在 ai-bot 页面源码与其站内“每日资讯”上下游页面继续反查；
  3) 找到后将其列为“P1-人工精选源”，并单独做低频抓取（避免重复灌入）。

## 本轮结论
- 已建立第三轮“小众垂直来源”候选池（英文7 + 中文4）。
- Notion线索已核查但尚未定位到确切公开页，进入下一子任务追踪。
