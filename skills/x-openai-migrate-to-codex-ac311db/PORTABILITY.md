# 迁移记录

来源：`upstream/openai/skills`

原名称：`migrate-to-codex`

原始副本位于导出包 `original-skills/x-openai-migrate-to-codex-ac311db`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项宿主审核（批次 0）

- 状态：`adapted`
- 结论：保留迁移到 Codex 的产品目标、配置字段和转换脚本；将当前执行者的固定 TODO 接口与脚本安装位置改为宿主可用能力和本技能路径。
- 审阅文件：`SKILL.md`、`agents/openai.yaml`、`references/differences.md`、`scripts/cli.py`、`scripts/migrate/__init__.py`、`scripts/migrate/agents.py`、`scripts/migrate/codex_config.py`、`scripts/migrate/common.py`、`scripts/migrate/hooks.py`、`scripts/migrate/instructions.py`、`scripts/migrate/mcps.py`、`scripts/migrate/plugins.py`、`scripts/migrate/skills.py`
- 实际依赖：Python 3 及脚本声明的依赖；被用户选定的 Claude 源目录与 Codex 目标目录；目标产品规则运行前需复核。
- 保留的产品/历史名称：Codex 产品名、.codex 配置路径与生成器 API/字段均为真实迁移目标，不是执行宿主要求。
- 验证范围：静态全文与宿主命中审核；未安装依赖、运行外部服务、执行硬件操作或验证账号连接。缺失能力不得宣称已完成。
- 资源解析：外部共享资源、相邻技能与插件根资源须按导出清单定位；路径不存在时先报告依赖缺失，不能把跨技能名称当成已安装证明。
