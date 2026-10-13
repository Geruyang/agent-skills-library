# 迁移记录

来源：`upstream/openai/plugins`

原名称：`define-security-policy`

原始副本位于导出包 `original-skills/x-openai-define-security-policy-36e2478`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐技能迁移审核（批2）

状态：`adapted`。

核心策略指导通用化；产品resolver为可选后端，普通文件工具可做同等有界策略链检查。

运行依赖：仓库读写权限；共享安全指导文档；使用产品resolver时需Codex Security插件

保留产品提及：Codex Security resolver真实命令与插件定位格式

检查范围：完整读取 SKILL.md，并读取清单命中的支持文件；扩展静态检查工具、路径与宿主引用。未执行这些技能、未进行服务登录或硬件/付费操作，不能据此声称端到端运行兼容。
