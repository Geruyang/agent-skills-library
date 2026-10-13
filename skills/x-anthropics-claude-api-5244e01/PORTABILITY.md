# 迁移记录

来源：`upstream/anthropics/skills`

原名称：`claude-api`

原始副本位于导出包 `original-skills/x-anthropics-claude-api-5244e01`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐技能跨宿主审核（2026-10-12）

- 状态：`adapted`。
- 范围：完整阅读本技能 `SKILL.md`；本项 manifest `host_matches` 为空，无自动命中的额外文件。按正文语义区分宿主调用与真实产品接口。
- 审核结论：Mapped documentation fetching and user-question UI to discovered host capabilities; retained real Anthropic API/model/SDK and Agent SDK tool identities.
- 能力核验：这是静态移植审计；未安装依赖、未访问账号或硬件、未执行技能业务流程，不能据此声称目标环境可运行。
- 剩余依赖：
  - Appropriate official Anthropic SDK/runtime or authorized REST client
  - Anthropic or supported provider credentials for live requests
  - Network/documentation retrieval for current facts
  - Bundled language-specific references
- 保留的真实产品/协议名称：Claude/Anthropic models and prices as source reference, not revalidated here；Claude Agent SDK；Managed Agents；AWS Bedrock；Google Vertex AI；Microsoft Foundry；official SDK/API URLs。
- 缺失能力处理：按正文的已核验等价能力或本地交付路径执行；没有等价项时明确报告缺失，不伪造工具调用、远端状态或完成结果。
