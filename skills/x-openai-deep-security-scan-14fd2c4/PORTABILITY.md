# 迁移记录

来源：`upstream/openai/plugins`

原名称：`deep-security-scan`

原始副本位于导出包 `original-skills/x-openai-deep-security-scan-14fd2c4`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项语义审核（批次4）

- 状态：`adapted`。
- 审核范围：完整读取 SKILL.md 及 3 个文本资源文件；复核清单 host_matches 并额外检查工具/路径假设。
- 结论：将Codex Security明确为可发现的外部MCP产品依赖，保留真实API和失败阻塞；移除默认当前宿主为Codex的暗示。
- 仍需验证：Codex Security MCP server与深度扫描生命周期API、访问权限。
- 保留产品语义：Codex Security产品名、start/complete/cancel_codex_security_*、Daybreak。
- 验证层级：静态适配审核；不代表已在目标宿主登录、连接服务或运行所有业务流程。
