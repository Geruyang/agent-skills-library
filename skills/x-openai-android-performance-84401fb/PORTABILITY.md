# 迁移记录

来源：`upstream/openai/plugins`

原名称：`android-performance`

原始副本位于导出包 `original-skills/x-openai-android-performance-84401fb`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项宿主审核（批次 0）

- 状态：`adapted`
- 结论：将专属 Codex 命令会话表述改为当前宿主核验的持续命令机制，保留 Android 采样流程。
- 审阅文件：`SKILL.md`
- 实际依赖：adb 目标及可调试/profileable 应用、Android SDK/NDK；Simpleperf、Perfetto 或相应分析器。
- 保留的产品/历史名称：codex-android-perf 为可覆盖的临时目录前缀。
- 验证范围：静态全文与宿主命中审核；未安装依赖、运行外部服务、执行硬件操作或验证账号连接。缺失能力不得宣称已完成。
- 资源解析：外部共享资源、相邻技能与插件根资源须按导出清单定位；路径不存在时先报告依赖缺失，不能把跨技能名称当成已安装证明。
