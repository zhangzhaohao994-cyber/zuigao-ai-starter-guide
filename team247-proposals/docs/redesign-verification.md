# 两版重设计验证 / Redesign verification

核验日期：2026-11-07。

- A、B、选择页脚本语法检查；静态资源和文档引用检查。
- 桌面 1280px 与 390px 手机宽度检查；中英文首屏均可读，手机两版 document.scrollWidth 与 390px 视口一致。
- A 完整阅读层显示八问；打开时停止背景绘制，关闭恢复原暂停状态。
- A 故事分支切换后焦点保留在新叙述；行业流程运行中切换语言会取消旧流程、重置按钮。
- B 人设与场景、行业节点、剧情分支与重选、全文八问、分组阅读均检查。
- B 分享图表验证：10 位创作者 × 6 位玩家 × 20% = 12 位下一轮创作者，均为假设。
- B 暂停及系统 prefers-reduced-motion 后，标题文字完全可见。
- 固定版本开源依赖及原始 MIT 许可证随站点保存，不依赖实时 CDN。

## 绘制路径的验证边界 / Rendering coverage

当前浏览器测试环境禁用了 WebGL，因此 A 的 Three.js 路径完成静态审查，但没有在该环境中验证实际 GPU 渲染。已实际观察并测试它的 Canvas2D 连续液态光影兼容路径。普通浏览器支持 WebGL 时优先使用 Three.js；不支持时自动使用 Canvas2D。未进行实体手机的帧率或耗电测量。

The test browser disables WebGL. A's Three.js path was statically reviewed, while its animated Canvas2D fallback was visually and interactively tested. Hardware frame rate and battery use have not been measured on a physical phone.

这两版是提案展示，概念交互与图表不代表 AI 产品已经上线或商业假设已经验证。
