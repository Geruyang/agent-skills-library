# 迁移记录

来源：`upstream/openai/plugins`

原名称：`codex-expo-run-actions`

原始副本位于导出包 `original-skills/x-openai-codex-expo-run-actions-2312b50`，来源文件未修改。当前文件为独立副本。

原宿主元数据／执行限制如下。目标宿主须在其配置或等价权限机制中实施这些约束；若无法实施，则不要执行依赖这些约束的自动化步骤。模型名称作为原宿主参考，不强制目标宿主使用不存在的模型。

```yaml
version: 1.0.0
```

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 跨宿主逐项复审（批次 7，2026-10-12）

- 结论：adapted。增加明确 Codex Run 产品目标的触发和写入限定；保留 .codex/environments/environment.toml、CLI 与 UI 的真实教程含义，不把其他当前宿主误认成 Codex。
- 阅读证据：`SKILL.md` (77 行), `agents/openai.yaml` (4 行), `references/expo-run-button-bootstrap.md` (208 行)；完整文件静态读取，清单命中逐项分类。
- 剩余依赖：目标产品 Codex app 的 Run actions 支持；Expo/Node.js 与项目本地 shell；其他客户端不能声称拥有 Codex Run 按钮。
- 保留的真实产品/API/URL：Codex、OpenAI、Expo。
- 边界：只修改导出副本；未运行源技能工作流、连接/发布远程服务、执行付费操作或修改原始技能。在线与 UI 可用性尚未验证。
