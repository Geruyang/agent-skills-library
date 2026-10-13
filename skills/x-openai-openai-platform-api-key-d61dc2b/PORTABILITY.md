# 迁移记录

来源：`upstream/openai/plugins`

原名称：`openai-platform-api-key`

原始副本位于导出包 `original-skills/x-openai-openai-platform-api-key-d61dc2b`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 本次逐项迁移审核（第 3 批）

- 结果：`adapted`。密钥技能保持显式确认和加密写入门禁；仅在发现安全连接器及 helper 后执行原产品协议，缺能力明确阻塞。
- 审核入口与匹配资源：`SKILL.md`, `references/evals.md`。
- 仍需环境能力：OpenAI Platform secure connector；Encrypted-key provisioning；Verified local helper and explicit destination confirmation。
- 保留的真实产品或兼容字段：open_codex_api_key_setup actual API identifier；OpenAI Platform；ChatGPT widget boundary。
