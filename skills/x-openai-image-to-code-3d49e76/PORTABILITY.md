# 迁移记录

来源：`upstream/openai/plugins`

原名称：`image-to-code`

原始副本位于导出包 `original-skills/x-openai-image-to-code-3d49e76`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。
## 逐项语义审核（第5批）

- 审核状态：`adapted`。
- 审核范围：完整读取 `SKILL.md` 与 3 个可读文本文件；复核 1 条原清单宿主匹配。
- 结论：预览地址和图像工具按实际宿主运行时发现；保留明确ChatGPT Work专用步骤作为条件分支，TRAE/Claude使用真实本地开发服务器。
- 剩余依赖：Image generation and image inspection；Frontend runtime and browser automation；Sites only for explicitly requested deployment。
- 保留产品语义：。
- 验证边界：静态迁移审核；未执行技能业务、登录外部账户或在TRAE/Claude中实跑。当前宿主能力不足时须报告真实阻塞，不能虚构调用或完成状态。
