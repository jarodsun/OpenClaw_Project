# 02-analysis

## 信息来源

- 数据来源：历史采集运行结果与失败来源修正记录（ai-global-news）。
- 访谈来源：无。
- 文档来源：项目内记忆记录与来源配置修正结果。

## 通用分析

### 方案选项

- 方案 A：纯 RSS（实现最简单，但 endpoint 失效风险高）
- 方案 B：纯 WEB（适配性高，但解析复杂、维护成本高）
- 方案 C：RSS + WEB 混合（优先 RSS，失效切 WEB）

### 对比维度（通用）

- 可行性：方案 C 最高，可覆盖站点差异。
- 成本：方案 A 最低，方案 C 中等。
- 风险：方案 A 在来源失效时风险最高；方案 C 风险可控。
- 复杂度：方案 C 略高，但可通过标准化配置管理。
- 可扩展性：方案 C 最优。
- 回报周期：方案 C 可快速上线并持续迭代。

## 技术项目专用分析（如适用）

- 技术栈匹配度：与当前采集器（RSS/WEB）完全匹配。
- 架构复杂度：低到中，重点在解析规则维护。
- 集成成本：低，主要为 source 配置更新。
- 可维护性：中，建议建立定期健康检查。
- 性能与稳定性：中到高，依赖站点结构稳定性。
- 安全与合规：仅公开页面抓取，风险可控。

## 商业项目专用分析（如适用）

- 不适用（本调研偏技术与内容来源建设）。

## 关键发现

- 发现 1：DeepMind、Anthropic、The Verge 在本轮采用 WEB 方式更稳。
- 发现 2：Azure AI Blog 的 RSS 可用，应优先 RSS。
- 发现 3：NVIDIA 由分类 RSS 切到全站 blog（WEB）后成功，说明“全站入口”比“细分类 feed”更稳。

## 来源站点结论表

- Google DeepMind Blog  
  - URL：`https://deepmind.google/blog/`  
  - 推荐采集：WEB  
  - 备注：原 RSS endpoint 404，WEB 可用

- Anthropic News  
  - URL：`https://www.anthropic.com/news`  
  - 推荐采集：WEB  
  - 备注：原 RSS endpoint 404，WEB 可用

- Azure AI Blog  
  - URL：`https://azure.microsoft.com/en-us/blog/category/ai-machine-learning/feed/`  
  - 推荐采集：RSS  
  - 备注：修正后 feed 可用

- The Verge AI  
  - URL：`https://www.theverge.com/ai-artificial-intelligence`  
  - 推荐采集：WEB  
  - 备注：RSS endpoint 不稳定，WEB 更稳

- NVIDIA Blog  
  - URL：`https://blogs.nvidia.com/`  
  - 推荐采集：WEB  
  - 备注：分类 RSS 404，切全站 blog 后可用

## 未解问题与信息缺口

- [ ] 尚未建立来源级 SLA（如 7 天成功率阈值）
- [ ] 尚未自动监控网页结构变化
