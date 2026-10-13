# 迁移记录

来源：`upstream/openai/plugins`

原名称：`dashboards-and-real-time-visualization`

原始副本位于导出包 `original-skills/x-openai-dashboards-and-real-time-visualization-e30f167`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项语义审核（2026-10-12）

- 状态：`reviewed-adapted`
- 检查范围：完整 `SKILL.md`；manifest `host_matches` 为空。
- 结论：将缺失插件树外引用改为可定位包资源标识；测试技能按名称定位，缺失明确阻塞。
- 尚需能力/资源：build-web-data-visualization共享foundations；可选testing-data-visualizations；项目数据和可视化运行环境。
- 保留产品引用：Canvas/WebGL和图形库实现选项。
- 文件清单：`SKILL.md`、`PORTABILITY.md`、`PORTABILITY_REVIEW.json`。
