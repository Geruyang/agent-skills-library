# 迁移记录

来源：`upstream/openai/plugins`

原名称：`research`

原始副本位于导出包 `original-skills/x-openai-research-4e6a95c`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## Cross-host manual review (2026-10-12)

- Result: `adapted`. Replaced assumed plugin sibling layout with companion-resource discovery and explicit missing-resource/source-access behavior.
- Review scope: complete SKILL.md and manifest host matches (none for this item); targeted local dependency/host-marker inspection. No source-skill workflow was executed.
- Remaining dependencies:
  - Web search and page retrieval or supplied evidence
  - User-authorized connectors for internal sources
  - Optional original index, critical-overrides and user-context companion resources; not bundled here
- Retained product/API references: Figma; Storybook; Reddit; X/Twitter; Hacker News; Stack Overflow; GitHub; Slack; Gong; Notion; Google Drive; Linear; Jira.
- Runtime limit: this static review does not prove tool installation, remote availability, credentials, live API compatibility, or successful execution. Discover actual capabilities before use and report missing ones; do not fabricate tool calls or outputs.
