# 迁移记录

来源：`upstream/openai/plugins`

原名称：`narrator`

原始副本位于导出包 `original-skills/x-openai-narrator-685a86e`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 跨宿主逐项复审（批次 7，2026-10-12）

- 结论：adapted。去除 sandbox_exec/HF_WORKFLOWS 独占路径；映射实际随包 speech_metrics.sh 和可用命令/下载能力，保留 Higgsfield seed_audio 的声音身份、计时与有限重试契约。
- 阅读证据：`SKILL.md` (177 行)；完整文件静态读取，清单命中逐项分类。
- 剩余依赖：已授权 Higgsfield seed_audio/voice/job API；确切 voice_id+voice_type；二进制下载；Bash 与 FFmpeg/FFprobe 计时/合并；缺少能力不制造音频。
- 保留的真实产品/API/URL：OpenAI、Higgsfield、seed_audio。
- 边界：只修改导出副本；未运行源技能工作流、连接/发布远程服务、执行付费操作或修改原始技能。在线与 UI 可用性尚未验证。
