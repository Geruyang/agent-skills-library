# 迁移记录

来源：`upstream/openai/plugins`

原名称：`brainstorming`

原始副本位于导出包 `original-skills/x-openai-brainstorming-8a528dc`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项宿主审核（批次 0）

- 状态：`adapted`
- 结论：浏览器伴随进程改为宿主能力发现；新增 BRAINSTORM_FOREGROUND 通用开关，保留历史环境检测兼容；修正本地资源定位。
- 审阅文件：`SKILL.md`、`scripts/start-server.sh`、`visual-companion.md`
- 实际依赖：Bash、Node.js、可持续命令会话和浏览器；visual companion 仍须用户原有审批。
- 保留的产品/历史名称：CODEX_CI 仅作可选旧环境检测；不是运行前提。
- 验证范围：静态全文与宿主命中审核；未安装依赖、运行外部服务、执行硬件操作或验证账号连接。缺失能力不得宣称已完成。
- 资源解析：外部共享资源、相邻技能与插件根资源须按导出清单定位；路径不存在时先报告依赖缺失，不能把跨技能名称当成已安装证明。
