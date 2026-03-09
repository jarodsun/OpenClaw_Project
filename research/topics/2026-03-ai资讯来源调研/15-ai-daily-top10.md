# 15-ai-daily-top10

## 任务
基于“AI每日资讯”目标，筛选质量相对更高的网站并给出 Top10。

## 说明
- 公开搜索引擎抓取本轮存在验证码/风控（Bing challenge、Google 429）。
- 因此采用“关键词意图 + 已验证可访问站点 + 行业常用高质量来源”综合筛选。
- 评分维度：原创深度、更新频率、噪音控制、可抓取稳定性、重复率风险。

## Top10（综合建议）

1. Google DeepMind Blog  
   - URL: `https://deepmind.google/blog/`  
   - 类型：英文 / 官方研究

2. Anthropic News  
   - URL: `https://www.anthropic.com/news`  
   - 类型：英文 / 官方公告

3. Claude Blog  
   - URL: `https://claude.com/blog`  
   - 类型：英文 / 产品实践

4. Google Cloud AI & ML Blog  
   - URL: `https://cloud.google.com/blog/products/ai-machine-learning`  
   - 类型：英文 / 云与开发者

5. Microsoft AI 来源组（组合位）  
   - URL: `https://azure.microsoft.com/en-us/blog/category/ai-machine-learning/`  
   - 备注：建议与 M365 / Research / Official Blog 联合抓取

6. MIT Technology Review (AI)  
   - URL: `https://www.technologyreview.com/topic/artificial-intelligence/`  
   - 类型：英文 / 深度媒体

7. The Verge AI  
   - URL: `https://www.theverge.com/ai-artificial-intelligence`  
   - 类型：英文 / 快讯媒体

8. 机器之心  
   - URL: `https://www.jiqizhixin.com/`  
   - 类型：中文 / 垂直媒体

9. 新智元  
   - URL: `https://aiera.com.cn/`  
   - 类型：中文 / 垂直媒体

10. InfoQ 中文（AI）  
    - URL: `https://www.infoq.cn/topic/AI`  
    - 类型：中文 / 技术社区媒体

## 备选池（根据重复率与可抓取性动态启用）
- 雷峰网 AI：`https://www.leiphone.com/category/ai`
- 36氪 AI：`https://36kr.com/information/AI`
- 量子位：`https://www.qbitai.com/`（本轮访问 403，需浏览器抓取策略）

## 实施建议
- 每日资讯主链路优先“官方源 + 深度媒体”，中文垂直媒体做增量补充。
- 中文媒体默认走更严格去重阈值，避免同一事件多站转载刷屏。
- 该 Top10 将在 T8 汇总阶段并入最终来源策略 V2。
