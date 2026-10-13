# 迁移记录

来源：`upstream/openai/plugins`

原名称：`adobe-design-from-template`

原始副本位于导出包 `original-skills/x-openai-adobe-design-from-template-08bc699`，来源文件未修改。当前文件为独立副本。

原宿主元数据／执行限制如下。目标宿主须在其配置或等价权限机制中实施这些约束；若无法实施，则不要执行依赖这些约束的自动化步骤。模型名称作为原宿主参考，不强制目标宿主使用不存在的模型。

```yaml
allowed-tools: adobe_mandatory_init search_design fill_text replace_image change_background_color
  animate_design download_design
```

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项语义审核

- 状态：`reviewed-adapted`。已完整读取 SKILL.md，并检查清单命中的支持文件；未执行源文指令。
- 结论：将Codex/Claude的固定图库与生成能力断言改为实际Adobe连接器权限和呈现能力；保留模板选择、文档URN继承、编辑边界和缺能力说明。
- 仍需能力／依赖：已登录Adobe Express连接器及初始化/搜索；可选文本、图片、动画和导出工具。
- 保留的产品／历史引用：Adobe Express/API字段/工具名称及官方产品实体
- 验证边界：这是静态语义与资源审查，不表示已在 TRAE 或 Claude 中完成远程服务认证或端到端实跑。
