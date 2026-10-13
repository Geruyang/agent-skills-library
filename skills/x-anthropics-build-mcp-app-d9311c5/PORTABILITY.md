# 迁移记录

来源：`upstream/anthropics/claude-plugins-official`

原名称：`build-mcp-app`

原始副本位于导出包 `original-skills/x-anthropics-build-mcp-app-d9311c5`，来源文件未修改。当前文件为独立副本。

原宿主元数据／执行限制如下。目标宿主须在其配置或等价权限机制中实施这些约束；若无法实施，则不要执行依赖这些约束的自动化步骤。模型名称作为原宿主参考，不强制目标宿主使用不存在的模型。

```yaml
version: 0.1.0
```

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项语义审核（2026-10-12）

- 状态：`reviewed-adapted`
- 检查范围：完整 `SKILL.md`；manifest `host_matches` 为空。
- 结论：加入MCP Apps/elicitation协商能力检测与资源定位，通用执行者改为assistant；SDK不冒充助手工具。
- 尚需能力/资源：Node.js、MCP/ext-apps SDK；目标客户端Apps/elicitation实测能力；可选build-mcp-server/build-mcpb技能。
- 保留产品引用：Claude/ChatGPT真实客户端；Claude Desktop配置及directory要求；@modelcontextprotocol/ext-apps真实SDK。
- 文件清单：`SKILL.md`、`PORTABILITY.md`、`PORTABILITY_REVIEW.json`。
