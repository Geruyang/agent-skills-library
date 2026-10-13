# 迁移记录

来源：`upstream/openai/plugins`

原名称：`react-best-practices`

原始副本位于导出包 `original-skills/x-openai-react-best-practices-12482cc`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项可移植性审核（2026-10-12）

- 结论：reviewed-unchanged。
- Reviewed full skill and supporting host-match scan; package-relative rules and compiled AGENTS.md are bundled product guidance.
- 剩余依赖：React/Next.js project for application;runtime tools for validation。
- 保留产品/API引用：React;Next.js;Vercel。
- 完整读取 SKILL.md，核对 manifest host_matches（为空），并按命中检查相关支持文件；未执行来源工作流，也未把静态审核视为产品实时规格验证。详情见 `PORTABILITY_REVIEW.json`。
