# 迁移记录

来源：`upstream/openai/plugins`

原名称：`test-triage`

原始副本位于导出包 `original-skills/x-openai-test-triage-095824b`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 跨宿主逐项复审（2026-10-12）

- 结论：reviewed-unchanged。保留 Xcode/SwiftPM 测试分流与失败分类；命令是实际产品 CLI。
- 阅读范围：完整 SKILL.md；manifest 的 host_matches 为空，无该字段要求追加的文件。
- 剩余依赖：兼容 macOS/Xcode 或 SwiftPM 运行环境；待测项目及测试夹具。
- 保留的真实产品/API/名称：Xcode、SwiftPM、xcodebuild、swift test。
- 验证边界：静态文档与文件检查；未登录远程服务、执行部署/写入、运行产品工作流或声称连接可用。名称保持导出唯一 ID。
