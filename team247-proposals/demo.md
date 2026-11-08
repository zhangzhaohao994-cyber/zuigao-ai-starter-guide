# Team247 · Three Interactive App Demos

**最高 × Team247 — 初代可操作原型 / First-generation interactive prototypes**  
2026-11-09

[打开三机演示页 / Open the demos](https://zhangzhaohao994-cyber.github.io/zuigao-ai-starter-guide/team247-proposals/demo.html) · [完整提案 / Full proposals](https://zhangzhaohao994-cyber.github.io/zuigao-ai-starter-guide/team247-proposals/b.html)

一个网页，按顺序呈现三部可操作手机。桌面左侧解释产品，右侧直接操作；手机端上下滑动，依次体验个人助理、行业 Agent 和人生游戏。顶部支持中文 / English 切换。

## 01 · 个人助理 / Personal AI

重点是「自己喜欢的人设进入日常生活」，而不只是通用聊天框。

- 选择原创角色或上传本机图片，编辑名称、语气与口头禅。
- 保存备忘、搜索与删除记录。
- 创建定时提醒、切换闹钟状态、进行短时试响。
- 使用设备语音朗读问候，不使用真人克隆声音。
- 人设与文字记录保存在当前浏览器。图片的保存范围以界面提示为准。

**怎么试：**先在人设页更换角色，再记录一条备忘，最后在提醒页点击试响并保持页面打开。

**边界：**浏览器不是系统闹钟。页面关闭、设备休眠或后台限流时不能保证准时提示。生产版需要原生通知或受支持的推送机制，以及授权角色、语音和隐私管理。

## 02 · 行业 Agent / Industry Agent

主要面向机构运营、咨询与销售。演示医美工作台，也展示向其他行业定制的方向。

- 选择行业与资料，输入主题、受众、渠道，生成本地模板草稿。
- 查看与维护产品资料、来源、日期和待核验项。
- 编辑、复制、导出文案、短视频脚本和图片简报。
- 管理虚构示例机构，或录入自己获授权使用的商业联系信息。
- 筛选线索、改变跟进阶段、生成联系草稿和导出 CSV。

**怎么试：**在资料页添加一条业务资料，再回工作台引用它制作草稿；在机构线索页推进一条记录的跟进阶段。

**边界：**示例资料与模板不构成专业医学知识库。没有模型调用、医疗决策、真实客户检索或自动外发消息。生产版需要有来源与版本的行业知识库、检索增强生成、专业审核、权限和可审计的业务集成。不会通过本演示抓取私人手机号码或批量添加微信。

## 03 · 人生游戏 / Life, Playable

从一段经历进入可选择的视觉小说，而不是停在一张生成结果图片上。

- 输入故事、聊天或文章片段，设置主要角色与题材。
- 可选择本机照片；不上传到服务器。
- 用本地剧情模板生成包含用户素材的短篇，进行分支选择，体验多个结局。
- 支持书架、继续游玩与重玩。
- 首部免费；后续制作使用演示积分，每部首次通关奖励一次。
- 可复制演示页链接；可下载包含自己故事的独立 HTML 游戏。

**怎么试：**先用示例素材快速制作一部游戏，走到结局；再输入自己的文字，比较生成的序章和角色。下载前注意文件会包含你的故事。

**边界：**分支是虚构创作，不推测真实人物想法、不预测现实结局。当前没有 AI 扩写、人物立绘生成、联网分享统计、充值或真实会员。复制链接分享的是公开演示页，不会自动分享私人故事。积分仅用于体验产品逻辑，不是实际经济权益。

## Architecture / 实现

- **Buildless, static HTML.** 原生 HTML / CSS / JavaScript，无运行时框架、无 CDN、无模型 API，因此当前 Demo 不消耗模型 token。
- **One entry point.** `demo.html` 内含三个模块的脚本与样式，复用同目录下 `assets/` 的 WebP 图片。复制整页时需保留这些图片的相对路径。
- **Local state.** 按模块存储在浏览器 `localStorage`；图片仅在本地处理。无账号、无后端数据库、无行为追踪。
- **Small, independent modules.** `Team247Assistant`、`Team247Industry`、`Team247Game` 分别提供 `mount(root, lang)`、`setLanguage(lang)`、`destroy()` 接口，后续可以单独迭代或接入服务。
- **Interaction first.** 表单校验、明确的空状态、可见操作反馈、键盘焦点和 `prefers-reduced-motion` 降低动态选项。
- **Generated vs. real.** 本地操作与模板结果可实际使用；AI、云同步、后台通知、付费和外部数据仍待接入。

## Browser references / 浏览器实现依据

- [MDN: localStorage](https://developer.mozilla.org/en-US/docs/Web/API/Window/localStorage) — 本机文字记录与异常处理。
- [MDN: Page Visibility API](https://developer.mozilla.org/en-US/docs/Web/API/Page_Visibility_API) — 后台定时器可能被限流，因此不把本网页宣称为可靠的系统闹钟。
- [MDN: SpeechSynthesis](https://developer.mozilla.org/en-US/docs/Web/API/SpeechSynthesis) — 设备语音朗读，具体声音与支持情况取决于浏览器。
- [MDN: Web Audio best practices](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API/Best_practices) — 由用户操作触发音频，失败时保留可见提示。

## English overview

Three interactive, phone-shaped prototypes on a single responsive page. Try a personalized everyday assistant, an industry workspace, and a branching visual novel made from your own story. A language button switches the UI between Chinese and English.

The current version implements lightweight actions locally: reminders while the page is running, notes, persona customization, source-aware template drafting, lead stages, story choices, a library, and downloads. It does **not** call a language model, send outreach, synchronize data to a server, process payments, or guarantee background alarms. Images and demonstration content are illustrative. Production AI and service integrations are a next step, not a claimed capability of this release.

## Verification / 本次验证

2026-11-09：

- 三个脚本与最终内联 HTML 中的脚本通过语法检查。
- 浏览器验证：助理人设保存、备忘保存/搜索/安全显示、刷新恢复、一次提醒创建、10 秒到时可见提醒。
- 浏览器验证：行业三类内容、线索阶段修改/筛选、联系草稿、表单填到一半切语言仍保留。
- 浏览器验证：故事素材输入、生成可玩短篇、五次选择、两条不同结局路径、奖励去重、第二部制作扣除积分、英文游玩、独立 HTML 下载。
- 下载的游戏脚本通过语法检查，不依赖外部网络；模块测试覆盖全部三类结局和输入脚本注入防护。
- 320px / 390px 窄屏下，中英文页面与三个 App 屏幕均无横向溢出；本机浏览器检查，不代表实体手机的性能实测。
- 浏览器无音频回听，因此仅确认提醒触发与文字反馈；系统语音和提示音的实际播放仍取决于浏览器及设备设置。
