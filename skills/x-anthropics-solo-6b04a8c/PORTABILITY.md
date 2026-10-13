# 迁移记录

来源：`upstream/anthropics/claude-plugins-official`

原名称：`solo`

原始副本位于导出包 `original-skills/x-anthropics-solo-6b04a8c`，来源文件未修改。当前文件为独立副本。

原宿主元数据／执行限制如下。目标宿主须在其配置或等价权限机制中实施这些约束；若无法实施，则不要执行依赖这些约束的自动化步骤。模型名称作为原宿主参考，不强制目标宿主使用不存在的模型。

```yaml
argument-hint: '[DIR=run-directory] <problem statement | problem-file>'
disable-model-invocation: true
disallowed-tools: WebSearch, WebFetch, AskUserQuestion
allowed-tools: Read, Write, Edit, Glob, Grep, Bash(mkdir *), Bash(cp *), Bash(cmp
  *)
```

目标宿主能力和远程服务可用性不由安装文件保证；查阅导出包的 MCP 清单与审核记录。

## 逐技能跨宿主审核（2026-10-12）

- 状态：`adapted`。
- 范围：完整阅读本技能 `SKILL.md`；本项 manifest `host_matches` 为空，无自动命中的额外文件。按正文语义区分宿主调用与真实产品接口。
- 审核结论：Mapped invocation arguments and bounded file operations to current host; preserved solo pure-reasoning and durable-notes restrictions.
- 能力核验：这是静态移植审计；未安装依赖、未访问账号或硬件、未执行技能业务流程，不能据此声称目标环境可运行。
- 剩余依赖：
  - Writable local run directory
  - File read/write/copy/compare capabilities
  - No subagents, web research or mathematical code execution in this workflow
- 保留的真实产品/协议名称：Claude Code shortcut names as source examples。
- 缺失能力处理：按正文的已核验等价能力或本地交付路径执行；没有等价项时明确报告缺失，不伪造工具调用、远端状态或完成结果。
