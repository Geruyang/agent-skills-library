# 迁移记录

来源：`upstream/openai/plugins`

原名称：`track-findings`

原始副本位于导出包 `original-skills/x-openai-track-findings-e6c94d7`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项语义审核

- 状态：`reviewed-adapted`。已完整读取 SKILL.md，并检查清单命中的支持文件；未执行源文指令。
- 结论：Codex Security是扫描来源产品，保留名称与封存契约；将私有app://连接入口改为宿主实际连接器发现；把验证器依赖及schemas按相对路径补入技能，保留逐项预览授权与账户/受众回验。
- 仍需能力／依赖：封存Codex Security扫描包；Python；已授权Linear/Jira/GitHub连接器，或用户明确选择的gh账号；advisory仍只允许既定gh流程。
- 保留的产品／历史引用：Codex Security产品、schema和模块命名必须保留以验证原扫描契约
- 验证边界：这是静态语义与资源审查，不表示已在 TRAE 或 Claude 中完成远程服务认证或端到端实跑。
