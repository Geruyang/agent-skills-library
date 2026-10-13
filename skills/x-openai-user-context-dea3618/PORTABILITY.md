# 迁移记录

来源：`upstream/openai/plugins`

原名称：`user-context`

原始副本位于导出包 `original-skills/x-openai-user-context-dea3618`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项语义审核

- 状态：`reviewed-adapted`。已完整读取 SKILL.md，并检查清单命中的支持文件；未执行源文指令。
- 结论：将 Codex 私有状态路径改为显式 --state-dir / PRODUCT_DESIGN_STATE_DIR，默认仅落当前项目 .agent-skills；保留保存前可写验证与禁止保存秘密的边界，并标明完整插件路由依赖。
- 仍需能力／依赖：Python；稳定可写的状态目录；未来会话必须使用同一目录；插件级路由需要单独安装完整 Product Design 插件。
- 保留的产品／历史引用：ChatGPT 仅为示例图片文件名；--codex-home 为旧显式 CLI 参数别名
- 验证边界：这是静态语义与资源审查，不表示已在 TRAE 或 Claude 中完成远程服务认证或端到端实跑。
