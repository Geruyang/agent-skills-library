# 迁移记录

来源：`upstream/openai/plugins`

原名称：`agent-browser-verify`

原始副本位于导出包 `original-skills/x-openai-agent-browser-verify-d0bc25d`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项语义审核（2026-10-12）

- 审核状态：`reviewed-adapted`
- 检查与结论：完整读取正文及 manifest 命中；保留 agent-browser 产品命令，正文增加 CLI/真实等价浏览器能力检查、实际服务器 URL 和产物目录解析、不可验证状态；禁止未采集 console 即宣称无错误。
- 正文/支持文件改动：`SKILL.md`。
- 剩余依赖：agent-browser CLI 或具备导航/截图/DOM/console 能力的真实浏览器 MCP/API/库；可达开发服务器；Vercel/Workflow 日志仅在对应后端存在时使用。
- 保留引用：metadata 的 Introducing Codex URL 为来源引用，保留；agent-browser、Vercel、Next.js、Vite、Workflow DevKit 是真实产品。
- 验证范围：已逐个完整读取 SKILL.md，并核对 export manifest 的 host_matches；正文无命中项也做语义检查。审核不代表外部服务已连接或产品任务已执行。
