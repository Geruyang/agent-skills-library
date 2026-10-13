# 迁移记录

来源：`upstream/openai/plugins`

原名称：`ios-ettrace-performance`

原始副本位于导出包 `original-skills/x-openai-ios-ettrace-performance-f35b770`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项语义审核（批次4）

- 状态：`adapted`。
- 审核范围：完整读取 SKILL.md 及 5 个文本资源文件；复核清单 host_matches 并额外检查工具/路径假设。
- 结论：ettrace采用宿主真实TTY和输入接口，临时前缀通用化；无TTY明确手动执行限制。
- 仍需验证：macOS、Xcode、ettrace、iOS设备/模拟器、TTY。
- 保留产品语义：ettrace、Apple工具链。
- 验证层级：静态适配审核；不代表已在目标宿主登录、连接服务或运行所有业务流程。
