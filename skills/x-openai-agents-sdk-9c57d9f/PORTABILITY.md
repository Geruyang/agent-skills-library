# 迁移记录

来源：`upstream/openai/plugins`

原名称：`agents-sdk`

原始副本位于导出包 `original-skills/x-openai-agents-sdk-9c57d9f`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 跨宿主逐项复审（2026-10-12）

- 结论：reviewed-unchanged。保留 Cloudflare Agents SDK 产品/API 教程及官方链接；不把 Agent/RPC/MCP 等产品术语当宿主限制。
- 阅读范围：完整 SKILL.md；manifest 的 host_matches 为空，无该字段要求追加的文件。
- 剩余依赖：Node.js/npm、agents 包、Cloudflare Workers/Wrangler 项目及需要时的账户权限；官方文档网络访问。
- 保留的真实产品/API/名称：Cloudflare、Agents SDK、Workers、Wrangler、React、McpAgent、https://developers.cloudflare.com/agents/、https://github.com/cloudflare/agents/tree/main/docs。
- 验证边界：静态文档与文件检查；未登录远程服务、执行部署/写入、运行产品工作流或声称连接可用。名称保持导出唯一 ID。
