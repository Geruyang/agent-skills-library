# 迁移记录

来源：`upstream/anthropics/claude-plugins-official`

原名称：`project-artifact`

原始副本位于导出包 `original-skills/x-anthropics-project-artifact-57711f6`，来源文件未修改。当前文件为独立副本。

原宿主元数据／执行限制如下。目标宿主须在其配置或等价权限机制中实施这些约束；若无法实施，则不要执行依赖这些约束的自动化步骤。模型名称作为原宿主参考，不强制目标宿主使用不存在的模型。

```yaml
user-invocable: true
```

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项语义审核（批次4）

- 状态：`adapted`。
- 审核范围：完整读取 SKILL.md 及 4 个文本资源文件；复核清单 host_matches 并额外检查工具/路径假设。
- 结论：Claude Artifact发布和数据目录明确为产品能力；其他宿主交付同样自包含状态页，不伪造URL或扩大分享权限。
- 仍需验证：Claude Artifact发布需登录与真实工具；本地模式需要文件写入/HTML预览；项目来源如gh/git或已授权连接器。
- 保留产品语义：Claude Artifact、CLAUDE_PLUGIN_DATA、claude.ai URL为真实产品能力。
- 验证层级：静态适配审核；不代表已在目标宿主登录、连接服务或运行所有业务流程。
