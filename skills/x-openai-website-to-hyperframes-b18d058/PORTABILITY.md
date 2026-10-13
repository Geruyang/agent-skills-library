# 迁移记录

来源：`upstream/openai/plugins`

原名称：`website-to-hyperframes`

原始副本位于导出包 `original-skills/x-openai-website-to-hyperframes-b18d058`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐项宿主审核（批次 0）

- 状态：`adapted`
- 结论：全文与验证参考已检查；语音参考的固定 MCP 标识改为真实连接器能力发现与本地 Kokoro 路线；codex-openai-video 仅是示例项目名，保留。
- 审阅文件：`SKILL.md`、`references/step-5-vo.md`、`references/step-7-validate.md`
- 实际依赖：HyperFrames CLI、Node/npm、浏览器、TTS/转写依赖；相邻 hyperframes 技能。
- 保留的产品/历史名称：HyperFrames、ElevenLabs、HeyGen；codex-openai-video 为示例目录名。
- 验证范围：静态全文与宿主命中审核；未安装依赖、运行外部服务、执行硬件操作或验证账号连接。缺失能力不得宣称已完成。
- 资源解析：外部共享资源、相邻技能与插件根资源须按导出清单定位；路径不存在时先报告依赖缺失，不能把跨技能名称当成已安装证明。
