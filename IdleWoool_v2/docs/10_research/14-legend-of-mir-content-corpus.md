# TP-R4 传奇世界内容语料库（命名与语义）

## 0. 任务定义

- TaskPack-ID：`TP-R4`
- 输入：
  - `docs/10_research/13-legend-of-mir-full-spectrum-analysis.md`
  - `/Users/jarod-macmini/SeaFile/Seafile/GameDesign/02_IdleWoool/woool_data/*`（只读）
- 输出：建立可复用语料清单，覆盖“职业/技能/怪物/道具/地图区名/NPC阵营/剧情意象/术语词典”8类。

> 语料定位：本文件不是玩法设计稿，而是后续 `TP-R5` 与 `TP-D* / TP-S*` 的命名与语义底座。

---

## 1. 职业语料（Class Corpus）

### 1.1 核心职业
- 战士（近战、承伤、爆发）
- 法师（远程、范围、法术压制）
- 道士（召唤、持续、辅助）

### 1.2 职业语义标签
- 战士：`破阵`、`硬刚`、`斩杀`、`近身压制`
- 法师：`元素`、`群攻`、`控场`、`法力管理`
- 道士：`毒符`、`召唤`、`续航`、`牵制`

### 1.3 设计约束
- 三职业必须保留“功能非对称”，禁止纯数值皮肤化。
- 文案命名优先使用“动词 + 兵器/元素/符咒”结构，保持传奇风格。

---

## 2. 技能语料（Skill Corpus）

### 2.1 技能命名样本（来自 `skill_data.csv` / `magic.csv`）
- 小火球
- 治疗术
- 初级剑法
- 精神战法
- 火炎刀

### 2.2 技能命名模式
- 战士：`<程度词><武技名>`（如 初级剑法）
- 法师：`<元素/火焰><弹/刀/墙>`（如 小火球、火炎刀）
- 道士：`<状态/召唤/符术><术/咒/符>`（如 治疗术）

### 2.3 技能语义字段（供后续模板复用）
- `skill_name`
- `class`
- `effect_type`
- `resource_cost`
- `min_power` / `max_power`
- `unlock_level`
- `pre_skill`
- `cooldown`

---

## 3. 怪物语料（Monster Corpus）

### 3.1 怪物命名样本（来自 `monster_data_basic.csv` / `monster.csv`）
- 鹿
- 毒蜘蛛
- 卫士
- 癞蛤蟆

### 3.2 怪物语义标签
- 生态类：`野兽`、`毒系`、`亡灵`、`守卫`
- 强度类：`普通`、`精英`、`Boss`
- 行为类：`近战`、`远程`、`持续效果`、`反隐身`

### 3.3 怪物数据字段（后续系统设计可直接引用）
- `monster_name`
- `level`
- `undead`
- `anti_stealth`
- `hp` / `attack` / `defense`
- `hit` / `dodge`
- `move_speed` / `attack_speed`
- `boss_level`

---

## 4. 道具语料（Item Corpus）

### 4.1 道具命名样本（来自 `stditems.csv` / `item_data_basic.csv`）
- 金创药(小量)
- 魔法药(小量)
- 粗布衣(男)
- 粗布衣(女)

### 4.2 道具类别样本（来自 `item_data_categories.csv`）
- 药品
- 技能卷轴
- 技能书
- 武器（单手/双手）
- 衣服（男/女）
- 盾牌
- 头盔/项链/戒指/手镯
- 毒药、符

### 4.3 道具语义标签
- 功能：`恢复`、`位移`、`增益`、`交易`
- 部位：`武器`、`防具`、`饰品`
- 稀有度：`普通`、`强化`、`特殊`
- 机制：`耐久`、`佩戴等级`、`叠加上限`

---

## 5. 地图区名语料（Map/Region Corpus）

> 说明：本地 `woool_data` 未提供完整地图命名表，本节采用“传奇世界常见区域语义 + 可复用命名模板”方式沉淀，后续在拿到高可信地图清单后可替换。

### 5.1 区域语义模板
- 新手区：`村`、`郊外`、`平原`
- 资源区：`矿洞`、`洞窟`、`荒地`
- 挑战区：`神殿`、`魔宫`、`禁地`
- 世界事件区：`城`、`要塞`、`王城`

