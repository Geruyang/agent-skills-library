# 迁移记录

来源：`upstream/openai/plugins`

原名称：`scrna-seq-qc`

原始副本位于导出包 `original-skills/x-openai-scrna-seq-qc-715241a`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项宿主审核（批次 0）

- 状态：`adapted`
- 结论：description 去掉 Codex 宿主限制，科学方法及禁止静默更换算法的规则保持。
- 审阅文件：`SKILL.md`
- 实际依赖：Python/R 与 Scanpy/AnnData/scDblFinder 等分析包、原始数据和物种参考；插件级 run_scrnaseq_post_count_qc.py 需解析其真实路径。
- 保留的产品/历史名称：无需特殊保留的 Codex 产品引用。
- 验证范围：静态全文与宿主命中审核；未安装依赖、运行外部服务、执行硬件操作或验证账号连接。缺失能力不得宣称已完成。
- 资源解析：外部共享资源、相邻技能与插件根资源须按导出清单定位；路径不存在时先报告依赖缺失，不能把跨技能名称当成已安装证明。
