# 迁移记录

来源：`upstream/openai/plugins`

原名称：`kpi-reporting`

原始副本位于导出包 `original-skills/x-openai-kpi-reporting-52b00a6`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 跨宿主逐项复审（2026-10-12）

- 结论：adapted。将源类别占位符与 companion skill 名称改为发现后路由；缺少报告/Google Slides 能力时交付本地报告或 deck 并明确云端未创建。
- 阅读范围：完整 SKILL.md；manifest 的 host_matches 为空，无该字段要求追加的文件。
- 剩余依赖：权威 KPI 数据源及访问权限；指标/报告/图表技能角色需在宿主目录中解析；本地报告写入能力，云交付另需真实连接。
- 保留的真实产品/API/名称：WBR、MBR、QBR、Google Slides。
- 验证边界：静态文档与文件检查；未登录远程服务、执行部署/写入、运行产品工作流或声称连接可用。名称保持导出唯一 ID。
