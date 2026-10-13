# 迁移记录

来源：`upstream/muratcankoylan/Agent-Skills-for-Context-Engineering`

原名称：`digital-brain`

原始副本位于导出包 `original-skills/x-muratcankoylan-digital-brain-1ef9ebd`，来源文件未修改。当前文件为独立副本。

原宿主元数据／执行限制如下。目标宿主须在其配置或等价权限机制中实施这些约束；若无法实施，则不要执行依赖这些约束的自动化步骤。模型名称作为原宿主参考，不强制目标宿主使用不存在的模型。

```yaml
version: 1.0.0
```

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 跨宿主复审结论（2026-10-12）

- 审核范围：完整阅读 `SKILL.md`；manifest 未命中宿主词仍做正文人工检查。未执行源技能的业务操作。
- 结论：Digital Brain 的本地文件模块与 Python 脚本为通用能力，正文保留。
- 状态：`reviewed-unchanged`（此轮正文未改动）。
- 剩余依赖：用户个人 identity/content/network/operations 数据与模块文件；Python 用于可选回顾脚本。
- 保留的真实产品/API 名称：Anthropic、X。
- 验证边界：完成静态可移植性审核；未验证远程账号、运行时软件、网络或目标宿主工具可用性。产品版本与价格等资料不在本次审核中重新核验。
