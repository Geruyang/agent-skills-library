# 迁移记录

来源：`upstream/openai/plugins`

原名称：`swiftui-ui-patterns`

原始副本位于导出包 `original-skills/x-openai-swiftui-ui-patterns-b27821b`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 跨宿主逐项复审（2026-10-12）

- 结论：reviewed-unchanged。保留 SwiftUI 状态、导航、预览与构建指导；未发现执行宿主绑定。
- 阅读范围：完整 SKILL.md；manifest 的 host_matches 为空，无该字段要求追加的文件。
- 剩余依赖：Swift/SwiftUI 项目；构建与预览通常需要兼容 macOS/Xcode；Apple 文档检索能力用于版本核验。
- 保留的真实产品/API/名称：SwiftUI、Swift、Apple、Xcode、iOS。
- 验证边界：静态文档与文件检查；未登录远程服务、执行部署/写入、运行产品工作流或声称连接可用。名称保持导出唯一 ID。
