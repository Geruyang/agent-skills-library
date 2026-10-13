# 迁移记录

来源：`upstream/openai/plugins`

原名称：`portfolio-risk-management`

原始副本位于导出包 `original-skills/x-openai-portfolio-risk-management-e45bdc5`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项语义审核（2026-10-12）

- 审核状态：`reviewed-adapted`
- 检查与结论：完整读取正文及 manifest 命中；改写宿主提问工具、特定浏览器与原共享资源布局绑定，缺少必要契约或视觉能力时明确受阻，保留风险输出结构。
- 正文/支持文件改动：`SKILL.md`。
- 剩余依赖：Public Equity Investing router 与 shared 风险、intake、HTML 契约；投资组合数据及授权市场数据；Python 计算脚本；可访问本地 HTML 的浏览器能力。
- 保留引用：Public Equity Investing、Credit Markets、ETF/CDS 等产品及专业术语保留。
- 验证范围：已逐个完整读取 SKILL.md，并核对 export manifest 的 host_matches；正文无命中项也做语义检查。审核不代表外部服务已连接或产品任务已执行。
