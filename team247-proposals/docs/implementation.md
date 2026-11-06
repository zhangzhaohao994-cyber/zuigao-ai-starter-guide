# 实现说明 / Implementation Notes

## 网站与内容 / Site and content

本项目是用于阅读和讨论的静态产品提案，不是三个拟议产品的生产系统。首页提供三个方向入口，每个方向包含概念图、互动示例、机制与验证图表，以及八项完整提案回答。中文默认，英文覆盖页面内容、正文和交互文字。

This is a static presentation for review and discussion, not the production implementation of the three proposed products. The overview links to three directions, each combining concept imagery, interactive examples, mechanism or validation diagrams, and eight complete proposal answers. Chinese is the default; English covers the interface, full proposal text, and interactions.

`content.js` separates the full bilingual proposal from presentation logic. It defines `window.PROPOSALS` with three IDs—`persona`, `industry`, and `story`—each containing eight sections, bilingual leads, and matching paragraph arrays. The corresponding documents are [Chinese](proposals.zh.md) and [English](proposals.en.md).

## 原创静态实现 / Original static implementation

页面使用原生 HTML、CSS、JavaScript 和 SVG，没有框架安装、编译或运行时开源库依赖。布局、图表、图标与概念交互为本网站编写。CSS 控制视觉层级、响应式版式及适度过渡，JavaScript 负责语言切换、页面导航、详情阅读和示例状态，SVG 用于精确的视觉与图形表达。

The implementation uses native HTML, CSS, JavaScript, and SVG with no framework installation, compilation, or runtime open-source library dependency. Layout, charts, iconography, and concept interactions were authored for this site. CSS handles hierarchy, responsive composition, and restrained transitions; JavaScript handles language, navigation, detailed reading, and demo state; SVG provides precise visual elements.

语言偏好保存在浏览器本地。交互示例不连接后端服务，不需要账户、密钥或真实客户数据。

The browser stores the language preference locally. Concept interactions do not connect to a backend and require no account, API key, or real customer data.

## 参考的使用方式 / How references inform the design

参考研究包括 Sequoia 的商业计划表达、Linear 和 Pitch 的分层产品介绍、Character.AI 与 Delphi 的人物入口、Dify 与 Fin 的知识及任务工作流、Monogatari 与 Inworld 的互动叙事。完整来源与具体观察见 [参考文档](references.md)。

These references inform information order, clarity, and interaction patterns: Sequoia for business-plan structure; Linear and Pitch for layered product storytelling; Character.AI and Delphi for identity-first entry points; Dify and Fin for knowledge-to-workflow explanation; Monogatari and Inworld for interactive narrative. See the [reference document](references.md) for links and observations.

本站没有复制参考网站的源码、品牌、完整界面或客户资产，也不暗示与参考公司有商业合作。

The site does not copy reference-site source code, branding, complete interfaces, or customer assets, and implies no commercial partnership with those companies.

## 开源候选与实际依赖 / Open-source shortlist versus dependencies

| 候选 / Candidate | 用途 / Potential use | 本站状态 / Status here |
| --- | --- | --- |
| reveal.js · MIT | 未来演讲或幻灯片模式 / future presentation mode | 未使用运行时 / not used at runtime |
| Motion · MIT | 更复杂的状态动画 / more complex animation | 未使用，当前为原生 CSS/JS / not used; native CSS/JS instead |
| Mermaid · MIT | 文档中的流程图 / document diagrams | 未使用运行时 / not used at runtime |
| Monogatari · MIT | 后续视觉小说产品原型 / future visual-novel prototype | 未集成；当前小型剧情示例为原创 JS / not integrated; the small story demo uses original JS |
| Dify · modified Apache 2.0 with additional conditions | 后续知识和 Agent 工作流评估 / future knowledge and Agent workflow evaluation | 未部署、未集成 / not deployed or integrated |

这是选型清单，不是软件依赖清单。Dify 的许可包含额外条件，不能将其视作无条件可改标的多租户 SaaS 模板；实际集成前需按使用方式核对对应版本。MIT 项目如果未来复制或打包代码，应保留其版权与许可。

This is an evaluation shortlist, not a dependency list. Dify's license has additional conditions and should not be treated as unrestricted, white-label multi-tenant SaaS boilerplate. Review the chosen version and use case before integration. Preserve copyright and license notices if code from MIT projects is copied or bundled later.

## 图片与概念示例 / Imagery and concept examples

三张主视觉通过图像生成工具制作，表现虚构角色和产品情境，不是现有产品截图、真实用户、真实客户或人物代言。生成说明保存在 [image-prompts.md](../assets/image-prompts.md)。实际图片使用及其授权范围与未来真人或商业 IP 产品方案应分别处理。

The three main visuals were produced with an image-generation tool and depict fictional characters and product scenarios. They are not screenshots of existing products, real users, customers, or endorsements. Generation notes are in [image-prompts.md](../assets/image-prompts.md). These illustrative assets are separate from any future permissions required for real people or commercial IP in a product.

私人 AI 示例切换原创角色、语气和生活情境；行业 Agent 示例点亮资料、检索、生成、审核、交付等步骤；视觉小说示例提供预先编写的虚构选择与结果。它们只展示可讨论的体验。

The personal-AI demo changes original personas, tone, and everyday scenarios. The industry-Agent demo highlights source, retrieval, drafting, review, and delivery steps. The visual-novel demo uses prewritten fictional choices and outcomes. They illustrate experiences to discuss.

## 数据与图表边界 / Data and chart boundaries

页面没有模型调用、语音转写、故事或照片上传、企业信息采集、邮件发送、微信添加、实际积分、充值或支付。按钮变化和剧情结果在浏览器内完成。

There are no model calls, speech transcription, story or photo uploads, business-data collection, email sending, WeChat requests, real credits, purchases, or payments. UI changes and story outcomes occur in the browser.

流程图表示拟议机制，验证图表示需要评估的指标。分享情景工具使用用户可调整的假设，不能作为已有用户、收入、转化率或增长预测引用。

Process diagrams describe proposed mechanisms; validation diagrams show what must be tested. The sharing scenario uses adjustable assumptions and must not be cited as observed users, revenue, conversion, or a growth forecast.

## 运行 / Running

在项目目录执行 `python3 -m http.server 8747`。GitHub Pages 直接提供静态文件，所有站内资源使用相对路径，以支持 `team247-proposals/` 子目录部署。

Run `python3 -m http.server 8747` in the project directory. GitHub Pages serves the static files directly. Internal assets use relative paths to support deployment under `team247-proposals/`.
