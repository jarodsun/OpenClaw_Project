# keynote-studio

专门用于“批量/定制生成 Keynote 演示文稿”的项目。

## 目标

- 根据不同场景快速生成 Keynote（产品方案、技术分享、复盘汇报、路演等）
- 支持模板化内容输入（Markdown / JSON）
- 支持后续接入自动化（AppleScript / Keynote Automation）

## 目录结构

- `docs/`：需求、流程、规范
- `templates/`：Keynote 模板定义（结构、配色、风格）
- `assets/`：图片、图标、字体等资源
- `scripts/`：生成与导出脚本
- `examples/`：示例输入与输出说明
- `output/`：生成结果（建议加入 .gitignore）

## 快速开始

1. 准备内容：将大纲写入 `examples/demo-outline.md`
2. 选择模板：在 `templates/` 选择或新增模板
3. 生成文稿：执行 `scripts/generate_keynote.sh`（当前为占位）

## 后续计划

- [ ] 定义统一输入规范（`title/sections/slides/notes`）
- [ ] 实现 Markdown -> Keynote 自动化流程
- [ ] 支持多主题模板与品牌风格
- [ ] 支持导出 PDF / PPTX
