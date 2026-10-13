# 迁移记录

来源：`upstream/openai/plugins`

原名称：`expo-dev-client`

原始副本位于导出包 `original-skills/x-openai-expo-dev-client-427e8e8`，来源文件未修改。当前文件为独立副本。

原宿主元数据／执行限制如下。目标宿主须在其配置或等价权限机制中实施这些约束；若无法实施，则不要执行依赖这些约束的自动化步骤。模型名称作为原宿主参考，不强制目标宿主使用不存在的模型。

```yaml
version: 1.0.0
```

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项可移植性审核（2026-10-12）

- 结论：reviewed-unchanged。
- Full workflow reviewed; CLI commands and artifact extensions are Expo/EAS platform requirements, not agent host bindings.
- 剩余依赖：Node.js;Expo/EAS CLI;platform build/signing tools。
- 保留产品/API引用：Expo;EAS;TestFlight;App Store Connect;Xcode。
- 完整读取 SKILL.md，核对 manifest host_matches（为空），并按命中检查相关支持文件；未执行来源工作流。详情见 `PORTABILITY_REVIEW.json`。
