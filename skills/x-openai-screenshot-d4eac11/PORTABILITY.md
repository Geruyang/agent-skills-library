# 迁移记录

来源：`upstream/openai/skills`

原名称：`screenshot`

原始副本位于导出包 `original-skills/x-openai-screenshot-d4eac11`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项语义审核（批次4）

- 状态：`adapted`。
- 审核范围：完整读取 SKILL.md 及 11 个文本资源文件；复核清单 host_matches 并额外检查工具/路径假设。
- 结论：截图当前执行者和目标示例通用化；保留OS权限流程、已有沙箱检测与测试环境变量，拒绝无授权绕过。
- 仍需验证：OS屏幕录制权限、Python/PowerShell及平台截图工具。
- 保留产品语义：CODEX_SANDBOX兼容检测与CODEX_SCREENSHOT_TEST_*测试变量；codex-shot/cache仅已有文件名。
- 验证层级：静态适配审核；不代表已在目标宿主登录、连接服务或运行所有业务流程。
