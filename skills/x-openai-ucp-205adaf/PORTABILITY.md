# 迁移记录

来源：`upstream/openai/plugins`

原名称：`ucp`

原始副本位于导出包 `original-skills/x-openai-ucp-205adaf`，来源文件未修改。当前文件为独立副本。

原宿主元数据／执行限制如下。目标宿主须在其配置或等价权限机制中实施这些约束；若无法实施，则不要执行依赖这些约束的自动化步骤。模型名称作为原宿主参考，不强制目标宿主使用不存在的模型。

```yaml
requires_bin: ucp
command: ucp
```

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## Cross-host manual review (2026-10-12)

- Result: `reviewed-unchanged`. Product-specific UCP CLI, profile and merchant capability discovery are portable; preserved workflow.
- Review scope: complete SKILL.md and manifest host matches (none for this item); targeted local dependency/host-marker inspection. No source-skill workflow was executed.
- Remaining dependencies:
  - Installed UCP CLI and process execution
  - Network access, local profile for merchant-scoped flows and merchant support
  - Required buyer authorization and merchant fulfillment/payment inputs
- Retained product/API references: UCP CLI; Shopify; JMESPath.
- Runtime limit: this static review does not prove tool installation, remote availability, credentials, live API compatibility, or successful execution. Discover actual capabilities before use and report missing ones; do not fabricate tool calls or outputs.
