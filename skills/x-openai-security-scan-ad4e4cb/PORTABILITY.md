# 迁移记录

来源：`upstream/openai/plugins`

原名称：`security-scan`

原始副本位于导出包 `original-skills/x-openai-security-scan-ad4e4cb`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。
## 逐项语义审核（第5批）

- 审核状态：`adapted`。
- 审核范围：完整读取 `SKILL.md` 与 5 个可读文本文件；复核 21 条原清单宿主匹配。
- 结论：Security产品协议保留；桌面路径只适用于明确Codex桌面，外部宿主走已有headless模式并检查完整插件/脚本是否随迁移可用。
- 剩余依赖：Codex Security plugin schemas/shared references/helper scripts；Python and repository read access；Optional actual Codex Security host tools; offline headless path otherwise。
- 保留产品语义：CODEX_SECURITY_* protocol variables, scan tools and canonical Security report format。
- 验证边界：静态迁移审核；未执行技能业务、登录外部账户或在TRAE/Claude中实跑。当前宿主能力不足时须报告真实阻塞，不能虚构调用或完成状态。
