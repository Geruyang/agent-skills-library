# 迁移记录

来源：`upstream/openai/skills`

原名称：`figma`

原始副本位于导出包 `original-skills/x-openai-figma-8a2aede`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。
## 逐项语义审核（第5批）

- 审核状态：`adapted`。
- 审核范围：完整读取 `SKILL.md` 与 6 个可读文本文件；复核 7 条原清单宿主匹配。
- 结论：Figma MCP配置改为先发现当前客户端HTTP/OAuth能力，原Codex TOML作为明确的可选产品示例保留；凭据仅检查是否存在。
- 剩余依赖：Figma MCP server and authorized account；Current host streamable HTTP/OAuth or supported bearer authentication。
- 保留产品语义：Codex TOML configuration example is explicitly product-specific；https://mcp.figma.com/mcp and Figma headers。
- 验证边界：静态迁移审核；未执行技能业务、登录外部账户或在TRAE/Claude中实跑。当前宿主能力不足时须报告真实阻塞，不能虚构调用或完成状态。
