# 迁移记录

来源：`upstream/openai/plugins`

原名称：`nvidia-skill-finder`

原始副本位于导出包 `original-skills/x-openai-nvidia-skill-finder-eba8c45`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐技能迁移审核（批2）

状态：`reviewed-unchanged`。

已检查，Codex只在与Claude并列的可选安装目标和基准资料中出现，保留真实产品命令。

运行依赖：NVIDIA在线技能目录；安装时需Node/npx和明确用户批准

保留产品提及：--agent codex、--agent claude-code为真实可选安装目标；基准表保留

检查范围：完整读取 SKILL.md，并读取清单命中的支持文件；扩展静态检查工具、路径与宿主引用。未执行这些技能、未进行服务登录或硬件/付费操作，不能据此声称端到端运行兼容。
