# 迁移记录

来源：`upstream/anthropics/claude-plugins-official`

原名称：`configure`

原始副本位于导出包 `original-skills/x-anthropics-configure-c2b8855`，来源文件未修改。当前文件为独立副本。

原宿主元数据／执行限制如下。目标宿主须在其配置或等价权限机制中实施这些约束；若无法实施，则不要执行依赖这些约束的自动化步骤。模型名称作为原宿主参考，不强制目标宿主使用不存在的模型。

```yaml
user-invocable: true
allowed-tools:
- Read
- Write
- Bash(ls *)
- Bash(mkdir *)
```

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项语义审核（2026-10-12）

- 状态：`reviewed-adapted`
- 检查范围：完整 `SKILL.md`；manifest `host_matches` 为空。
- 结论：明确教程配置原Claude Discord服务，先核验路径/命令/权限，保留产品默认目录。
- 尚需能力/资源：Claude Discord channel server；授权凭据文件读写与系统权限工具。
- 保留产品引用：Discord、Claude渠道配置；~/.claude/channels/discord与/discord命令。
- 文件清单：`SKILL.md`、`PORTABILITY.md`、`PORTABILITY_REVIEW.json`。
