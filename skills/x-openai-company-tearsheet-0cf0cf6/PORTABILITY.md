# 迁移记录

来源：`upstream/openai/plugins`

原名称：`company-tearsheet`

原始副本位于导出包 `original-skills/x-openai-company-tearsheet-0cf0cf6`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项语义审核（2026-10-12）

- 审核状态：`reviewed-adapted`
- 检查与结论：完整读取正文及 manifest 命中；原固定 request_user_input 改为实际结构化询问或聊天，特定 in-app Browser 排除改为可访问本地文件的真实浏览器能力；外部契约缺失明确阻塞。
- 正文/支持文件改动：`SKILL.md`。
- 剩余依赖：Public Equity Investing router 与 shared runtime/intake/HTML 契约需要实际安装并定位；市场数据、披露资料与相应授权；HTML QA 需要浏览器；Python 用于可选本地 helpers。
- 保留引用：Public Equity Investing、issuer/HTML dashboard schema 和真实投资研究产品引用保留。
- 验证范围：已逐个完整读取 SKILL.md，并核对 export manifest 的 host_matches；正文无命中项也做语义检查。审核不代表外部服务已连接或产品任务已执行。
