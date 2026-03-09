# 02-analysis（V2）

## 信息来源
- 历史采集修正结果（ai-global-news）
- 专项调研文档：`11~16`（Gemini覆盖、Anthropic/Claude重合、微软矩阵、中文规范化、Top10、去重策略）

## 关键专项结论汇总

### 1) Gemini 覆盖
- 仅 DeepMind 不足以覆盖 Gemini 全量资讯。
- 最小覆盖集合：
  - DeepMind（研究/模型）
  - Google Blog Gemini（产品）
  - Google Cloud AI&ML（云与企业）

### 2) Anthropic News vs Claude Blog
- 重合度中等偏低（约 20%~40%）。
- 两者定位不同：
  - News：公司级公告/战略
  - Claude Blog：产品与实践
- 结论：两个都抓。

### 3) 微软来源完整性
- 只抓 Azure 不全面。
- 推荐“4线矩阵”：
  - Azure AI（平台）
  - Microsoft 365 Blog（产品/Copilot）
  - Microsoft Research（研究）
  - Official Microsoft Blog（公司战略）

### 4) 中文来源规范化
- 新智元标准域名：`https://aiera.com.cn/`
- “雷峰网AI / AI科技评论”合并为同一来源：`https://www.leiphone.com/category/ai`

### 5) 中文重复率问题
- 采用“三级去重+两级保护”：
  - URL规范化 -> 标题hash -> 语义相似
  - 官方源优先 + 角度差异保护

## Top10（AI每日资讯）收敛结果
1. DeepMind Blog
2. Anthropic News
3. Claude Blog
4. Google Cloud AI&ML
5. Microsoft AI来源组（组合位）
6. MIT Technology Review (AI)
7. The Verge AI
8. 机器之心
9. 新智元（aiera.com.cn）
10. InfoQ 中文（AI）

## 分层接入建议（P0/P1/P2）
- P0（必须）：官方源与核心产品源（Google/Anthropic/Microsoft 关键线）
- P1（建议）：高质量媒体深度源（MIT TR、The Verge、机器之心、新智元、InfoQ）
- P2（备选）：高重复或抗抓取风险源（雷峰网、36氪、量子位）

## 未解问题
- 来源级 SLA 需接入自动统计
- 语义去重阈值需用真实样本再调参（尤其中文）
