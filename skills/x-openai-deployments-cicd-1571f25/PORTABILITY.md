# 迁移记录

来源：`upstream/openai/plugins`

原名称：`deployments-cicd`

原始副本位于导出包 `original-skills/x-openai-deployments-cicd-1571f25`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 跨宿主复审结论（2026-10-12）

- 审核范围：完整阅读 `SKILL.md`；manifest 未命中宿主词仍做正文人工检查。未执行源技能的业务操作。
- 结论：将插件快捷命令 /deploy、/status、/env 替换为 Vercel CLI 或项目控制台操作，补充 CLI 能力核验；部署产品语义保留。
- 状态：`adapted`（此轮正文已适配）。
- 剩余依赖：Vercel CLI 及已关联项目、部署令牌或授权登录；CI 提供方凭据和生产发布授权。
- 保留的真实产品/API 名称：Vercel、GitHub Actions、GitLab CI、Bitbucket Pipelines、AWS、GCP。
- 验证边界：完成静态可移植性审核；未验证远程账号、运行时软件、网络或目标宿主工具可用性。产品版本与价格等资料不在本次审核中重新核验。
