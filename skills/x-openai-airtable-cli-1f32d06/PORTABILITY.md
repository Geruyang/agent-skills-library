# 迁移记录

来源：`upstream/openai/plugins`

原名称：`airtable-cli`

原始副本位于导出包 `original-skills/x-openai-airtable-cli-1f32d06`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐技能跨宿主审核（2026-10-12）

- 状态：`reviewed-unchanged`。
- 范围：完整阅读本技能 `SKILL.md`；本项 manifest `host_matches` 为空，无自动命中的额外文件。按正文语义区分宿主调用与真实产品接口。
- 审核结论：Portable airtable-mcp CLI with runtime tool discovery already present; retained body.
- 能力核验：这是静态移植审计；未安装依赖、未访问账号或硬件、未执行技能业务流程，不能据此声称目标环境可运行。
- 剩余依赖：
  - Node.js/npm and @airtable/mcp-cli
  - Airtable PAT with appropriate scopes
  - Network access to the Airtable MCP service
- 保留的真实产品/协议名称：Airtable；airtable-mcp；@airtable/mcp-cli；AIRTABLE_TOKEN；airtable.com URLs。
- 缺失能力处理：按正文的已核验等价能力或本地交付路径执行；没有等价项时明确报告缺失，不伪造工具调用、远端状态或完成结果。
