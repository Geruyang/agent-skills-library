# 迁移记录

来源：`upstream/openai/plugins`

原名称：`twilio-conference-calls`

原始副本位于导出包 `original-skills/x-openai-twilio-conference-calls-4e242fe`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## Cross-host manual review (2026-10-12)

- Result: `reviewed-unchanged`. Twilio Conference API/SDK patterns are host-independent; preserved body.
- Review scope: complete SKILL.md and manifest host matches (none for this item); targeted local dependency/host-marker inspection. No source-skill workflow was executed.
- Remaining dependencies:
  - Twilio account, voice-capable number and credentials
  - Python or Node.js Twilio SDK and webhook application
  - TaskRouter if agent routing is required
- Retained product/API references: Twilio Conference; TwiML; TaskRouter; Flask; Express; Voice Insights.
- Runtime limit: this static review does not prove tool installation, remote availability, credentials, live API compatibility, or successful execution. Discover actual capabilities before use and report missing ones; do not fabricate tool calls or outputs.
