# 迁移记录

来源：`upstream/openai/plugins`

原名称：`biostudies-arrayexpress-skill`

原始副本位于导出包 `original-skills/x-openai-biostudies-arrayexpress-skill-920e064`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项可移植性审核（2026-10-12）

- 结论：reviewed-adapted。
- Resolved Python/HTTP execution and removed fixed /tmp raw-output path.
- 剩余依赖：Python 3 and requests or equivalent HTTP client;network;authorized output directory。
- 保留产品/API引用：BioStudies;ArrayExpress。
- 完整读取 SKILL.md，核对 manifest host_matches（为空），并按命中检查相关支持文件；未执行来源工作流。详情见 `PORTABILITY_REVIEW.json`。
