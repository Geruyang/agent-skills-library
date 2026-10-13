# 迁移记录

来源：`upstream/openai/plugins`

原名称：`mixpanel-headless-setup`

原始副本位于导出包 `original-skills/x-openai-mixpanel-headless-setup-1c898d2`，来源文件未修改。当前文件为独立副本。

原宿主元数据／执行限制如下。目标宿主须在其配置或等价权限机制中实施这些约束；若无法实施，则不要执行依赖这些约束的自动化步骤。模型名称作为原宿主参考，不强制目标宿主使用不存在的模型。

```yaml
disable-model-invocation: false
allowed-tools: Bash
```

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项语义审核（2026-10-12）

- 审核状态：`reviewed-adapted`
- 检查与结论：完整读取正文及 host_matches 的 setup.sh；取消 CODEX_CLOUD、/sessions 推断与固定 Claude bridge 自动加载承诺，改为显式路径和已核验接收契约；定位 companion helper，检测 Bash/Python 能力。
- 正文/支持文件改动：`SKILL.md`、`scripts/setup.sh`。
- 剩余依赖：Python 3.10+、Bash 或等价 Python 执行能力、包安装权限；Mixpanel/mixpanel-headless、网络与用户账户授权；mixpanelyst auth_manager.py 或已安装 CLI 支持的等价认证检查；可选凭据桥必须有真实 receiver；MP_AUTH_BRIDGE_FILE 仅为本诊断脚本输入。
- 保留引用：Mixpanel、CodeMode、真实 mp CLI/SDK、~/.mp/config.toml 保留；~/.claude 路径仅作为原 Claude 集成条件性说明保留。
- 验证范围：已逐个完整读取 SKILL.md，并核对 export manifest 的 host_matches；正文无命中项也做语义检查。审核不代表外部服务已连接或产品任务已执行。
- 本地验证：桥接 Python 片段有效 v2、错误版本、错误形态、损坏 JSON、缺失文件 5 个合成用例均符合预期。未发现 Bash，未执行完整安装脚本、安装包或访问真实凭据。

## 上游资源旧链接修正（2026-10-12）

- 原 `mixpanelyst/references/analytical-frameworks.md` 与 `python-api.md` 不存在于下载的上游快照。
- 现已指向实际导出 sibling `x-openai-mixpanelyst-cd72fae/SKILL.md` 的 `Exploratory Analysis Workflow` 与 `mixpanel_headless API Reference`，并保留按 `scripts/help.py` 发现真实签名的要求。
- 已验证链接文件及章节存在；未运行 Mixpanel 查询、认证或安装流程。
