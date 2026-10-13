# 迁移记录

来源：`upstream/anthropics/claude-plugins-official`

原名称：`plugin-settings`

原始副本位于导出包 `original-skills/x-anthropics-plugin-settings-cf24312`，来源文件未修改。当前文件为独立副本。

原宿主元数据／执行限制如下。目标宿主须在其配置或等价权限机制中实施这些约束；若无法实施，则不要执行依赖这些约束的自动化步骤。模型名称作为原宿主参考，不强制目标宿主使用不存在的模型。

```yaml
version: 0.1.0
```

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项语义审核（2026-10-12）

- 状态：`reviewed-unchanged`
- 检查范围：完整 `SKILL.md`；manifest `host_matches` 为空。
- 结论：明确为Claude Code插件设置教程；.claude与Read/Bash是教程对象，不做全局替换。
- 尚需能力/资源：Claude Code插件目标环境；运行shell示例需Bash和文本工具。
- 保留产品引用：Claude Code、.claude/*.local.md、allowed-tools；ralph-loop/multi-agent-swarm示例。
- 文件清单：`PORTABILITY.md`、`PORTABILITY_REVIEW.json`。
