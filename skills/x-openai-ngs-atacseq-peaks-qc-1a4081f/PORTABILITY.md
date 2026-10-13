# 迁移记录

来源：`upstream/openai/plugins`

原名称：`ngs-atacseq-peaks-qc`

原始副本位于导出包 `original-skills/x-openai-ngs-atacseq-peaks-qc-1a4081f`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项语义审核（批次 2，尾段）

- 审核状态：`adapted`。
- 审核范围：完整 SKILL.md；manifest host_matches 为零，另检查相关工具名/宿主路径及命中的支持文件。
- 结论：明确独立包缺失ngs-analysis共享runner，执行受依赖检查约束。
- 保留依赖：ngs-analysis共享runner；nf-core/Nextflow或ATAC工具链；参考基因组。
- 保留产品名称：nf-core、MACS2、HOMER。
- TRAE / Claude 执行约束：先发现实际可用的工具、权限和依赖；缺失的执行能力明确报告阻塞。本文审核不代表已连接服务、安装运行时或完成外部操作。
