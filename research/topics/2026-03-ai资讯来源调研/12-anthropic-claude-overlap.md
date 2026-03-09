# 12-anthropic-claude-overlap

## 调研问题
`https://www.anthropic.com/news` 与 `https://claude.com/blog` 的重合度高不高？应该抓一个还是两个？

## 结论（先给结论）
- **重合度：中等偏低（建议按 20%~40% 区间看待）**。
- **抓取策略：两个都抓，不建议二选一**。

## 结构性差异

### Anthropic News（公司级）
- 内容重心：公司公告、政策立场、国家安全/治理声明、重大模型发布。
- 典型栏目：Announcements、Product（少量）、战略声明。
- 角色定位：**官方总入口（corporate layer）**。

### Claude Blog（产品与实践级）
- 内容重心：Claude 产品功能、企业实践、开发者工作流、Claude Code/Agents 用例。
- 典型栏目：Product announcements、Enterprise AI、Claude Code、Agents。
- 角色定位：**产品与应用入口（product/use-case layer）**。

## 为什么不是高重合
- 同一重大节点（如模型发布）可能双站都出现，但呈现角度不同：
  - News 更偏“官方声明/战略语境”；
  - Claude Blog 更偏“功能细节/落地实践”。
- Claude Blog 的大量实践类文章在 Anthropic News 不会完整覆盖。

## 推荐抓取方案

- P0：Anthropic News（WEB）
  - URL: `https://www.anthropic.com/news`
  - 用途：官方公告与公司级事件基线

- P0：Claude Blog（WEB）
  - URL: `https://claude.com/blog`
  - 用途：产品更新、开发者/企业实践细节

## 去重与归并建议
- 去重维度：
  1) URL 归一化
  2) 标题标准化（去前后缀）
  3) 语义相似度（同日发布阈值可更严格）
- 归并策略：若同主题双源出现，保留两条但标记“官方声明版 / 产品实践版”。

## 本任务决策
- **最终决策：两个都抓。**
- 只抓一个会损失信息完整性：
  - 只抓 News 会漏产品实操；
  - 只抓 Claude Blog 会漏公司/政策级公告。
