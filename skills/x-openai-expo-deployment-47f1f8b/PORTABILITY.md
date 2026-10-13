# 迁移记录

来源：`upstream/openai/plugins`

原名称：`expo-deployment`

原始副本位于导出包 `original-skills/x-openai-expo-deployment-47f1f8b`，来源文件未修改。当前文件为独立副本。

原宿主元数据／执行限制如下。目标宿主须在其配置或等价权限机制中实施这些约束；若无法实施，则不要执行依赖这些约束的自动化步骤。模型名称作为原宿主参考，不强制目标宿主使用不存在的模型。

```yaml
version: 1.0.0
```

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 跨宿主逐项复审（2026-10-12）

- 结论：reviewed-unchanged。保留 Expo/EAS/App Store/Play Store 部署命令与教程；无宿主绑定。
- 阅读范围：完整 SKILL.md；manifest 的 host_matches 为空，无该字段要求追加的文件。
- 剩余依赖：Node.js/npm 与 EAS CLI；Expo、Apple/Google 账户及发布权限；上游 ./reference/ 链接与实际 references/ 目录不一致，按实际目录读取。；当前导出目录未解析的原相对参考：./reference/ios-app-store.md, ./reference/play-store.md, ./reference/testflight.md, ./reference/workflows.md
- 保留的真实产品/API/名称：Expo、EAS、Apple App Store、TestFlight、Google Play Store。
- 验证边界：静态文档与文件检查；未登录远程服务、执行部署/写入、运行产品工作流或声称连接可用。名称保持导出唯一 ID。
