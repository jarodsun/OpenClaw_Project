# TP-R1 Idle MMO 全景调研（产品与体验）

## 0. 调研范围与说明

- TaskPack-ID：`TP-R1`
- 调研对象：`https://web.idle-mmo.com/`、`https://wiki.idle-mmo.com/`
- 目标：提炼 Idle MMO 的完整产品体验框架，作为 IdleWoool_v2 设计输入。
- 说明：公开 Wiki 为目录式知识组织，部分子页信息密度有限；本稿以可验证页面结构为主，并结合挂机 MMORPG 通用范式做结构化归纳，供后续 `TP-R2` 参数深拆继续落地。

## 1. 信息架构（Information Architecture）

Idle MMO 的公开信息架构高度模块化，可按“上手-成长-战斗-世界-经济-社交”六层组织：

1. 上手层：Getting Started（引导入门）
2. 角色层：Character（Classes / Stats / Effects / Daily Reward / Membership）
3. 战斗层：Combat（Battling / Hunting / Dungeons / World Bosses）
4. 世界层：Lore（世界观与 NPC 叙事）
5. 经济层：Economy & Trading（Market）
6. 社交层：Guild（Challenges / Conquest / Raids / Seasons / Guild Hall / Armoury）

结论：该 IA 的核心不是“功能堆叠”，而是围绕玩家长期目标（角色成长）进行的能力分层。

## 2. 核心循环（Core Loop）

从公开描述可还原出一个挂机 MMORPG 的最小闭环：

1. 角色配置（职业、属性、效果）
2. 进入战斗活动（Battling/Hunting/Dungeon/Boss）
3. 获取收益（经验、材料、装备、特殊产物如 pet egg）
4. 回到养成与经济层（强化、交易、配装）
5. 通过公会与赛季目标获得二次驱动
6. 重返更高难度活动

核心特征：
- 强“可离线推进”属性，降低持续在线负担。
- 活动类型分层，提供不同风险-收益曲线。

## 3. 成长节奏（Progression Pacing）

已识别成长轴：

- 垂直成长：等级/属性/职业能力。
- 横向成长：玩法位移（普通战斗→地牢→世界 Boss→公会内容）。
- 福利成长：Daily Reward（签到/连击奖励）形成稳定回流。
- 付费成长：Membership 提供额外权益与长期体验优化。

节奏判断：
- 早期以“快速反馈 + 新系统解锁”为主。
- 中后期转向“效率优化 + 社交协作 + 赛季竞争”。

## 4. 留存机制（Retention Mechanics）

可明确识别的留存抓手：

1. 日常回流：Daily Rewards 与日常挑战。
2. 周期目标：Guild Seasons、Conquest 领地争夺。
3. 协作门槛：World Boss、Raids 需多人参与。
4. 稀缺驱动：独特掉落（例如 pet egg）与高价值物品。

留存逻辑：
- 低压力签到回流（短周期）+ 公会赛季目标（中周期）+ 高价值稀缺追求（长周期）。

## 5. 经济与交易（Economy & Trading）

公开信息显示其经济中枢为玩家市场（Market），具备典型玩家驱动经济特征：

- 供给侧：战斗与活动产出道具。
- 需求侧：成长与构筑消耗。
- 流通层：市场买卖连接 PVE 与养成效率。

对 IdleWoool_v2 的启示：
- 经济系统必须先定义“可交易资产边界”，再定义“价格形成机制”。
- 若后续加入税率/手续费，应优先服务“抑制操纵与通胀”而非单纯回收货币。

## 6. 社交结构（Social Structure）

Guild 模块显示其社交设计并非轻聊天，而是“组织化协作系统”：

- 内部建设：Guild Hall、Armoury。
- 任务协作：Challenges、Raids。
- 外部竞争：Conquest、Seasons。

结论：
- 社交并入主进程，而非旁支玩法。
- 公会是长期留存与中后期目标承载体。

## 7. Web 端交互特质（Web Interaction Traits）

从 Web 入口与 Wiki 组织可见的产品工程特质：

- 跨端一致：Web、iOS、Android 并存，账号体系统一。
- 低门槛访问：浏览器即可进入，减少安装阻力。
- 文档驱动学习：Wiki 采用“能力域目录化”方式，降低复杂系统认知成本。
- 活动可视化入口：将战斗、公会、经济等核心域做明确入口分层，利于挂机游戏的短时操作。

## 8. 可迁移设计原则（Transferable Principles）

面向 IdleWoool_v2 的可迁移原则：

1. **主循环必须可离线推进**：保证“忙时不断档，闲时可冲刺”。
2. **系统按能力域分层**：成长、战斗、经济、社交清晰解耦但数据互联。
3. **短中长目标并存**：日常回流、周/赛季目标、长期稀缺追求同时存在。
4. **社交要进入收益主链路**：公会协作应影响效率与资源，不做纯聊天壳。
5. **市场经济先定边界**：先定义可交易物，再定义手续费/税与反操纵规则。
6. **文档即产品的一部分**：复杂系统需可导航、可检索、可解释的知识结构。
7. **入口低摩擦、决策高价值**：操作步骤短，但每次选择都影响中长期效率。
8. **内容扩展遵循模块化**：未来活动/赛季应可插拔，不破坏基础循环。

## 9. 对后续任务包的输入约束（给 TP-R2）

`TP-R2` 深拆时需补齐并量化：

- 各战斗活动的输入-规则-输出矩阵
- 成长速率与资源产消速度（单位时间）
- 市场交易的价格波动与异常行为边界
- 公会玩法的协作门槛与奖励分配机制

---

## 附：本次使用来源

- `https://web.idle-mmo.com/`
- `https://wiki.idle-mmo.com/`
- `https://wiki.idle-mmo.com/getting-started/`
- `https://wiki.idle-mmo.com/character/`
- `https://wiki.idle-mmo.com/combat/`
- `https://wiki.idle-mmo.com/economy-and-trading/`
- `https://wiki.idle-mmo.com/guilds/`
