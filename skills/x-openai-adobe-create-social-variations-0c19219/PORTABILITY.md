# 迁移记录

来源：`upstream/openai/plugins`

原名称：`adobe-create-social-variations`

原始副本位于导出包 `original-skills/x-openai-adobe-create-social-variations-0c19219`，来源文件未修改。当前文件为独立副本。

原宿主元数据／执行限制如下。目标宿主须在其配置或等价权限机制中实施这些约束；若无法实施，则不要执行依赖这些约束的自动化步骤。模型名称作为原宿主参考，不强制目标宿主使用不存在的模型。

```yaml
allowed-tools: adobe_mandatory_init asset_initialize_file_upload asset_finalize_file_upload
  asset_add_file asset_inline_preview asset_preview_file image_crop_and_resize image_generative_expand
  video_resize resizeVideoPoll
```

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项语义审核

- 状态：`reviewed-adapted`。已完整读取 SKILL.md，并检查清单命中的支持文件；未执行源文指令。
- 结论：按实际组件可用性选择Adobe上传、选图和预览，不再以Codex/Claude名称推定能力；替换固定上传目录，保留Adobe API名、云资产上传约束与预览审批。
- 仍需能力／依赖：已认证Adobe Creative Cloud MCP连接；裁切、上传、预览及可选生成/视频权限；网络上传权限。
- 保留的产品／历史引用：Adobe Creative Cloud / Adobe for creativity 与真实工具名称；平台名称和尺寸示例保留，运行时仍需按用户目标核验
- 验证边界：这是静态语义与资源审查，不表示已在 TRAE 或 Claude 中完成远程服务认证或端到端实跑。
