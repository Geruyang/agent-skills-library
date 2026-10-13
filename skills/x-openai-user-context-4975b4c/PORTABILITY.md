# 迁移记录

来源：`upstream/openai/plugins`

原名称：`user-context`

原始副本位于导出包 `original-skills/x-openai-user-context-4975b4c`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 本次逐项迁移审核（第 3 批）

- 结果：`adapted`。本地用户状态改为显式目录或环境变量；脚本仍兼容明确传入的历史 --codex-home；自动化使用实际调度能力且不臆称已创建。
- 审核入口与匹配资源：`SKILL.md`, `plugin-author-config/source-category-config.json`, `references/automation.md`, `references/plugin-memory.md`, `references/source-category-runtime.md`, `scripts/init_user_context_state.py`, `scripts/reset_user_context_state.py`, `scripts/state_paths.py`, `scripts/user_context_preflight.py`, `tests/test_state_helpers.py`。
- 仍需环境能力：Python 3；Explicit state directory；Optional authenticated connectors and host scheduler。
- 验证：显式状态目录初始化、只读 preflight、reset dry-run 通过。原完整测试存在上游历史布局依赖（未迁移 sibling 名称、shared 路径）及原始 marketplace ID 不一致，34 项测试中 7 项失败、20 项错误；这不作为运行兼容通过声明。
- 保留的真实产品或兼容字段：--codex-home explicit backward compatibility；Public Equity Investing。
