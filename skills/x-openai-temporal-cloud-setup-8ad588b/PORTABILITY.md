# 迁移记录

来源：`upstream/openai/plugins`

原名称：`temporal-cloud-setup`

原始副本位于导出包 `original-skills/x-openai-temporal-cloud-setup-8ad588b`，来源文件未修改。当前文件为独立副本。

原宿主元数据／执行限制如下。目标宿主须在其配置或等价权限机制中实施这些约束；若无法实施，则不要执行依赖这些约束的自动化步骤。模型名称作为原宿主参考，不强制目标宿主使用不存在的模型。

```yaml
version: 0.8.1
disable-model-invocation: true
```

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 跨宿主逐项复审（批次 7，2026-10-12）

- 结论：adapted。保留 Temporal 真实 CLI、账单/凭据确认门槛及可移植 provision.sh；移除凭 Codex 品牌推断默认网络封锁和专属输出通道命名。
- 阅读证据：`SKILL.md` (803 行), `references/failure-handling.md` (39 行), `scripts/provision.sh` (2096 行)；完整文件静态读取，清单命中逐项分类。
- 剩余依赖：Bash、Git、Temporal CLI、浏览器登录和 *.tmprl.cloud gRPC egress；各阶段原授权门槛保留。
- 保留的真实产品/API/URL：Codex、OpenAI、Claude Code、Claude、Cursor、Expo、Render、Temporal、https://cloud.temporal.io/namespaces/、https://docs.temporal.io/cli、https://docs.temporal.io/cloud/api-keys、https://docs.temporal.io/develop、https://docs.temporal.io/encyclopedia/retry-policies、https://docs.temporal.io/workflows、https://github.com/temporalio/cloud-cli/releases/latest、https://github.com/temporalio/money-transfer-project-java。
- 边界：只修改导出副本；未运行源技能工作流、连接/发布远程服务、执行付费操作或修改原始技能。在线与 UI 可用性尚未验证。
