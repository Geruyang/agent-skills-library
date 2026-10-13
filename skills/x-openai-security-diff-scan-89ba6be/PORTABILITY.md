# 迁移记录

来源：`upstream/openai/plugins`

原名称：`security-diff-scan`

原始副本位于导出包 `original-skills/x-openai-security-diff-scan-89ba6be`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐技能迁移审核（批2）

状态：`adapted`。

限定工作台API分支，明确终端等价后端及依赖缺失处理，评论交付和技能调用改用宿主支持方式。

运行依赖：Codex Security MCP/workbench 或原插件CLI、共享扫描契约、Git仓库

保留产品提及：Codex Security真实API、CLI名称和scanId契约

检查范围：完整读取 SKILL.md，并读取清单命中的支持文件；扩展静态检查工具、路径与宿主引用。未执行这些技能、未进行服务登录或硬件/付费操作，不能据此声称端到端运行兼容。
