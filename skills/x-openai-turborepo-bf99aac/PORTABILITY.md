# 迁移记录

来源：`upstream/openai/plugins`

原名称：`turborepo`

原始副本位于导出包 `original-skills/x-openai-turborepo-bf99aac`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项可移植性审核（2026-10-12）

- 结论：reviewed-unchanged。
- Reviewed all 611 lines; Bash/Ubuntu CI examples, environment variables, output names and paths are project/product examples.
- 剩余依赖：Turborepo;project package manager/runtime;Vercel account for remote cache。
- 保留产品/API引用：Turborepo;Vercel;GitHub Actions;Bun;Next.js。
- 完整读取 SKILL.md，核对 manifest host_matches（为空），并按命中检查相关支持文件；未执行来源工作流，也未把静态审核视为产品实时规格验证。详情见 `PORTABILITY_REVIEW.json`。
