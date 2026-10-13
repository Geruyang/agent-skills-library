# 迁移记录

来源：`upstream/anthropics/claude-plugins-official`

原名称：`claude-security`

原始副本位于导出包 `original-skills/x-anthropics-claude-security-4f1abe6`，来源文件未修改。当前文件为独立副本。

原宿主元数据／执行限制如下。目标宿主须在其配置或等价权限机制中实施这些约束；若无法实施，则不要执行依赖这些约束的自动化步骤。模型名称作为原宿主参考，不强制目标宿主使用不存在的模型。

```yaml
allowed-tools:
- Read
- Write
- Edit
- Glob
- Grep
- AskUserQuestion
- Workflow
- Workflow(claude-security:scan)
- Agent(claude-security:scan-inventory, claude-security:scan-researcher, claude-security:scan-verifier,
  claude-security:scan-loader, claude-security:scan-redactor, claude-security:patch-generator,
  claude-security:patch-verifier, claude-security:explore)
- Bash(date *)
- Bash(ls *)
- Bash(wc *)
- Bash(mkdir -p *)
- Bash(git *)
- Bash(GIT_CONFIG_GLOBAL=/dev/null GIT_TERMINAL_PROMPT=0 git *)
- Bash(find . -maxdepth 1 -type d -name "CLAUDE-SECURITY-2*")
- Bash(python3 "${CLAUDE_PLUGIN_ROOT}/scripts/render_report.py" *)
- Bash(python3 "${CLAUDE_PLUGIN_ROOT}/scripts/save_result.py" *)
- Bash(python3 "${CLAUDE_PLUGIN_ROOT}/scripts/write_scan_meta.py" *)
- Bash(bash "${CLAUDE_PLUGIN_ROOT}/scripts/keep-waiting.sh" *)
- Bash(python3 "${CLAUDE_PLUGIN_ROOT}/scripts/patch_artifacts.py" *)
- Bash(sleep *)
- Bash(GIT_TERMINAL_PROMPT=0 git *)
```

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐技能跨宿主审核（2026-10-12）

- 状态：`adapted`。
- 范围：完整阅读本技能 `SKILL.md`；本项 manifest `host_matches` 为空，无自动命中的额外文件。按正文语义区分宿主调用与真实产品接口。
- 审核结论：Added an upfront product-capability gate, real path resolution and explicit unsupported-host outcome; removed automatic command/include expansion and mandatory irrelevant auto-mode message.
- 能力核验：这是静态移植审计；未安装依赖、未访问账号或硬件、未执行技能业务流程，不能据此声称目标环境可运行。
- 剩余依赖：
  - Full Claude Security plugin workflow and agent definitions (not in exported skill)
  - Plugin-root helper scripts (not in exported skill)
  - Compatible Workflow execution and verified-result contract
  - Question/consent UI, Git, Python and shell for native jobs
- 保留的真实产品/协议名称：Claude Security；claude-security:scan；Claude Code optional auto-mode controls；CLAUDE.md；sandbox-runtime repository URL。
- 缺失能力处理：按正文的已核验等价能力或本地交付路径执行；没有等价项时明确报告缺失，不伪造工具调用、远端状态或完成结果。
