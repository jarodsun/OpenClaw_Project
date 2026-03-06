# Keynote Studio
## Reveal.js + Dracula 示例

单文件 HTML 演示稿（由 `source.md` 生成）

---

## 目标

- 用 Web 前端技术生成演示稿
- 每个 Keynote 独立目录管理
- 输出单个 HTML 文件

---

## 结构示例

1. 封面页
2. 目录页
3. 内容页
4. 总结页

---

## 代码块示例

```js
const deck = {
  engine: 'reveal.js',
  theme: 'dracula',
  output: 'single-html'
};

console.log('Keynote Studio demo ready');
```

---

## 下一步

- 扩展模板系统
- 增加品牌化样式
- 支持批量生成
