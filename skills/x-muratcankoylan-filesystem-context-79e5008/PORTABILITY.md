# 迁移记录

来源：`upstream/muratcankoylan/Agent-Skills-for-Context-Engineering`

原名称：`filesystem-context`

原始副本位于导出包 `original-skills/x-muratcankoylan-filesystem-context-79e5008`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项语义审核（批次 2，尾段）

- 审核状态：`reviewed-unchanged`。
- 审核范围：完整 SKILL.md；manifest host_matches 为零，另检查相关工具名/宿主路径及命中的支持文件。
- 结论：文件型上下文方法保留，通用工具名作为示意。
- 保留依赖：文件读写/搜索能力；子代理共享目录需权限。
- 保留产品名称：LangChain、Cursor、Anthropic Agent Skills。
- TRAE / Claude 执行约束：先发现实际可用的工具、权限和依赖；缺失的执行能力明确报告阻塞。本文审核不代表已连接服务、安装运行时或完成外部操作。
