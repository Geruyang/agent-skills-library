# 迁移记录

来源：`upstream/openai/plugins`

原名称：`view-refactor`

原始副本位于导出包 `original-skills/x-openai-view-refactor-7fc3b20`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项语义审核（2026-10-12）

- 状态：`reviewed-unchanged`
- 检查范围：完整 `SKILL.md`；manifest `host_matches` 为空。
- 结论：macOS重构正文的文件结构与API是目标工程约定，无宿主固定路径。
- 尚需能力/资源：macOS SwiftUI工程与Apple工具链；可选swiftui-patterns/appkit-interop。
- 保留产品引用：macOS、SwiftUI、AppKit。
- 文件清单：`PORTABILITY.md`、`PORTABILITY_REVIEW.json`。
