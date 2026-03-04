# AI Global News - 首批数据源优先级

## A. 高优先级（MVP 首周接入）

1. OpenAI Blog（产品与模型发布）
2. Google DeepMind Blog
3. Anthropic News/Blog
4. Meta AI Blog
5. Microsoft Research / Azure AI Blog
6. NVIDIA Blog (AI)
7. Hugging Face Blog
8. arXiv cs.AI / cs.LG / cs.CL（论文）
9. GitHub Trending（AI 相关仓库）
10. Hacker News（AI 关键词流）
11. TechCrunch AI
12. The Verge AI

## B. 中优先级（MVP 第二周接入）

13. VentureBeat AI
14. MIT Technology Review (AI)
15. Stability AI Blog
16. Mistral AI News
17. Perplexity Blog
18. Cohere Blog
19. Databricks AI Blog
20. AWS AI / ML Blog

## C. 低优先级（后续扩展）

- 各国监管机构 AI 政策公告
- 专家博客与 Newsletter（需质量控制）
- X/Twitter 账号流（需 API 与噪音治理）

## 接入策略

- 优先 RSS / 官方 API
- 无 RSS 时使用网页解析（限速 + 失败重试）
- 每个来源定义独立解析器，统一输出到 Canonical Schema
