# 迁移记录

来源：`upstream/anthropics/claude-plugins-official`

原名称：`cardputer-buddy`

原始副本位于导出包 `original-skills/x-anthropics-cardputer-buddy-abea3bc`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项语义审核（2026-10-12）

- 状态：`reviewed-unchanged`
- 检查范围：完整 `SKILL.md`；manifest `host_matches` 为空。
- 结论：设备布局、源码目录及Claude Buddy都是目标项目约定，非执行宿主假设。
- 尚需能力/资源：用户build-with-claude源码及buddy/onboard脚本；Cardputer-Adv、Python、串口。
- 保留产品引用：Claude Buddy、Claude Desktop Hardware Buddy；MicroPython、UIFlow、m5-onboard。
- 文件清单：`PORTABILITY.md`、`PORTABILITY_REVIEW.json`。
