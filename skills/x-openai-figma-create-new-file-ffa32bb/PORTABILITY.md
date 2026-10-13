# 迁移记录

来源：`upstream/openai/plugins`

原名称：`figma-create-new-file`

原始副本位于导出包 `original-skills/x-openai-figma-create-new-file-ffa32bb`，来源文件未修改。当前文件为独立副本。

原宿主元数据／执行限制如下。目标宿主须在其配置或等价权限机制中实施这些约束；若无法实施，则不要执行依赖这些约束的自动化步骤。模型名称作为原宿主参考，不强制目标宿主使用不存在的模型。

```yaml
disable-model-invocation: false
```

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项语义审核（批次 2，尾段）

- 审核状态：`adapted`。
- 审核范围：完整 SKILL.md；manifest host_matches 为零，另检查相关工具名/宿主路径及命中的支持文件。
- 结论：明确Figma创建工具及计划字段是特定适配器契约；无能力则阻塞。
- 保留依赖：Figma账户；支持空白文件创建的MCP/适配器。
- 保留产品名称：Figma、FigJam、Slides。
- TRAE / Claude 执行约束：先发现实际可用的工具、权限和依赖；缺失的执行能力明确报告阻塞。本文审核不代表已连接服务、安装运行时或完成外部操作。
