# 11-gemini-coverage-analysis

## 调研问题
Google DeepMind Blog 是否可以覆盖所有 Gemini 系列资讯？

## 结论（先给结论）
**不能。** 仅抓取 Google DeepMind Blog 会漏掉大量 Gemini 产品层与云侧发布信息。

## 覆盖链路拆解
Gemini 相关资讯至少分布在以下几条发布链路：

1. **研究/模型能力线（Research/Model）**
   - 来源：Google DeepMind Blog
   - 典型内容：模型代际能力、研究进展、安全评估
   - 覆盖特征：偏“模型与研究”

2. **产品发布线（Consumer/Product）**
   - 来源：Google 官方博客 Gemini 分类
   - 典型内容：Gemini App、功能更新、用户侧体验改动
   - 覆盖特征：偏“产品与功能”

3. **云与企业线（Cloud/Enterprise）**
   - 来源：Google Cloud AI & ML Blog
   - 典型内容：Vertex AI、企业接入、开发者与业务团队能力
   - 覆盖特征：偏“企业落地与开发者接入”

## 证据摘要（本轮抓取）
- DeepMind 页面可见多条 Gemini 模型与研究相关发布（如 Gemini 3.x 系列条目）。
- Google Cloud AI & ML 页面可见 Gemini 在 Cloud/Vertex 侧发布（如 Gemini 3.1 Pro on Google Cloud）。
- Google 官方博客存在 Gemini 产品频道（用于产品与功能侧更新）。

## 采集策略建议（最小可用集合）
为尽量完整覆盖 Gemini 资讯，建议至少接入以下 3 个来源：

- P0-1：Google DeepMind Blog（WEB）
  - URL: `https://deepmind.google/blog/`
- P0-2：Google 官方博客 Gemini 分类（WEB）
  - URL: `https://blog.google/products-and-platforms/products/gemini/`
- P0-3：Google Cloud AI & ML（WEB 或 RSS 若可用）
  - URL: `https://cloud.google.com/blog/products/ai-machine-learning`

## 采集实现建议
- 主策略：三源并行抓取 + 入库去重（URL/标题/语义三级）。
- 分类标签：`research` / `product` / `cloud`。
- 优先级：DeepMind 与 Google Blog（Gemini）为 P0；Cloud 线同为 P0（若面向开发者/企业用户则权重更高）。

## 风险与边界
- Google 博客栏目路径可能调整，需定期健康检查。
- 某些 Gemini 更新可能出现在更泛化 Google Blog 分类中，后续可增补“AI 总栏目”作为兜底源。

## 本任务决策
- DeepMind **不作为唯一来源**。
- Gemini 资讯采用“研究 + 产品 + 云”三线来源合并策略。
