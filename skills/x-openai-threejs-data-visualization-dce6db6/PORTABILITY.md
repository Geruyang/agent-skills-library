# 迁移记录

来源：`upstream/openai/plugins`

原名称：`threejs-data-visualization`

原始副本位于导出包 `original-skills/x-openai-threejs-data-visualization-dce6db6`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项语义审核（2026-10-12）

- 状态：`reviewed-adapted`
- 检查范围：完整 `SKILL.md`；manifest `host_matches` 为空。
- 结论：共享理论/模板按包资源定位，缺失前置报告，保留真实图形库及平台API。
- 尚需能力/资源：build-web-data-visualization共享foundations和advanced-interactive模板；目标浏览器GPU/WebGL及选定图形库。
- 保留产品引用：Three.js、WebGL/WebGPU、deck.gl等库；WebXR和浏览器权限API。
- 文件清单：`SKILL.md`、`PORTABILITY.md`、`PORTABILITY_REVIEW.json`。
