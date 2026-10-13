# 迁移记录

来源：`upstream/openai/plugins`

原名称：`boltz-small-molecule-design`

原始副本位于导出包 `original-skills/x-openai-boltz-small-molecule-design-f03693f`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项语义审核（批次4）

- 状态：`adapted`。
- 审核范围：完整读取 SKILL.md 及 5 个文本资源文件；复核清单 host_matches 并额外检查工具/路径假设。
- 结论：后台下载、进程句柄和监控改为当前宿主真实机制；保留成本确认及无调度能力时手动status交付。
- 仍需验证：boltz-api、Boltz认证、费用确认；持久进程/可选调度。
- 保留产品语义：Boltz API真实命令、参数和成本确认。
- 验证层级：静态适配审核；不代表已在目标宿主登录、连接服务或运行所有业务流程。
