# 迁移记录

来源：`upstream/openai/skills`

原名称：`transcribe`

原始副本位于导出包 `original-skills/x-openai-transcribe-5df1773`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 本次逐项迁移审核（第 3 批）

- 结果：`adapted`。转写 CLI 改用技能目录解析，保留 OpenAI 转写模型与密钥隐私规则。
- 审核入口与匹配资源：`SKILL.md`。
- 仍需环境能力：Python / openai SDK；OpenAI API credential and network。
- 保留的真实产品或兼容字段：OpenAI；gpt-4o-mini-transcribe；gpt-4o-transcribe-diarize。
