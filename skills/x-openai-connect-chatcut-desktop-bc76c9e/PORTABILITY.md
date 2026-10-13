# 迁移记录

来源：`upstream/openai/plugins`

原名称：`connect-chatcut-desktop`

原始副本位于导出包 `original-skills/x-openai-connect-chatcut-desktop-bc76c9e`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐技能迁移审核（批2）

状态：`adapted`。

保留ChatCut管理的Codex集成说明，并将当前宿主连接与重载改为验证后的行为。

运行依赖：签名ChatCut Desktop、受支持OS、官方MCP连接、用户登录

保留产品提及：ChatCut内置Codex agent和自动同步为真实产品行为，未改名

检查范围：完整读取 SKILL.md，并读取清单命中的支持文件；扩展静态检查工具、路径与宿主引用。未执行这些技能、未进行服务登录或硬件/付费操作，不能据此声称端到端运行兼容。
