# 迁移记录

来源：`upstream/openai/plugins`

原名称：`public-equity-investing`

原始副本位于导出包 `original-skills/x-openai-public-equity-investing-0bdc3f2`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项宿主审核（批次 0）

- 状态：`adapted`
- 结论：将固定提问/安装工具与 picker 参数改为实际宿主的已发现能力；保留财务路由、来源验证和用户授权要求。
- 审阅文件：`SKILL.md`、`internal-support/dashboard-builder/INTERNAL.md`、`internal-support/excel-data-cleaner/INTERNAL.md`、`internal-support/financial-source-of-truth/INTERNAL.md`、`internal-support/sector-context-overlay/INTERNAL.md`、`internal-support/style-guide-adapter/INTERNAL.md`
- 实际依赖：Public Equity Investing 共享策略、相邻技能与 .app.json；相关市场/财报数据源或用户导出；按输出需要的渲染运行时。
- 保留的产品/历史名称：Public Equity Investing、Daloopa、Quartr 及其他供应商名称为产品/数据来源。
- 验证范围：静态全文与宿主命中审核；未安装依赖、运行外部服务、执行硬件操作或验证账号连接。缺失能力不得宣称已完成。
- 资源解析：外部共享资源、相邻技能与插件根资源须按导出清单定位；路径不存在时先报告依赖缺失，不能把跨技能名称当成已安装证明。
