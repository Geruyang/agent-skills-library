# 迁移记录

来源：`upstream/openai/plugins`

原名称：`tpmi-phewas-skill`

原始副本位于导出包 `original-skills/x-openai-tpmi-phewas-skill-40b33f1`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项语义审核（批次 2，尾段）

- 审核状态：`reviewed-unchanged`。
- 审核范围：完整 SKILL.md；manifest host_matches 为零，另检查相关工具名/宿主路径及命中的支持文件。
- 结论：TPMI变异解析和接口字段为真实服务契约，保留。
- 保留依赖：Python依赖；TPMI和变异解析服务网络访问。
- 保留产品名称：TPMI、PheWAS。
- TRAE / Claude 执行约束：先发现实际可用的工具、权限和依赖；缺失的执行能力明确报告阻塞。本文审核不代表已连接服务、安装运行时或完成外部操作。
