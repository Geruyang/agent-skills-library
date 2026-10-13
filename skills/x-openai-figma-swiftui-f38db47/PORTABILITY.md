# 迁移记录

来源：`upstream/openai/plugins`

原名称：`figma-swiftui`

原始副本位于导出包 `original-skills/x-openai-figma-swiftui-f38db47`，来源文件未修改。当前文件为独立副本。

原宿主元数据／执行限制如下。目标宿主须在其配置或等价权限机制中实施这些约束；若无法实施，则不要执行依赖这些约束的自动化步骤。模型名称作为原宿主参考，不强制目标宿主使用不存在的模型。

```yaml
disable-model-invocation: false
```

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 跨宿主逐项复审（2026-10-12）

- 结论：adapted。增加 Figma 读写能力与 schema 发现、原 companion skill 目录解析、精确符号/字体缺失说明及本地交付路径；不假设 REST 连接支持 use_figma。
- 阅读范围：完整 SKILL.md；manifest 的 host_matches 为空，无该字段要求追加的文件。
- 剩余依赖：Figma 设计读取/截图与精确映射能力；写入需授权且真实支持相应操作的 MCP/API；SwiftUI 项目与构建环境；关联技能需映射导出 ID。；当前导出目录未解析的原相对参考：../figma-generate-design/SKILL.md, ../figma-generate-library/SKILL.md, ../figma-use/SKILL.md
- 保留的真实产品/API/名称：Figma、SwiftUI、SF Symbols、Code Connect、get_design_context、use_figma。
- 验证边界：静态文档与文件检查；未登录远程服务、执行部署/写入、运行产品工作流或声称连接可用。名称保持导出唯一 ID。
