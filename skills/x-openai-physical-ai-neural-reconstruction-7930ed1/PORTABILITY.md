# 迁移记录

来源：`upstream/openai/plugins`

原名称：`physical-ai-neural-reconstruction`

原始副本位于导出包 `original-skills/x-openai-physical-ai-neural-reconstruction-7930ed1`，来源文件未修改。当前文件为独立副本。

原宿主元数据／执行限制如下。目标宿主须在其配置或等价权限机制中实施这些约束；若无法实施，则不要执行依赖这些约束的自动化步骤。模型名称作为原宿主参考，不强制目标宿主使用不存在的模型。

```yaml
version: 0.3.0
tools:
- Read
- Shell
```

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 跨宿主逐项复审（批次 7，2026-10-12）

- 结论：reviewed-unchanged。已静态复审 physical-ai-neural-reconstruction 的完整主文档及清单命中文件；保留任务方法、真实产品协议和原约束，未发现需要替换的当前 Codex 宿主硬绑定。
- 阅读证据：`SKILL.md` (295 行), `references/upstream-fetch.md` (57 行)；完整文件静态读取，清单命中逐项分类。
- 剩余依赖：NVIDIA/Physical AI 源仓库、重建依赖/GPU/数据及网络；.agents 等目录为多客户端发现候选。
- 保留的真实产品/API/URL：Codex、OpenAI、Claude Code、Claude、Cursor、Expo、Render、https://github.com/NVIDIA/asset-harvester''},、https://github.com/NVIDIA/harmonizer'',、https://github.com/NVIDIA/ncore''},、https://github.com/NVIDIA/nurec-skills、https://github.com/NVIDIA/nurec-skills'',、https://github.com/NVIDIA/nurec-skills.git、https://github.com/NVIDIA/nurec-skills/blob/main/.agents/skills/SKILL.md、https://huggingface.co/nvidia''},。
- 边界：只修改导出副本；未运行源技能工作流、连接/发布远程服务、执行付费操作或修改原始技能。在线与 UI 可用性尚未验证。
