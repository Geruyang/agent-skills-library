# 迁移记录

来源：`upstream/openai/skills`

原名称：`hatch-pet`

原始副本位于导出包 `original-skills/x-openai-hatch-pet-62f7133`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。
## 逐项语义审核（第5批）

- 审核状态：`adapted`。
- 审核范围：完整读取 `SKILL.md` 与 15 个可读文本文件；复核 41 条原清单宿主匹配。
- 结论：保留Codex宠物atlas/manifest目标；图像技能与执行脚本按实际安装发现，生成暂存与宠物包在项目内交付，安装目标产品仅在明确授权且路径存在时进行。
- 剩余依赖：Image generation skill/service with reference-image support；Python image libraries and jq/Bash or equivalent shell operations；Subagent and visual review capability; missing capability blocks relevant steps；Codex app only for final pet installation/use。
- 保留产品语义：Codex pet product and 8×9 sprite contract；Optional actual Codex installation path in codex-pet-contract.md。
- 验证边界：静态迁移审核；未执行技能业务、登录外部账户或在TRAE/Claude中实跑。当前宿主能力不足时须报告真实阻塞，不能虚构调用或完成状态。
