# 迁移记录

来源：`upstream/openai/plugins`

原名称：`adobe-batch-edit-photos`

原始副本位于导出包 `original-skills/x-openai-adobe-batch-edit-photos-3103583`，来源文件未修改。当前文件为独立副本。

原宿主元数据／执行限制如下。目标宿主须在其配置或等价权限机制中实施这些约束；若无法实施，则不要执行依赖这些约束的自动化步骤。模型名称作为原宿主参考，不强制目标宿主使用不存在的模型。

```yaml
allowed-tools: adobe_mandatory_init image_list_presets asset_add_file read_widget_context
  asset_initialize_file_upload asset_finalize_file_upload image_auto_straighten image_apply_auto_tone
  image_apply_adjustments image_apply_preset image_select_subject image_apply_gaussian_blur
  image_crop_and_resize asset_preview_file create_firefly_board
```

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐技能迁移审核（批2）

状态：`adapted`。

移除按宿主品牌假定widget支持的判断，按Adobe工具能力分流并保留预览确认。

运行依赖：Adobe Creative Cloud账户、对应MCP服务、上传权限

保留产品提及：Claude Cowork原产品背景、Adobe工具/URI/参数保留

检查范围：完整读取 SKILL.md，并读取清单命中的支持文件；扩展静态检查工具、路径与宿主引用。未执行这些技能、未进行服务登录或硬件/付费操作，不能据此声称端到端运行兼容。
