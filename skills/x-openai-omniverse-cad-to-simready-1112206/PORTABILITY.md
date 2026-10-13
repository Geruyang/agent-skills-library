# 迁移记录

来源：`upstream/openai/plugins`

原名称：`omniverse-cad-to-simready`

原始副本位于导出包 `original-skills/x-openai-omniverse-cad-to-simready-1112206`，来源文件未修改。当前文件为独立副本。

原宿主元数据／执行限制如下。目标宿主须在其配置或等价权限机制中实施这些约束；若无法实施，则不要执行依赖这些约束的自动化步骤。模型名称作为原宿主参考，不强制目标宿主使用不存在的模型。

```yaml
version: 0.1.0
tools:
- Read
- Shell
```

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 本次逐项迁移审核（第 3 批）

- 结果：`adapted`。上游 version/tools 顶层格式改为历史说明，导出元数据保留在 PORTABILITY.md；NVIDIA 上游真实 .codex/skills 路径、发布别名和查找候选保持原意。
- 审核入口与匹配资源：`SKILL.md`, `references/content-agents/references/material-agent-client/README.md`, `references/content-agents/references/physics-agent-client/README.md`, `references/content-agents/references/texture-agent-client/README.md`, `references/deploy-content-agents/README.md`, `references/deploy-content-agents/references/deploy-material-agent-docker.md`, `references/deploy-content-agents/references/deploy-ovrtx-docker.md`, `references/deploy-content-agents/references/deploy-physics-agent-docker.md`, `references/deploy-content-agents/references/deploy-texture-agent-docker.md`, `references/ovrtx-render-service/README.md`, `references/preflight/scripts/preflight.py`。
- 仍需环境能力：Linux/macOS；Python 3.12 / uv；NVIDIA GPU / Docker / Container Toolkit；Content Agents upstream and authenticated services。
- 保留的真实产品或兼容字段：NVIDIA Omniverse；Upstream .codex/skills repository layout；Optional .claude/skills discovery alias。
