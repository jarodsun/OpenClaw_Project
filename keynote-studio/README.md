# keynote-studio

专门用于“批量/定制生成 Keynote 演示文稿”的项目。

## 目标

- 根据不同场景快速生成 Keynote（产品方案、技术分享、复盘汇报、路演等）
- 使用 Markdown 维护每个演示稿的文本内容
- 使用 Reveal.js 生成单个 HTML 文件

## 目录结构（每个 Keynote 独立文件夹）

- `decks/<deck-name>/source.md`：该演示稿的 Markdown 文本稿
- `decks/<deck-name>/assets/`：该演示稿私有资源（图片等）
- `decks/<deck-name>/output/index.html`：该演示稿输出 HTML
- `scripts/render_reveal.sh`：渲染脚本（`source.md` -> `output/index.html`）

## 快速开始

1. 新建一个演示目录（示例）
   - `mkdir -p decks/my-talk/{assets,output}`
   - `cp decks/demo-reveal-dracula/source.md decks/my-talk/source.md`
2. 生成 HTML
   - `./scripts/render_reveal.sh my-talk`
3. 打开结果
   - `open decks/my-talk/output/index.html`

## 当前示例

- `decks/demo-reveal-dracula/source.md`
- `decks/demo-reveal-dracula/output/index.html`

## 后续计划

- [ ] 支持多主题模板（不仅 dracula）
- [ ] 支持从 JSON 输入生成
- [ ] 支持导出 PDF / PPTX
