# 迁移记录

来源：`upstream/openai/plugins`

原名称：`vercel-queues`

原始副本位于导出包 `original-skills/x-openai-vercel-queues-53a14e2`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 跨宿主复审结论（2026-10-12）

- 审核范围：完整阅读 `SKILL.md`；manifest 未命中宿主词仍做正文人工检查。未执行源技能的业务操作。
- 结论：Vercel Queues 的 API、鉴权与文档核验要求保持；不把云服务产品依赖误判为 agent 宿主绑定。
- 状态：`reviewed-unchanged`（此轮正文未改动）。
- 剩余依赖：Vercel Queues 服务、兼容 Node.js 与 @vercel/queue、OIDC 或 VERCEL_QUEUE_API_TOKEN；可访问官方文档。
- 保留的真实产品/API 名称：Vercel Queues、Vercel Workflow、Next.js。
- 验证边界：完成静态可移植性审核；未验证远程账号、运行时软件、网络或目标宿主工具可用性。产品版本与价格等资料不在本次审核中重新核验。
