# 迁移记录

来源：`upstream/openai/plugins`

原名称：`adobe-retouch-portraits`

原始副本位于导出包 `original-skills/x-openai-adobe-retouch-portraits-7f439fb`，来源文件未修改。当前文件为独立副本。

原宿主元数据／执行限制如下。目标宿主须在其配置或等价权限机制中实施这些约束；若无法实施，则不要执行依赖这些约束的自动化步骤。模型名称作为原宿主参考，不强制目标宿主使用不存在的模型。

```yaml
allowed-tools: adobe_mandatory_init image_list_presets asset_add_file read_widget_context
  asset_initialize_file_upload asset_finalize_file_upload asset_preview_file image_auto_straighten
  image_apply_auto_tone image_apply_adjustments image_select_subject image_apply_preset
  image_apply_lens_blur image_apply_gaussian_blur image_crop_and_resize image_fill_area
  create_firefly_board
```

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项语义审核（批次4）

- 状态：`adapted`。
- 审核范围：完整读取 SKILL.md 及 5 个文本资源文件；复核清单 host_matches 并额外检查工具/路径假设。
- 结论：Adobe窗口与生成能力按当前连接器和宿主许可判定，移除品牌硬编码；保留非生成默认、人像保护和批准检查。
- 仍需验证：Adobe登录/Creative Cloud存储、对应图像工具；生成需实际能力和宿主允许。
- 保留产品语义：Adobe、Creative Cloud、真实工具名。
- 验证层级：静态适配审核；不代表已在目标宿主登录、连接服务或运行所有业务流程。
