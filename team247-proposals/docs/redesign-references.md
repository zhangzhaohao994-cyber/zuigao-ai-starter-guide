# 两版重设计：开源动效与执行依据

核验日期：2026-11-07。范围：官方文档、可运行 Demo、固定版本分发文件和许可证；本文件不代表浏览器性能测试已经完成。以下性能数字是本项目的设计预算，需要真机验证。

设计目标是**进入网站立即看见动态**。本次两版要改变空间组织、阅读路径和动作语言，不只是更换背景颜色。三份提案的完整八项内容、中英文切换、直接链接与手机可读性仍须保留。

交付入口固定为：**A = `a.html`，深色流体展览；B = `b.html`，酸黄动态字体工作台。实际依赖只有 Three.js 0.160.1 与 Anime.js 4.2.2**；下文其他项目是可复用候选或研究参考，不代表已经安装。已下载这两个选定版本，并确认 SHA-256 与本报告一致。

视觉核验边界：已实际打开并截图 Codrops TextCharacterAnimations，看到暗底红色巨型字排版；Anime.js 官网文档可读取，但本次浏览器截图为黑屏，因此不宣称它的完整视觉演示已通过现场验证。

## 已确定的两条路线

| 项目 | A：银紫数字展览 / Luminous Cinema | B：酸性动态工作台 / Kinetic Studio |
| --- | --- | --- |
| 第一眼 | 黑色空间里，银紫流动光带已经在缓慢变化；大标题从暗处揭示 | 酸性黄与电光蓝整屏碰撞；巨型中英文字、编号和几何标记立即进入画面 |
| 视觉主体 | 光、暗、景深、原创图像，文字保持清楚的前景层 | 文字本身、强网格、粗细变化、色块、切片与印刷式构图 |
| 内容结构 | 沿纵向滚动进入三个章节；背景色场与图像随章节转场 | 像展开三份创意档案；方向选择、标签、样本与八项回答构成工作台 |
| 主要动作 | 慢速连续流体 + 短促清晰的文字揭示 + 章节镜头转换 | 文字错位归位、遮罩揭示、编号切换、色块推移、菜单排版变形 |
| 实际引擎 | Three.js 0.160.1 + Anime.js 4.2.2 | Anime.js 4.2.2 + CSS/SVG；无需 WebGL |
| 手机逻辑 | 同一视觉主题，减少像素与层数，三个章节顺序滚动 | 重新组合为单列，巨字保持完整，方向索引可点击，内容不依赖 hover |

### A 的具体执行

1. **进站即动：**首帧先显示黑底、标题与导航；WebGL 准备好后立即出现缓慢银紫光带。避免“点击进入”和假加载倒计时。光影运行不应成为正文可见的前置条件。
2. **一个场景贯穿三章：**用一个平面和自写片元着色器实现低频噪声、层叠波纹与高光，滚动只改变少量 uniform。每章配独立原创视觉：私人 AI 的身份轮廓、行业 Agent 的工作链、人生游戏的故事入口；不能让三章都成为同一个发光球。
3. **文字节奏：**章节名与首句用逐字/逐词遮罩揭示，正文按行或段落出现。动作结束后完全静止可读。标题、正文、按钮在 DOM 中，不能全部画进 Canvas。
4. **手机预算：**建议移动端 DPR 上限 1–1.25、桌面 1.5；先不加多遍 bloom、真实折射和大面积模糊。页面隐藏或主要动效区域离开视口时暂停绘制。低性能设备可降到 30 FPS；WebGL 不可用时使用静态渐变与原始图像，正文照常工作。
5. **滚动：**原生滚动为默认，章节交替使用宽图、左右关系和全宽图表。不要把全文锁进固定高度的“电影屏幕”；长提案必须容易浏览与定位。

