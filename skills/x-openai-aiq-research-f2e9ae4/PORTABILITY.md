# 迁移记录

来源：`upstream/openai/plugins`

原名称：`aiq-research`

原始副本位于导出包 `original-skills/x-openai-aiq-research-f2e9ae4`，来源文件未修改。当前文件为独立副本。

原宿主元数据／执行限制如下。目标宿主须在其配置或等价权限机制中实施这些约束；若无法实施，则不要执行依赖这些约束的自动化步骤。模型名称作为原宿主参考，不强制目标宿主使用不存在的模型。

```yaml
permissions:
  env:
  - AIQ_SERVER_URL
  network:
  - http://localhost:8000
allowed-tools: Read Bash
```

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项语义审核

- 状态：`reviewed-unchanged`。已完整读取 SKILL.md，并检查清单命中的支持文件；未执行源文指令。
- 结论：正文已采用真实Python HTTP助手、可配置后端和能力条件分支；Codex仅出现在平台清单与原始评测结果，保持原文。
- 仍需能力／依赖：Python3.11+；兼容AI-Q Blueprint服务器及网络；非本地后端明确用户信任；此公开helper不管理认证。
- 保留的产品／历史引用：Codex/claude-code为历史评测代理；NVIDIA AI-Q/版本与产品URL
- 验证边界：这是静态语义与资源审查，不表示已在 TRAE 或 Claude 中完成远程服务认证或端到端实跑。
