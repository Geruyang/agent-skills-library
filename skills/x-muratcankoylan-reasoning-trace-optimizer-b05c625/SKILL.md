---
name: x-muratcankoylan-reasoning-trace-optimizer-b05c625
description: Debug and optimize AI agents by analyzing reasoning traces, context degradation, tool confusion, instruction drift, repeated task failures, and performance regressions.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Reasoning Trace Optimizer

Debug and optimize AI agents by analyzing their reasoning traces. This skill uses MiniMax M2.1's interleaved thinking to provide deep insight into agent decision-making and generate concrete improvements.

## When to Activate

- Agent reasoning traces need debugging, analysis, or prompt optimization
- Agent task fails and user wants to understand why
- User mentions "context degradation", "tool confusion", or "instruction drift"
- Request to improve agent performance or reduce errors
- User wants to generate shareable learnings from debugging sessions
- After repeated failures on similar tasks

## Core Concepts

### Interleaved Thinking

Unlike standard reasoning models that think once at the start, interleaved thinking allows reasoning BETWEEN each tool interaction. This is critical because:

1. **Long-horizon tasks** require maintaining focus across many turns
2. **External perturbations** (tool outputs, environment changes) need real-time adaptation
3. **Debugging** requires seeing HOW decisions were made, not just WHAT was output

### The Optimization Loop

```
Execute Agent → Capture Traces → Analyze Patterns → Optimize Prompt → Re-run
                                                          ↑____________|
```

Each iteration improves the prompt based on detected patterns until convergence.

### Pattern Detection

Common failure patterns the analyzer detects:

| Pattern | Description |
|---------|-------------|
| `context_degradation` | Model loses track of information over long contexts |
| `tool_confusion` | Model misunderstands tool capabilities or outputs |
| `instruction_drift` | Model gradually deviates from original instructions |
| `goal_abandonment` | Model stops pursuing the original goal |
| `circular_reasoning` | Model repeats similar actions without progress |
| `premature_conclusion` | Model concludes before completing the task |

## Usage Modes

### Mode 1: M2.1 Agent Debugging

Run a task through M2.1 and analyze its reasoning:

```python
from reasoning_trace_optimizer import TraceCapture, TraceAnalyzer

capture = TraceCapture()
trace = capture.run(
    task="Search for Python tutorials and summarize them",
    system_prompt="You are a research assistant.",
    tools=[search_tool],
    tool_executor=execute_search
)

analyzer = TraceAnalyzer()
analysis = analyzer.analyze(trace)

print(f"Score: {analysis.overall_score}/100")
for pattern in analysis.patterns:
    print(f"Found: {pattern.type.value} - {pattern.suggestion}")
```

### Mode 2: Full Optimization Loop

Automatically iterate until the prompt is optimized:

```python
from reasoning_trace_optimizer import OptimizationLoop, LoopConfig

config = LoopConfig(
    max_iterations=5,
    min_score_threshold=80.0,
)

loop = OptimizationLoop(config=config)
result = loop.run(
    task="Analyze this codebase and suggest improvements",
    initial_prompt="You are a code reviewer.",
    tools=[read_file_tool, search_tool],
    tool_executor=execute_tool
)

print(f"Improved: {result.initial_score} → {result.final_score}")
print(f"Final prompt:\n{result.final_prompt}")
```

### Mode 3: Universal Session Analysis

Analyze user-provided or explicitly exported agent traces with a supported parser. Discover which trace/log export the current host exposes; do not assume access to current-session private thinking or hidden reasoning. Prefer observable tool calls, errors, user-visible summaries, and results. If no authorized trace export exists, report session-trace analysis as blocked and accept a supplied log instead. Skill slash commands are optional host shortcuts, not guaranteed executables.

### Mode 4: Generate Shareable Skills

Convert optimization learnings into reusable Agent Skills:

```python
from reasoning_trace_optimizer import SkillGenerator

generator = SkillGenerator()
skill_path = generator.generate(
    result=loop_result,
    skill_name="web-search-best-practices",
    output_dir="./skills"
)
```

## CLI Commands

```bash
# Capture reasoning trace
rto capture "Search for Python tutorials" -s "You are a helpful assistant."

# Analyze a task
rto analyze "Debug this code" -o analysis.txt

# Run optimization loop
rto optimize "Research AI papers" --max-iterations 5 --generate-skill

# Generate skill from artifacts
rto generate-skill my-skill-name --artifacts-dir ./optimization_artifacts
```

## Host Integration (TRAE / Claude)

Discover the current host's supported log export and hook configuration, and inspect `rto --help` before wiring any command. This package does not itself guarantee a current-session reader or an `analyze-session` CLI subcommand. Only configure a documented hook against a command that exists; otherwise keep analysis manual using supplied trace files.

For on-demand analysis:
1. Read an authorized exported trace or user-provided log.
2. Identify observable failure patterns and evidence.
3. Propose prompt improvements for the user's agent project.
4. Save changes only to an explicitly authorized project configuration; do not claim to update the running host's hidden system prompt.

## Guidelines

1. **Preserve full context**: M2.1 requires full response history including thinking blocks for optimal performance
2. **Use appropriate tools**: Define tools clearly with unambiguous descriptions
3. **Set realistic convergence thresholds**: 5-10% improvement per iteration is typical
4. **Review generated skills**: Auto-generated skills should be reviewed before sharing
5. **Monitor token usage**: Each optimization iteration uses significant tokens

## Examples

### Before Optimization

```
System: You are a helpful assistant.

Issue: Agent called wrong tools, lost track of goal after 3 turns
Score: 45/100
Patterns: tool_confusion, goal_abandonment
```

### After Optimization

```
System: You are a research assistant focused on finding accurate information.

IMPORTANT GUIDELINES:
- Always verify search results before summarizing
- If a tool returns an error, try an alternative approach
- Keep track of your original goal throughout the task
- Validate findings against multiple sources when possible

Issue: None
Score: 85/100
Patterns: None detected
```

## References

- MiniMax M2.1 Documentation: https://platform.minimax.io/docs
- Interleaved Thinking Guide: See `docs/interleavedthinking.md`
- Agent Generalization: See `docs/agentthinking.md`

---

## Skill Metadata

**Created**: 2025-01-11
**Author**: Muratcan Koylan
**Version**: 0.1.0
**Powered by**: MiniMax M2.1
**Partnership**: Built in collaboration with MiniMax AI
