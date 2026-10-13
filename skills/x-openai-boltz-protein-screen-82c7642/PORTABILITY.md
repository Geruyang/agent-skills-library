# 迁移记录

来源：`upstream/openai/plugins`

原名称：`boltz-protein-screen`

原始副本位于导出包 `original-skills/x-openai-boltz-protein-screen-82c7642`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐技能迁移审核（批2）

状态：`adapted`。

后台下载与监控改为当前宿主真实会话/调度能力，缺失时交付状态命令，保留费用确认。

运行依赖：boltz-api CLI、Boltz认证、网络、费用明确批准；自动监控需支持且获授权

保留产品提及：Boltz真实API和CLI保持

检查范围：完整读取 SKILL.md，并读取清单命中的支持文件；扩展静态检查工具、路径与宿主引用。未执行这些技能、未进行服务登录或硬件/付费操作，不能据此声称端到端运行兼容。
