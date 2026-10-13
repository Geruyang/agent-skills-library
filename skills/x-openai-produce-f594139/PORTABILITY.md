# 迁移记录

来源：`upstream/openai/plugins`

原名称：`produce`

原始副本位于导出包 `original-skills/x-openai-produce-f594139`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项语义审核（批次4）

- 状态：`adapted`。
- 审核范围：完整读取 SKILL.md 及 55 个文本资源文件；复核清单 host_matches 并额外检查工具/路径假设。
- 结论：正文改为探测MCP board与图像能力；无UI提供现有本地review产物、无代理串行；两个helper兼容独立技能缺插件manifest。
- 仍需验证：图像生成工具/API；Creative Production MCP用于live board，缺失时本地交付；本地Python与浏览器用于review helper。
- 保留产品语义：Creative Production MCP、openai/widgetSessionId协议、.codex-plugin可选版本元数据。
- 验证层级：静态适配审核；不代表已在目标宿主登录、连接服务或运行所有业务流程。
