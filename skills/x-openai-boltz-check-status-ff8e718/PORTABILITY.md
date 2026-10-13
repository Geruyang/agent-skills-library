# 迁移记录

来源：`upstream/openai/plugins`

原名称：`boltz-check-status`

原始副本位于导出包 `original-skills/x-openai-boltz-check-status-ff8e718`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 本次逐项迁移审核（第 3 批）

- 结果：`adapted`。Boltz 长任务与轮询改为当前宿主受管进程和可用调度器，保留恢复游标、同ID重试与认证规则。
- 审核入口与匹配资源：`SKILL.md`, `references/api.md`, `references/resume.md`。
- 仍需环境能力：boltz-api CLI and authentication；Managed process support optional；Scheduler only for authorized follow-up。
- 保留的真实产品或兼容字段：Boltz；Claude Code conditional background example。
