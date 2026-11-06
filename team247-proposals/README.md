# 最高 × Team247 · Three Product Explorations

一个中英双语的交互式产品提案网站：通过原创概念图片、可操作的示例、流程图与完整提案，介绍三个值得验证的产品方向。

A bilingual, interactive product proposal: original concept imagery, hands-on examples, process diagrams, and complete proposals for three directions to validate.

**[打开网站 / Open the presentation](https://zhangzhaohao994-cyber.github.io/zuigao-ai-starter-guide/team247-proposals/)**

| 方向 / Direction | 核心设想 / Concept |
| --- | --- |
| 01 · 私人 AI / Personal AI | 把喜欢的人物定制成日常助手。A personally meaningful identity for wake-ups, reminders, and notes. |
| 02 · 行业 Agent / Industry agents | 专业资料、内容生产与商务工作流。Domain knowledge, professional content, and business workflows. |
| 03 · 人生游戏 / Personal visual novels | 讲述自己的故事，生成、游玩与分享视觉小说。Tell a personal story, then create, play, and share a visual novel. |

## 阅读 / Read

- [完整中文提案 / Full Chinese proposals](docs/proposals.zh.md)
- [Full English proposals / 完整英文提案](docs/proposals.en.md)
- [参考案例与开源候选 / References and open-source shortlist](docs/references.md)
- [实现说明 / Implementation notes](docs/implementation.md)

三个方向均保留八项完整回答：产品想法、目标用户、用户需求、市场与竞品、商业模式、验证计划、执行计划和所需支持。顶部可切换中文与英文，菜单可进入每个方向。

Each direction retains eight complete sections: product idea, target users, user needs, market and competitors, business model, validation, execution, and support needed. Use the top navigation to switch languages or explore a direction.

## 演示状态 / Demo status

这是提案展示网站，里面的交互是本地概念演示。角色切换、工作流节点、剧情选择和增长情景图用于解释产品设想，不代表三款产品已经上线。

The interactions are local concept demonstrations. Persona switching, workflow steps, narrative choices, and the sharing scenario explain proposed experiences; they are not evidence that the three products have launched.

- 不连接模型，不上传故事或人物资料，不采集机构信息，也不发送外部联系消息。
- 不提供真实游戏生成、积分充值、支付或会员服务。情景图的输入是明确标注的假设。
- No live model calls, story or photo uploads, institutional data collection, or external outreach.
- No actual game generation, credit purchases, payments, or memberships. Scenario-chart inputs are labeled assumptions.

## 本地运行 / Run locally

在本目录执行以下命令，然后打开 [localhost:8747](http://localhost:8747)：

From this directory, run the command below and open [localhost:8747](http://localhost:8747):

```bash
python3 -m http.server 8747
```

无需安装依赖或构建。使用静态 HTML、CSS、SVG、图片与 JavaScript；可直接由 GitHub Pages 托管。

No dependency installation or build step is required. The site uses static HTML, CSS, SVG, images, and JavaScript and can be hosted directly on GitHub Pages.

## 文件 / Files

- `index.html` — 页面入口与导航 / page shell and navigation
- `style.css` — 响应式布局与动效 / responsive design and motion
- `app.js` — 路由、双语界面、概念交互与图表 / routing, bilingual UI, concept interactions, and charts
- `content.js` — 三个方向的完整中英文内容 / complete Chinese and English proposal content
- `assets/` — 原创概念图与图标 / original concept imagery and icon
- `docs/` — 提案、参考与实现说明 / proposals, references, and implementation notes

产品功能、渠道、定价、授权和传播效果仍需独立验证。完整提案保留了这些假设及所需支持。

Features, distribution, pricing, rights, and growth remain subject to independent validation. The full proposals preserve those assumptions and resource needs.
