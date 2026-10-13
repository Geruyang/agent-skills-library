# 迁移记录

来源：`upstream/openai/plugins`

原名称：`event-driven-analyzer`

原始副本位于导出包 `original-skills/x-openai-event-driven-analyzer-4300999`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项语义审核（2026-10-12）

- 审核状态：`reviewed-adapted`
- 检查与结论：完整读取正文及 manifest 命中；把 request_user_input 和原 sibling/shared 布局假设改为宿主工具探测、真实目录定位与依赖阻塞，保留事件分析及子工作流。
- 正文/支持文件改动：`SKILL.md`。
- 剩余依赖：Public Equity Investing router 与 shared runtime/intake/HTML 契约；事件披露、时间戳行情及可选研究来源；Python event_math helper；HTML 视觉检查能力。
- 保留引用：Public Equity Investing、Credit Markets、SEC 表单和市场/API schema 引用保留。
- 验证范围：已逐个完整读取 SKILL.md，并核对 export manifest 的 host_matches；正文无命中项也做语义检查。审核不代表外部服务已连接或产品任务已执行。
