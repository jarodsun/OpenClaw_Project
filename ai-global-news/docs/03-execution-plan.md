# AI Global News - 执行计划（到可上线）

## Phase 0：项目初始化（当前）

- [x] 创建项目目录
- [x] 明确需求与 MVP 验收指标
- [x] 产出首批来源优先级

## Phase 1：后端骨架（第 1-2 天）

- [x] 初始化 FastAPI 工程
- [x] 定义配置体系（env/dev/prod）
- [x] 建立 SQLite3 数据模型与迁移脚本
- [x] 接入基础日志与健康检查接口

## Phase 2：采集与入库（第 3-6 天）

- [x] 设计采集器接口（RSS/API/Web）
- [x] 接入首批 12 个高优先级来源
  - 进展：已落地 WEBCollector 并接入调度执行链路，12/12 来源均可进入统一采集流程（RSS/API/WEB）。
- [x] 实现抓取任务调度（每小时）
- [x] 完成原始数据入库与失败重试

## Phase 3：处理流水线（第 7-10 天）

- [x] 文本清洗与规范化
  - 进展：已在入库链路接入 text_normalizer，并补充单元测试（tests/test_text_normalizer.py）。
- [x] 去重策略（URL + SimHash + 标题相似度）
  - 进展：已在 ingest 调度接入 `Deduplicator`（URL 规范化 + 标题归一化 + SimHash 汉明距离阈值），并补充单测 `tests/test_dedup.py`。
- [x] 标签分类（规则 + LLM）
  - 进展：已新增规则分类器 `classifier.py`（LLM/agent/infra/research/product/policy/general），并在 ingest 入库阶段落库 `articles.tags`（JSON 文本），补充单测 `tests/test_classifier.py`。
- [x] 摘要生成（失败降级与缓存）
  - 进展：已新增 `summarizer.py`（首句提炼 + 异常降级 + LRU 缓存），并在 ingest 入库链路写入 `articles.summary`，补充单测 `tests/test_summarizer.py`。

## Phase 4：API 与前端（第 11-15 天）

- [x] API：资讯列表、详情、搜索、筛选
  - 进展：已支持列表/详情、关键词搜索、来源过滤、标签过滤、发布时间区间过滤（`published_from` / `published_to`），并补齐组合筛选与统一排序回归用例。
- [x] Next.js：资讯流、详情页、标签页
  - 进展：`frontend/app/page.js`（资讯流）、`frontend/app/articles/[id]/page.js`（详情页）、`frontend/app/tags/[tag]/page.js`（标签页）均已落地并接入后端 API。
- [x] 增加基础管理页（来源状态、任务状态）
  - 进展：后端已新增接口 `/api/admin/sources` 与 `/api/admin/jobs/status`；前端管理页已支持 token 持久化、401 鉴权提示、回车刷新与“手动触发采集”交互。

## Phase 5：验收与上线（第 16-21 天）

- [ ] 指标验收（成功率、重复率、摘要率、延迟）
- [ ] 压测与性能优化
- [ ] 部署与回滚预案
- [ ] 上线监控与告警

## 上线判定（必须全满足）

- [ ] 抓取成功率 >= 95%
- [ ] 摘要成功率 >= 90%
- [ ] 重复占比 <= 15%
- [ ] 检索 P95 <= 800ms
- [ ] 连续稳定运行 72 小时
