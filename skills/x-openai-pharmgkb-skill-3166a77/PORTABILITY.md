# 迁移记录

来源：`upstream/openai/plugins`

原名称：`pharmgkb-skill`

原始副本位于导出包 `original-skills/x-openai-pharmgkb-skill-3166a77`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## Cross-host manual review (2026-10-12)

- Result: `reviewed-unchanged`. Portable Python REST workflow; no host-specific invocation found.
- Review scope: complete SKILL.md and manifest host matches (none for this item); targeted local dependency/host-marker inspection. No source-skill workflow was executed.
- Remaining dependencies:
  - Python 3 and requests
  - Network access to api.pharmgkb.org; API availability
  - Writable output path for requested raw payloads
- Retained product/API references: PharmGKB; https://api.pharmgkb.org/v1/data.
- Runtime limit: this static review does not prove tool installation, remote availability, credentials, live API compatibility, or successful execution. Discover actual capabilities before use and report missing ones; do not fabricate tool calls or outputs.
