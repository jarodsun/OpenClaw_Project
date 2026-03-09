# 14-cn-source-normalization

## 任务目标
完成中文 AI 资讯来源的规范化：域名修正、重复来源合并、可抓取性标注。

## 本轮修正结果

### 1) 新智元域名修正
- 旧记录：`https://www.aixinzhi.com/`（错误）
- 新记录：`https://aiera.com.cn/`（确认可访问）
- 处理结论：以 `aiera.com.cn` 作为唯一标准域名。

### 2) 雷峰网 AI 与 AI 科技评论重复问题
- 现状：两者在当前采集口径里指向同一主站 AI 分类页。
- 标准 URL：`https://www.leiphone.com/category/ai`
- 处理结论：合并为一个来源，来源名建议统一为“雷峰网 AI（含 AI 科技评论内容域）”。

### 3) 站点可抓取性快速校验
- 新智元 `aiera.com.cn`：可访问（200）
- 雷峰网 AI：可访问（200）
- 机器之心：可访问（200）
- 量子位 `qbitai.com`：本轮 `web_fetch` 返回 403（需要浏览器抓取或代理策略）

## 标准化后的中文来源（当前建议）

- 机器之心：`https://www.jiqizhixin.com/`
- 量子位：`https://www.qbitai.com/`（标记：抗抓取风险）
- 新智元：`https://aiera.com.cn/`
- 雷峰网 AI（合并 AI 科技评论）：`https://www.leiphone.com/category/ai`
- InfoQ 中文（AI）：`https://www.infoq.cn/topic/AI`

## 落地规则
- 同源别名归并：
  - `aixinzhi.com` -> `aiera.com.cn`
  - `雷峰网AI` + `AI科技评论` -> `leiphone/category/ai`
- 入库字段新增：`source_canonical`（标准来源名）与 `source_aliases`（别名列表）。

## 本任务决策
- 已完成中文来源规范化第一轮。
- 下一步进入 T6：基于“AI每日资讯”关键词再筛选高质量中文来源 Top10。