### 5.2 区域命名结构
- `<地貌词> + <危险词>`（例：荒原禁地）
- `<阵营词> + <据点词>`（例：修罗要塞）
- `<历史词> + <遗迹词>`（例：封魔遗迹）

### 5.3 设计约束
- 命名应可被玩家一眼识别风险等级。
- 区域命名需兼容后续“章节制世界事件”。

---

## 6. NPC 阵营语料（Faction Corpus）

### 6.1 阵营骨架（用于 v2 设计）
- 人族城邦阵营（秩序、贸易、防务）
- 修罗/魔族阵营（侵蚀、灾变、首领驱动）
- 中立/游离阵营（商旅、隐修、情报）

### 6.2 阵营语义标签
- 立场：`守序`、`混沌`、`中立`
- 关系：`敌对`、`可交易`、`可结盟`
- 功能：`任务发布`、`资源兑换`、`事件触发`

### 6.3 NPC 命名模板
- `<身份> + <称号>`（例：城防统领）
- `<职业> + <地名后缀>`（例：矿区商人）
- `<阵营词> + <职位>`（例：修罗祭司）

---

## 7. 剧情意象语料（Narrative Imagery Corpus）

### 7.1 核心意象词
- 封魔
- 复苏
- 灾变
- 苦修
- 争城
- 守土
- 打宝
- 命运

### 7.2 叙事句式模板
- `<危机> 再临，<势力> 必须在 <时限> 内完成 <目标>`
- `<角色/行会> 为争夺 <资源/据点>，触发 <冲突事件>`
- `<古老遗迹> 开启，玩家需在 <风险条件> 下获取 <核心掉落>`

### 7.3 使用原则
- 剧情文案必须服务玩法目标（升级、掉落、社交冲突）。
- 避免纯背景堆叠，优先“事件驱动叙事”。

---

## 8. 术语词典（Glossary Corpus）

### 8.1 系统术语
- 挂机收益
- 离线收益
- 挂机效率
- 风险收益比
- 掉落池
- 保底机制
- 构筑（Build）

### 8.2 传奇语境术语
- 打宝
- 爆装
- 行会
- 攻城
- Boss
- 神油
- 卷轴
- 道符

### 8.3 术语规范
- 一个术语只保留一个主定义，避免跨文档歧义。
- 术语中英混用时，首次出现采用“中文（英文）”格式。

---

## 9. 复用格式（供 TP-R5 / TP-D* / TP-S* 调用）

推荐后续文档统一使用以下语料引用结构：

```text
[语料类型] 技能语料
[名称] 小火球
[语义标签] 法师 / 元素 / 远程
[规则锚点] skill_data.csv: effect_type=1
[设计用途] 早期法师清怪主技能命名参考
```

---

## 10. 验收对照（TP-R4）

- 职业：已完成（第 1 节）
- 技能：已完成（第 2 节）
- 怪物：已完成（第 3 节）
- 道具：已完成（第 4 节）
- 地图区名：已完成（第 5 节）
- NPC阵营：已完成（第 6 节）
- 剧情意象：已完成（第 7 节）
- 术语词典：已完成（第 8 节）

结论：`TP-R4` 验收通过，可作为 `TP-R5` 双源融合映射的直接输入。

## 11. 本轮来源索引

- `/Users/jarod-macmini/SeaFile/Seafile/GameDesign/02_IdleWoool/woool_data/skill_data.csv`
- `/Users/jarod-macmini/SeaFile/Seafile/GameDesign/02_IdleWoool/woool_data/magic.csv`
- `/Users/jarod-macmini/SeaFile/Seafile/GameDesign/02_IdleWoool/woool_data/monster_data_basic.csv`
- `/Users/jarod-macmini/SeaFile/Seafile/GameDesign/02_IdleWoool/woool_data/monster.csv`
- `/Users/jarod-macmini/SeaFile/Seafile/GameDesign/02_IdleWoool/woool_data/item_data_basic.csv`
- `/Users/jarod-macmini/SeaFile/Seafile/GameDesign/02_IdleWoool/woool_data/stditems.csv`
- `/Users/jarod-macmini/SeaFile/Seafile/GameDesign/02_IdleWoool/woool_data/item_data_categories.csv`
- `docs/10_research/13-legend-of-mir-full-spectrum-analysis.md`
