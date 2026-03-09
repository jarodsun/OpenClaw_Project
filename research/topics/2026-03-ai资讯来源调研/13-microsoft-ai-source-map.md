# 13-microsoft-ai-source-map

## 调研问题
微软 AI 新闻如果只从 Azure 获取，是否全面？

## 结论（先给结论）
**不全面。** Azure AI 只能覆盖“云平台与模型接入”这一条主线，无法完整覆盖微软 AI 在产品层、研究层与公司战略层的发布。

## 微软 AI 资讯来源矩阵（建议）

### 1) 平台/开发者线（Platform）
- 来源：Azure AI + Machine Learning Blog
- URL：`https://azure.microsoft.com/en-us/blog/category/ai-machine-learning/`
- 覆盖：Foundry、模型接入、数据平台、云侧能力更新
- 推荐优先级：P0

### 2) 产品/办公协作线（Product）
- 来源：Microsoft 365 Blog（含 Copilot 相关）
- URL：`https://www.microsoft.com/en-us/microsoft-365/blog/`
- 覆盖：Copilot、Agent、Office/Teams 端产品更新与商用策略
- 推荐优先级：P0

### 3) 研究/前沿线（Research）
- 来源：Microsoft Research Blog
- URL：`https://www.microsoft.com/en-us/research/blog/`
- 覆盖：模型研究（如 Phi 系列）、科研成果、方法论文落地
- 推荐优先级：P1（面向技术用户可升 P0）

### 4) 公司战略/重大事件线（Corporate）
- 来源：The Official Microsoft Blog
- URL：`https://blogs.microsoft.com/`
- 覆盖：合作、战略声明、重大组织级 AI 发布
- 推荐优先级：P0

## 为什么只抓 Azure 不够
- 会漏掉 M365/Copilot 的大量产品更新（用户可感知变化主要在这一层）。
- 会漏掉 Research 线的重要模型进展（如 Phi 相关）。
- 会漏掉公司层面的政策/合作/重大声明（影响市场判断）。

## 推荐抓取策略（微软专组）
- 采用“四线并抓”：Azure + M365 + Research + Corporate。
- 入库时打标签：`ms_platform` / `ms_product` / `ms_research` / `ms_corporate`。
- 同主题归并：例如同一天在 Corporate 与 Azure 同时发布的消息，归并为单主题多来源。

## 去重建议（微软专组）
1. URL 标准化去重
2. 标题归一化（去品牌前后缀）
3. 语义相似度（同日同主题阈值较高）

## 本任务决策
- 微软来源不再单点依赖 Azure。
- 采用“4 来源矩阵”作为微软 AI 新闻标准接入方案。
