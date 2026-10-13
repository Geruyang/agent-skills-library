# 迁移记录

来源：`upstream/openai/plugins`

原名称：`shadcn`

原始副本位于导出包 `original-skills/x-openai-shadcn-d513686`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。
## 逐项语义审核（第5批）

- 审核状态：`reviewed-unchanged`。
- 审核范围：完整读取 `SKILL.md` 与 12 个可读文本文件；复核 1 条原清单宿主匹配。
- 结论：MCP文档里的Codex路径属于多编辑器对照表中的专门配置示例，保留；主要CLI工作流无当前宿主绑定。
- 剩余依赖：Node.js/shadcn CLI；Optional configured shadcn MCP。
- 保留产品语义：Codex config-table row, alongside Cursor/VS Code/OpenCode。
- 验证边界：静态迁移审核；未执行技能业务、登录外部账户或在TRAE/Claude中实跑。当前宿主能力不足时须报告真实阻塞，不能虚构调用或完成状态。
