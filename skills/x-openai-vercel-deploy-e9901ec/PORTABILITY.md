# 迁移记录

来源：`upstream/openai/skills`

原名称：`vercel-deploy`

原始副本位于导出包 `original-skills/x-openai-vercel-deploy-e9901ec`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 跨宿主逐项复审（批次 7，2026-10-12）

- 结论：adapted。Vercel 部署审批选项改成实际宿主机制；保留 Codex-named deploy URL 作为真实原部署服务地址，不将其替换成虚构域名。
- 阅读证据：`SKILL.md` (83 行), `scripts/deploy.sh` (301 行)；完整文件静态读取，清单命中逐项分类。
- 剩余依赖：Vercel CLI/认证或随包部署服务；网络与明确部署授权；原服务 URL 可用性未联网验证。
- 保留的真实产品/API/URL：OpenAI、Expo、Vercel。
- 边界：只修改导出副本；未运行源技能工作流、连接/发布远程服务、执行付费操作或修改原始技能。在线与 UI 可用性尚未验证。
