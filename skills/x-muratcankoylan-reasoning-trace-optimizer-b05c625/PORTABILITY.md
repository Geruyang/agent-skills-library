# 迁移记录

来源：`upstream/muratcankoylan/Agent-Skills-for-Context-Engineering`

原名称：`reasoning-trace-optimizer`

原始副本位于导出包 `original-skills/x-muratcankoylan-reasoning-trace-optimizer-b05c625`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项语义审核（批次 2，尾段）

- 审核状态：`adapted`。
- 审核范围：完整 SKILL.md；manifest host_matches 为零，另检查相关工具名/宿主路径及命中的支持文件。
- 结论：去除当前会话thinking自动可读和未实现命令的假设，改用授权导出trace。
- 保留依赖：MiniMax/API凭证；Python包；用户提供或授权导出trace。
- 保留产品名称：MiniMax M2.1、Claude、GPT。
- TRAE / Claude 执行约束：先发现实际可用的工具、权限和依赖；缺失的执行能力明确报告阻塞。本文审核不代表已连接服务、安装运行时或完成外部操作。
