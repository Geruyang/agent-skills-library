# 迁移记录

来源：`upstream/openai/plugins`

原名称：`adobe-create-mockups`

原始副本位于导出包 `original-skills/x-openai-adobe-create-mockups-039bd3f`，来源文件未修改。当前文件为独立副本。

原宿主元数据／执行限制如下。目标宿主须在其配置或等价权限机制中实施这些约束；若无法实施，则不要执行依赖这些约束的自动化步骤。模型名称作为原宿主参考，不强制目标宿主使用不存在的模型。

```yaml
allowed-tools: adobe_mandatory_init asset_share_link boards_add_items_to_board boards_create_new_board
  image_generate
```

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项语义审核（批次4）

- 状态：`adapted`。
- 审核范围：完整读取 SKILL.md 及 5 个文本资源文件；复核清单 host_matches 并额外检查工具/路径假设。
- 结论：去除Codex唯一surface元数据；Adobe实际工具、登录与pilot批准仍为要求。
- 仍需验证：Adobe/Firefly认证、图像生成与Board工具。
- 保留产品语义：Adobe Firefly真实工具及参数。
- 验证层级：静态适配审核；不代表已在目标宿主登录、连接服务或运行所有业务流程。
