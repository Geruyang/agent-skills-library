# 迁移记录

来源：`upstream/openai/plugins`

原名称：`subtitles`

原始副本位于导出包 `original-skills/x-openai-subtitles-bb9adc8`，来源文件未修改。当前文件为独立副本。

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 跨宿主逐项复审（2026-10-12）

- 结论：adapted。移除 Higgsfield/sandbox_exec 独占运行假设，改为能力预检与已授权本地/MCP/API；使用实际随包 scripts 路径，保留 Whisper 定时及隐私边界。
- 阅读范围：完整 SKILL.md；manifest 的 host_matches 为空，无该字段要求追加的文件。
- 额外核验：目录包含 audio_to_captions.py、subtitle_paper_burn.py、burn_caps_clean.sh；脚本头部/依赖检查确认命令入口，未运行转写或渲染。
- 剩余依赖：Python 3；FFmpeg/FFprobe；faster-whisper 或已授权 OpenAI STT；clean 需要 Bash/libass；paper/bold 需要 Pillow/NumPy 与覆盖字幕语言的字体；可选 finish_video.sh 未打包。
- 保留的真实产品/API/名称：Higgsfield (original optional runtime only)、Whisper、OpenAI STT、whisper-1、FFmpeg、faster-whisper、Pillow、NumPy。
- 验证边界：静态文档与文件检查；未登录远程服务、执行部署/写入、运行产品工作流或声称连接可用。名称保持导出唯一 ID。
