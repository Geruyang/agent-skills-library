# 迁移记录

来源：`upstream/openai/plugins`

原名称：`vercel-sandbox`

原始副本位于导出包 `original-skills/x-openai-vercel-sandbox-de79966`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项可移植性审核（2026-10-12）

- 结论：reviewed-adapted。
- Added real Vercel capability/credential checks, distinguished guest Linux commands, and resolved missing upstream helper paths.
- 剩余依赖：Vercel Sandbox service/account;SDK or equivalent API;Node runtime;upstream demo helper not bundled。
- 保留产品/API引用：Vercel Sandbox;Firecracker;agent-browser;Chrome;Amazon Linux;OIDC。
- 完整读取 SKILL.md，核对 manifest host_matches（为空），并按命中检查相关支持文件；未执行来源工作流，也未把静态审核视为产品实时规格验证。详情见 `PORTABILITY_REVIEW.json`。
