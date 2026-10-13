# 迁移记录

来源：`upstream/openai/skills`

原名称：`define-goal`

原始副本位于导出包 `original-skills/x-openai-define-goal-e2d53a0`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项语义审核（批次4）

- 状态：`adapted`。
- 审核范围：完整读取 SKILL.md 及 4 个文本资源文件；复核清单 host_matches 并额外检查工具/路径假设。
- 结论：额外工具扫描发现无Codex字样的get_goal/create_goal硬绑定；改为真实能力发现，无能力输出目标文本并声明未创建。
- 仍需验证：可选宿主goal管理接口；不存在时只进行目标定义。
- 保留产品语义：get_goal/create_goal保留为实际发现时可用的原接口。
- 验证层级：静态适配审核；不代表已在目标宿主登录、连接服务或运行所有业务流程。
