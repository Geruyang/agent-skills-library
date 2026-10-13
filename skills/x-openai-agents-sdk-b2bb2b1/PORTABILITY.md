# 迁移记录

来源：`upstream/openai/plugins`

原名称：`agents-sdk`

原始副本位于导出包 `original-skills/x-openai-agents-sdk-b2bb2b1`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 本次逐项迁移审核（第 3 批）

- 结果：`adapted`。当前执行者和来源对话改为宿主中立，保留 Agents SDK 和部署管理器依赖。
- 审核入口与匹配资源：`SKILL.md`。
- 仍需环境能力：OpenAI Agents SDK；API credentials；Optional Deployment Manager。
- 保留的真实产品或兼容字段：OpenAI Agents SDK；Deployment Manager。
