# 迁移记录

来源：`upstream/openai/plugins`

原名称：`ai-gateway`

原始副本位于导出包 `original-skills/x-openai-ai-gateway-d1b6180`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项宿主审核（批次 0）

- 状态：`reviewed-unchanged`
- 结论：全文已检查；Codex 命中属于 GPT-5.3-Codex 模型沿革，保留真实产品/API 示例，未引入宿主调用。
- 审阅文件：`SKILL.md`
- 实际依赖：Vercel AI Gateway/AI SDK、账户及认证；模型/价格/版本需在实际使用时按正文刷新官方文档。
- 保留的产品/历史名称：GPT-5.3-Codex 及 OpenAI、Anthropic、Vercel 模型/API/产品名。
- 验证范围：静态全文与宿主命中审核；未安装依赖、运行外部服务、执行硬件操作或验证账号连接。缺失能力不得宣称已完成。
- 资源解析：外部共享资源、相邻技能与插件根资源须按导出清单定位；路径不存在时先报告依赖缺失，不能把跨技能名称当成已安装证明。
