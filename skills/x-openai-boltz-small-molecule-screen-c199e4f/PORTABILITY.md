# 迁移记录

来源：`upstream/openai/plugins`

原名称：`boltz-small-molecule-screen`

原始副本位于导出包 `original-skills/x-openai-boltz-small-molecule-screen-c199e4f`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项宿主审核（批次 0）

- 状态：`adapted`
- 结论：将 Codex 固定 shell 参数、轮询接口和 heartbeat 指令改为已核验的长任务会话/调度能力；保留费用显式确认与 Boltz CLI/API 参数。
- 审阅文件：`SKILL.md`
- 实际依赖：Boltz CLI、账户认证与网络；长期进程支持；自动后续检查另需宿主调度能力，否则只能手动查询状态。
- 保留的产品/历史名称：Boltz 产品/API 与 Claude Code 权限宿主举例保留。
- 验证范围：静态全文与宿主命中审核；未安装依赖、运行外部服务、执行硬件操作或验证账号连接。缺失能力不得宣称已完成。
- 资源解析：外部共享资源、相邻技能与插件根资源须按导出清单定位；路径不存在时先报告依赖缺失，不能把跨技能名称当成已安装证明。
