# 迁移记录

来源：`upstream/openai/plugins`

原名称：`ios-simulator-browser`

原始副本位于导出包 `original-skills/x-openai-ios-simulator-browser-4a27c73`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项宿主审核（批次 0）

- 状态：`adapted`
- 结论：镜像与预览 URL 在任意可用本地浏览器打开；保留真实帧和热更新证据要求。
- 审阅文件：`SKILL.md`
- 实际依赖：macOS、Xcode Simulator、Node/npm、serve-sim；Swift package 与所需构建工具。
- 保留的产品/历史名称：iOS、SwiftUI、Xcode 为真实平台产品名。
- 验证范围：静态全文与宿主命中审核；未安装依赖、运行外部服务、执行硬件操作或验证账号连接。缺失能力不得宣称已完成。
- 资源解析：外部共享资源、相邻技能与插件根资源须按导出清单定位；路径不存在时先报告依赖缺失，不能把跨技能名称当成已安装证明。
