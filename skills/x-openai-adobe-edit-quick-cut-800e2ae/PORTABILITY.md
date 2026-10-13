# 迁移记录

来源：`upstream/openai/plugins`

原名称：`adobe-edit-quick-cut`

原始副本位于导出包 `original-skills/x-openai-adobe-edit-quick-cut-800e2ae`，来源文件未修改。当前文件为独立副本。

原宿主元数据／执行限制如下。目标宿主须在其配置或等价权限机制中实施这些约束；若无法实施，则不要执行依赖这些约束的自动化步骤。模型名称作为原宿主参考，不强制目标宿主使用不存在的模型。

```yaml
allowed-tools: adobe_mandatory_init asset_add_file asset_initialize_file_upload asset_finalize_file_upload
  video_create_quick_cut quickCutPoll asset_preview_file video_resize
```

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 本次逐项迁移审核（第 3 批）

- 结果：`adapted`。Adobe widget 与媒体预览按工具实际可用性分支，保留 assetId、egress 检查和禁止原始路径传视频工具。
- 审核入口与匹配资源：`SKILL.md`。
- 仍需环境能力：Adobe MCP connector / authentication；Asset staging egress when no picker。
- 保留的真实产品或兼容字段：Adobe；Claude Cowork example。
