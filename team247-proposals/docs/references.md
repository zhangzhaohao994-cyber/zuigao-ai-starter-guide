# 参考案例与开源选型 / References & Open-source Options

研究日期：2026-11-07。用于最高 × Team247 三个产品提案的网站表达、交互和后续原型选型。以下官方页面与仓库已读取，另在浏览器查看了 Linear 首页的标题层级、产品图与留白。其他参考主要依据官方页面内容和示例研究。具体颜色、排版与插图为本项目原创设计选择。

## 1. 整体提案结构：Sequoia × Linear × Pitch

| 官方案例 | 已核对的表达方式 | 本项目怎样使用 |
| --- | --- | --- |
| [Sequoia：Writing a Business Plan](https://sequoiacap.com/article/writing-a-business-plan) | 先用一句话说明公司目的，再讨论问题、解决方案、市场、竞争、商业模式、团队和愿景；没有财务就不强补财务 | 每个项目先用一句具体的体验说清楚，再展示 Demo、八项回答与验证计划。保留 Ting 的八项要求，不将空白阶段包装成已有业绩 |
| [Linear](https://linear.app/) | 首页先给单句价值主张，随后用产品界面和按工作过程组织的章节解释能力 | 网站用“清楚的标题＋可操作的演示＋深入阅读”三层结构。统一网格、留白、细线和编号；三项目用不同强调色，不做三套互不相干的品牌 |
| [Pitch](https://pitch.com/) / [模板入口](https://pitch.com/templates) | 产品首页使用简洁主张、编辑中的产品图和 Create / Collaborate / Deliver 分段；模板以快速建立专业演示为目标 | 提案用大标题、关键结论、图表与阅读详情分层。采用可滚动、可回到概览的网页，不把所有内容挤成小字幻灯片 |

**建议的网站阅读路径：** 三方向概览 → 点击进入某个产品 → 一句话理解 → 看概念演示 → 看流程和商业逻辑图 → 阅读八项完整回答 → 查看验证假设与参考。

这是一份产品提案，不是已上线产品的销售站。演示需标“概念演示 / Concept demo”，图表须区分机制示意、待验证假设和真实数据。不要编造收入曲线、转化率、用户数和客户 logo。

## 2. 方向一：私人 AI — 身份和体验，而非功能清单

### 对标 A：Character.AI

- [Character Calls & Voice 官方说明](https://support.character.ai/hc/en-us/articles/23957274129691-Character-Calls-Voice-FAQ)
- 其官方说明包含创建声音、把声音与角色关联、语音对话，以及声音的可见范围。这证明“可定制角色/声音”已存在，不能作为无人竞争的能力。
- 适合借鉴：用角色头像、声音和具体互动场景让用户先理解体验。本站可提供原创角色切换器；用户切换后，手机预览中的名字、语气、口头禅与叫醒文案一起变化。
- 本提案差异仍须验证：身份一致性如何进入起床、提醒和备忘，而不只存在于聊天中。

### 对标 B：Delphi

- [Delphi](https://www.delphi.co/)（原 delphi.ai 当前跳转此地址）
- 页面以真实人物身份和具体可提问的情境组织入口，突出用户想向谁询问，而非先解释模型技术。
- 适合借鉴：将“你希望谁陪你”作为体验入口，用三种原创 persona 对照，而非用抽象圆球代表 AI。情绪与任务的关系用“身份设定 → 日常触点 → 持续使用”图解释。
- 不应搬用其真实人物头像、推荐语或暗示同样获得人物授权。

## 3. 方向二：行业 Agent — 知识、工作流与交付

### 对标 A：Dify

- [Dify 官方网站](https://dify.ai/)
- 官方明确区分 Workflow Studio、Knowledge Pipeline、模型/工具集成及云端或自托管部署。
- 适合借鉴：用资料卡、工作流节点、审核关口、输出预览解释专业资料怎样变成行业结果。本站概念演示可切换“内容生产 / 商务研究”，按资料 → 检索 → 生成 → 审核 → 输出逐步点亮。
- 重要边界：Dify 是编排基础设施，不能据此证明本项目已有专业医美资料或内容准确率。

### 对标 B：Fin / Intercom

- [Fin 工作流与人工交接](https://www.intercom.com/help/en/articles/10032299-use-fin-ai-agent-in-workflows)
- 官方文档将 Agent 放在明确触发、分派、交接和预览流程中，说明 Agent 能力需要接入业务操作和人员处理。
- 适合借鉴：展示一个真实形态的任务结果及人工审核节点，代替“全能 Agent”文案。商务线索仅演示机构公开商务资料与经许可的联系流程。
- 页面应同时区分“标准化医美产品”和“其他行业定制服务”，用双轨交付图解释不同收入与执行方式。

## 4. 方向三：人生视觉小说 — 先让人玩到，再解释生成

### 对标 A：Monogatari

- [官方产品与 Demo 入口](https://monogatari.io/)
- 官方提供面向浏览器的视觉小说引擎，包含多媒体、翻译、存档、动画和响应式体验。
- 适合借鉴：完整画面、角色、对白框、两个有意义的选择以及重新开始按钮。提案中只用原创虚构人物与故事，并标注“示例剧情”；不要让用户以为已接入 AI 生成或真实付费系统。
- 后续产品原型可以评估直接使用其运行时，而不是重新实现整个视觉小说播放器。

### 对标 B：Inworld Games & Media

- [Inworld Games & Media](https://inworld.ai/gaming-media)
- 官方以游戏与媒体体验、角色和语音示例解释能力，而不是只展示 API 名称。
- 适合借鉴：先展示最终游戏体验，再回溯输入故事、人物识别、场景生成和分支编排。声音可作为后续能力，不应因为参考站提供而添加到已承诺首版范围。
- 分享积分机制使用原创循环图：首次免费创作 → 分享 → 有效游玩 → 积分 → 再次创作；玩家转创作者作为第二支路。没有真实数据时只表达机制，不画虚假增长曲线。

## 5. 可以用得上的开源项目

| 项目与官方链接 | 已核对许可 | 能解决什么 | 本次建议 |
| --- | --- | --- | --- |
| [reveal.js](https://github.com/hakimel/reveal.js) / [Demo](https://revealjs.com/) | MIT；仓库 LICENSE | HTML 演示、章节导航、动画、演讲者视图和 PDF 导出 | 如果以后需要会议演讲模式，可由相同内容生成。当前需自由浏览三方向，普通网页导航更直接，不必强制幻灯片化 |
| [Motion](https://github.com/motiondivision/motion) | MIT；仓库 LICENSE | JS / React 动画、交互过渡 | 可用于更复杂的场景动画。若仅卡片进入、菜单和步骤点亮，原生 CSS 足够，减少依赖 |
| [Mermaid](https://github.com/mermaid-js/mermaid) / [许可证原文](https://raw.githubusercontent.com/mermaid-js/mermaid/develop/LICENSE) | MIT | 文本生成流程、关系和时序图 | 文档版本可直接使用；网页可用原创 SVG 获得更精确的排版和交互。不要将未使用的库列为实际依赖 |
| [Monogatari](https://github.com/Monogatari/Monogatari) | MIT；官方站与仓库一致 | 浏览器视觉小说、多语言与多媒体 | 方向三后续原型的直接候选；提案站的小型选择 Demo 可用轻量原创 JS，无需立即集成完整引擎 |
| [Dify](https://github.com/langgenius/dify) / [许可证原文](https://raw.githubusercontent.com/langgenius/dify/main/LICENSE) | 修改版 Apache 2.0，含额外条件，不是纯 Apache 2.0 或 MIT | 知识库和 Agent 工作流后端 | 可作为方向二后续技术评估对象。多租户服务需书面授权；使用其前端时对 logo/版权信息有约束。不能直接改标后作为自己的多租户 SaaS 发布 |

MIT 项目如实际复制或打包代码，应保留对应版权与许可文件。以上是候选，不表示本网站已安装全部项目。Dify 的限制按 2026-11-07 读取的仓库许可说明，正式集成前需重新核对具体版本及使用方式。

## 6. 本站原创 UI 执行建议

- 首页：一张具有情绪和科技质感的原创主视觉，配简短价值主张与三张方向卡，不把八项正文全部堆在首页。
- 导航：最高 × Team247 标识、语言切换、菜单按钮；菜单含三方向与参考。中文默认，英文应覆盖正文和交互提示，而非仅翻译标题。
- 每个方向：一句具体主张、案例演示、机制图、八项提案内容、验证重点与资源需求。
- 图表：私人 AI 身份到生活触点流程；行业 Agent 知识生产和双业务路径；视觉小说输入到成品路径和分享积分循环。
- 动效：进入淡显、角色切换、流程步骤高亮、视觉小说分支反馈。减少纯装饰动效，支持 reduced-motion。
- 视觉：使用原创字体层级、颜色体系、构图和图片。可以研究他人的信息顺序与交互方式，不复制网站源码、品牌标识、真实用户数据、名人图像或完整页面视觉资产。
- 产品边界：所有案例与 UI 都标明概念演示；按钮有具体可见反馈；不伪装真实数据采集、外发消息、注册、生成、充值或计费。

## English summary

The references inform structure and interaction, not copied branding or assets. Sequoia informs proposal clarity; Linear and Pitch inform layered product storytelling. Character.AI and Delphi inform persona-first presentation; Dify and Fin inform knowledge-to-workflow delivery; Monogatari and Inworld inform playable visual-novel presentation. All proposal demos remain conceptual. Useful OSS candidates are reveal.js, Motion, Mermaid and Monogatari (MIT). Dify uses a modified Apache 2.0 license with additional commercial-use conditions; it is not treated as unrestricted SaaS boilerplate.
