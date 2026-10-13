# 迁移记录

来源：`upstream/openai/plugins`

原名称：`create-data-context`

原始副本位于导出包 `original-skills/x-openai-create-data-context-d5643af`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项语义审核

- 状态：`reviewed-adapted`。已完整读取 SKILL.md，并检查清单命中的支持文件；未执行源文指令。
- 结论：将语义层安装目录、脚本状态根和自动化机制改为可发现宿主能力；修复独立导出后的 source-category-config 相对路径。保留明确授权、专用任务与回读验证门槛。
- 仍需能力／依赖：Python；来源连接器认证；本地技能发现；可选调度器必须支持持久化、独立任务身份和回读。；完整插件级历史测试仍依赖原插件布局，不能等同于独立技能运行验收。
- 保留的产品／历史引用：ChatGPT personal Skills 是独立真实产品分支；--codex-home 仅保留为显式传入的旧 CLI 参数别名，不再默认读取 Codex 目录
- 验证边界：这是静态语义与资源审查，不表示已在 TRAE 或 Claude 中完成远程服务认证或端到端实跑。
