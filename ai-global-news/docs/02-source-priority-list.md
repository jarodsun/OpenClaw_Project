# AI Global News - 首批数据源优先级

## A. 高优先级（MVP 首周接入）

1. OpenAI Blog（产品与模型发布）
   - 官方链接：<https://openai.com/news/>
2. Google DeepMind Blog
   - 官方链接：<https://deepmind.google/blog/>
3. Anthropic News/Blog
   - 官方链接：<https://www.anthropic.com/news>
4. Meta AI Blog
   - 官方链接：<https://ai.meta.com/blog/>
5. Microsoft Research / Azure AI Blog
   - 官方链接（Microsoft Research）：<https://www.microsoft.com/en-us/research/blog/>
   - 官方链接（Azure AI）：<https://azure.microsoft.com/en-us/blog/category/ai-machine-learning/>
6. NVIDIA Blog (AI)
   - 官方链接：<https://blogs.nvidia.com/blog/category/deep-learning/>
7. Hugging Face Blog
   - 官方链接：<https://huggingface.co/blog>
8. arXiv cs.AI / cs.LG / cs.CL（论文）
   - 官方链接（cs.AI）：<https://arxiv.org/list/cs.AI/recent>
   - 官方链接（cs.LG）：<https://arxiv.org/list/cs.LG/recent>
   - 官方链接（cs.CL）：<https://arxiv.org/list/cs.CL/recent>
9. GitHub Trending（AI 相关仓库）
   - 官方链接（Trending）：<https://github.com/trending>
   - 官方链接（AI Topic）：<https://github.com/topics/artificial-intelligence>
10. Hacker News（AI 关键词流）
   - 官方链接：<https://news.ycombinator.com/>
11. TechCrunch AI
   - 官方链接：<https://techcrunch.com/tag/artificial-intelligence/>
12. The Verge AI
   - 官方链接：<https://www.theverge.com/ai-artificial-intelligence>

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
