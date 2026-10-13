# 迁移记录

来源：`upstream/openai/skills`

原名称：`skill-installer`

原始副本位于导出包 `original-skills/x-openai-skill-installer-b36e203`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 本次逐项迁移审核（第 3 批）

- 结果：`adapted`。安装目标必须显式选择当前宿主技能目录；不再向 .codex 默认写入，保留网络、覆盖及认证边界。
- 审核入口与匹配资源：`SKILL.md`, `scripts/install-skill-from-github.py`, `scripts/list-skills.py`。
- 仍需环境能力：Python 3；GitHub network / optional Git credentials；Verified host skills directory。
- 验证：未配置目的目录时安装器阻止执行；未配置目录的清单不会误读另一宿主安装；未进行联网安装。
- 保留的真实产品或兼容字段：openai/skills；codex-skill-* HTTP client identifier。