实际机制参考：[Three.js Lava Shader Demo](https://threejs.org/examples/webgl_shader_lava.html)、[Three.js Unreal Bloom Demo](https://threejs.org/examples/webgl_postprocessing_unreal_bloom.html)。前者参考时间驱动的材质变化，后者参考亮暗层次；示例中的纹理、模型和独立署名不自动随库的 MIT 许可证一起授权。本项目应使用原创着色器、图像和几何体。

### B 的具体执行

1. **进站即动：**大号 `THREE / DIRECTIONS` 与中文主标题按不同方向进入，数字 `01—03`、横线和色块同步对齐。整体在约 0.8–1.2 秒内稳定；用户立即能点方向和语言。
2. **全文的排版体系：**所有章节标题、提案首句、数字、图表标签都有统一的出现规则；长正文按行/段落短揭示，不能把三份长文全部拆成数千个永久动画字符。
3. **工作台的操作：**三个方向以可点击的粗体标签或档案页呈现；点击后标题位置、背景色块、示例区同步变换。每份提案仍有完整八项内容和锚点，不把阅读变成连续猜按钮。
4. **动作与产品对应：**私人 AI 演示三种可辨识人设；行业 Agent 的节点从材料到交付逐步完成；人生游戏展示“输入—生成—选择—分享”的图形流程。装饰文字动效必须让位于这些概念演示。
5. **手机预算：**正文 16px 起，按钮点击区域约 44px，巨字用 `clamp()` 并限制溢出。标题可换行，英文不硬塞中文宽度。鼠标跟随和倾斜仅在 `hover:hover` 时启用，触摸端始终提供直接按钮。

实际参考：[Anime.js splitText 官方可运行示例](https://animejs.com/documentation/text/splittext/)、[Anime.js 首页的时间线与错峰动作](https://animejs.com/)、[Codrops Text Character Animations](https://tympanus.net/Demos/TextCharacterAnimations/)。建议挑选 2–3 种动作构成系统，不把 19 种效果逐一堆进同一网站。

## 六个真实可复用项目

### 1. Three.js：A 版空间与程序化光影

- [官方仓库](https://github.com/mrdoob/three.js)；[官方示例库](https://threejs.org/examples/)；[固定版本 MIT 许可证](https://cdn.jsdelivr.net/npm/three@0.160.1/LICENSE)。
- **已核验分发文件：**[three.module.min.js · 0.160.1](https://cdn.jsdelivr.net/npm/three@0.160.1/build/three.module.min.js)，HTTP 200，670,681 bytes。
- 是可本地保存的 ESM 构建，不必引入 React、构建框架或远程模型。使用 `<script type="module">` 从本地路径 import；若加入 addons，必须使用同一版本并处理相对依赖。
- r160.1 是有意锁定的版本，不是“当前最新版”。当前官方 Demo 可能已经使用新版 API；学习效果机制后按 r160.1 API 实现，避免把最新 WebGPU/TSL 代码直接粘贴进旧版。
- 适合：单个全屏 ShaderMaterial、轻量粒子、程序化几何体。当前方案不需要完整物理流体模拟。

### 2. Anime.js：两版的主动画引擎

- [官方仓库](https://github.com/juliangarnier/anime)、[安装与直接下载说明](https://animejs.com/documentation/getting-started/installation/)、[固定版本 MIT 许可证](https://cdn.jsdelivr.net/npm/animejs@4.2.2/LICENSE.md)。
- **已核验分发文件：**[anime.umd.min.js · 4.2.2](https://cdn.jsdelivr.net/npm/animejs@4.2.2/dist/bundles/anime.umd.min.js)，HTTP 200，88,816 bytes。可保存到 `vendor/`，普通 script 加载后使用 `anime.animate`、`anime.createTimeline` 等 v4 API。
- [splitText 示例](https://animejs.com/documentation/text/splittext/)提供行、词、字符拆分与遮罩；[响应式 Scope 示例](https://animejs.com/documentation/scope/scope-parameters/mediaqueries/)展示媒体查询和减少动态效果的分支。
- 适合：标题与段落揭示、SVG 线条、菜单时间线、图表切换。已经选择它时，不需再为同样职责同时加载 Motion。

### 3. Splitting.js：极小的排版拆分备选

- [官方 Demo](https://splitting.js.org/)、[官方指南](https://splitting.js.org/guide.html)、[仓库](https://github.com/shshaw/Splitting)、[MIT 许可证](https://cdn.jsdelivr.net/npm/splitting@1.1.0/LICENSE.md)。
- **已核验：**[splitting.min.js · 1.1.0](https://cdn.jsdelivr.net/npm/splitting@1.1.0/dist/splitting.min.js)，HTTP 200，3,871 bytes；[配套 splitting.css](https://cdn.jsdelivr.net/npm/splitting@1.1.0/dist/splitting.css)，HTTP 200，1,784 bytes。
- 它负责把文本/子元素分组并附上 CSS 索引，不负责动画；适合 B 版通过 CSS 做字符错峰、斜切、波浪和格栅。Anime.js 自带拆字已经够用时可以省略它。
- 中文长句没有英文的空格分词规则；只对合适的短标题按字符处理，正文优先按段/行，字体加载或容器宽度改变后重新测量。

### 4. Lenis：A 版滚动同步的可选层

- [官方可运行站点](https://lenis.dev/)、[源码与接入文档](https://github.com/darkroomengineering/lenis)、[MIT 许可证](https://cdn.jsdelivr.net/npm/lenis@1.3.27/LICENSE)。旧官网 `lenis.darkroom.engineering` 当前跳转到 `lenis.dev`。
- **已核验：**[lenis.min.js · 1.3.27](https://cdn.jsdelivr.net/npm/lenis@1.3.27/dist/lenis.min.js)，HTTP 200，18,815 bytes；[配套 CSS](https://cdn.jsdelivr.net/npm/lenis@1.3.27/dist/lenis.css)，HTTP 200，513 bytes。
- 适合把滚动进度和 WebGL 场景更新同步；并非只要装上就能让设计高级。首次实现可不使用，避免与原生锚点、弹层、触摸滚动形成双重控制。
- 若使用，统一一条 RAF 更新链；测试键盘 PageDown、锚点定位、弹层内滚动、浏览器返回及移动端地址栏伸缩。

### 5. Motion：可替代 Anime.js 的成熟交互引擎

- [官方示例库](https://motion.dev/examples)、[JavaScript 接入与示例](https://motion.dev/docs/quick-start)、[仓库](https://github.com/motiondivision/motion)、[MIT 许可证](https://cdn.jsdelivr.net/npm/motion@14.10.1/LICENSE.md)。
- **已核验：**[motion.js · 14.10.1](https://cdn.jsdelivr.net/npm/motion@14.10.1/dist/motion.js)，HTTP 200，183,604 bytes；这是完整浏览器构建的原始体积，不是官方介绍的 mini 模块体积。
- 适合弹簧交互、滚动驱动、SVG 与 DOM 动画。当前项目已锁定 Anime.js，因此保留为替代方案，不加载两套重叠引擎。
- **许可范围要分开：**Motion 开源库为 MIT；官网同时展示 Motion+ 等产品，不能把所有收费示例、组件和网站素材都默认当作 MIT 免费资源。

### 6. Codrops TextCharacterAnimations：可运行的逐字排版研究项目

- [官方 Demo：19 种文字动画](https://tympanus.net/Demos/TextCharacterAnimations/)、[完整仓库](https://github.com/codrops/TextCharacterAnimations)、[固定提交 LICENSE](https://raw.githubusercontent.com/codrops/TextCharacterAnimations/ac0fe97a4e4f786ef5d514d7030b6eb5855da05b/LICENSE)。
- 核验提交：`ac0fe97a4e4f786ef5d514d7030b6eb5855da05b`。这是完整 HTML/CSS/JS 演示项目，不是截图模板。仓库说明本地 HTTP 服务即可运行。
- 可研究 Cursor Scramble、Telegram、Swipe、Live Captions 等动作：文字先被一个明确规则组织，再回到清楚可读的排版。B 版应取“错位—归位”和“遮罩—揭示”的规律，使用原创中文与版式重新实现。
- 仓库自身代码是 MIT，随附字体说明为 SIL OFL 1.1；但 HTML 实际加载 GSAP、ScrollTrigger、ScrollSmoother、SplitText、Flip。**不能称整套依赖均为 MIT。**GSAP 使用其独立的 [Standard No Charge License](https://gsap.com/community/standard-license/)。本项目采用 Anime.js 重写相应动作，不必再增加 GSAP。
- 固定提交的 [js/index.js CDN](https://cdn.jsdelivr.net/gh/codrops/TextCharacterAnimations@ac0fe97a4e4f786ef5d514d7030b6eb5855da05b/js/index.js)（HTTP 200，9,556 bytes）与 [css/base.css CDN](https://cdn.jsdelivr.net/gh/codrops/TextCharacterAnimations@ac0fe97a4e4f786ef5d514d7030b6eb5855da05b/css/base.css)（HTTP 200，11,091 bytes）均已实测，可用于下载研究；这不是可单独丢进本站就运行的通用插件，它依赖原项目 DOM、样式和上述运行时。

## 本地保存与校验

本轮对选定的库与对应许可证执行了真实 HTTP GET；以下 SHA-256 可用于下载后的完整性比对。字节数为未 gzip 的响应正文。

| 文件 | 字节数 | SHA-256 |
| --- | ---: | --- |
| `three@0.160.1/build/three.module.min.js` | 670681 | `3e690ac7d180b0aadf0891bea39eec643e29e2d3e75c99b18689518665f69ba6` |
| `three@0.160.1/LICENSE` | 1081 | `852e0e8699169bf9f6fdc6bda3e682d078dcbc738b5d33e74df594721bff271d` |
| `animejs@4.2.2/dist/bundles/anime.umd.min.js` | 88816 | `7c9c60d061852e9d48289b6399ee5c6c429be703339549f6b708b3e52d7aa73e` |
| `animejs@4.2.2/LICENSE.md` | 1075 | `3f3e835a9952cfc2a6ca836fb95b3257c981f24fa3ef51249055acb09931897b` |

建议本地结构为 `vendor/three.module.min.js`、`vendor/anime.umd.min.js` 和两份单独 LICENSE；保留原文件头与版权说明，在项目文档注明版本。部署不依赖 `@latest` 或访客实时请求第三方 CDN。演示站的布局、图像、人物、品牌标记和文字并不因底层代码开源就全部可复制。

## 两版共用的完成标准

- 第一次打开就能看到动态，同时标题、语言按钮和目录立刻可用；不必等待动画播放结束才能操作。
- 中英切换后销毁旧时间线与文字拆分，重新绑定新 DOM；同一视口不积累重复 RAF、观察器或字符节点。
- 屏幕阅读器仍读到完整句子；逐字包装不造成逐字重复播报。`prefers-reduced-motion` 下移除连续光影、倾斜和长距离位移，保留直接呈现。
- 返回上一页、点击同一锚点、展开问题、切换方向、关闭菜单都保持正确位置和键盘焦点。
- 手机按 320、375、390、430px 检查；桌面至少检查 1280 和 1440px。英文长标题、中文断行、图表标签、导航和安全区域都需要实测。
- 图表的指标与假设继续明确标注；动效不把概念原型包装成已上线产品或已有业绩。三份提案各自八项正文不能因改版删减。
