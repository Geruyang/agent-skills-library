---
name: x-muratcankoylan-context-engineering-collection-19d0266
description: A comprehensive collection of Agent Skills for context engineering, harness engineering, multi-agent architectures, and production agent systems. Use when building, optimizing, evaluating, or debugging agent systems that require effective context management and reliable operating loops.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Agent Skills for Context Engineering

This collection provides structured guidance for building production-grade AI agent systems through effective context engineering.

## When to Activate

Activate these skills when:
- Building new agent systems from scratch
- Optimizing existing agent performance
- Debugging context-related failures
- Designing multi-agent architectures
- Creating or evaluating tools for agents
- Implementing memory and persistence layers
- Designing autonomous research or evaluation harnesses

## Skill Map

### Foundational Context Engineering

**Understanding Context Fundamentals**
Context is not just prompt text—it is the complete state available to the language model at inference time, including system instructions, tool definitions, retrieved documents, message history, and tool outputs. Effective context engineering means understanding what information truly matters for the task at hand and curating that information for maximum signal-to-noise ratio.

**Recognizing Context Degradation**
Language models exhibit predictable degradation patterns as context grows: the "lost-in-middle" phenomenon where information in the center of context receives less attention; U-shaped attention curves that prioritize beginning and end; context poisoning when errors compound; and context distraction when irrelevant information overwhelms relevant content.

### Architectural Patterns

**Multi-Agent Coordination**
Production multi-agent systems converge on three dominant patterns: supervisor/orchestrator architectures with centralized control, peer-to-peer swarm architectures for flexible handoffs, and hierarchical structures for complex task decomposition. The critical insight is that sub-agents exist primarily to isolate context rather than to simulate organizational roles.

**Long-Horizon Prompting**
Long-running autonomous agents and parallel orchestrations succeed or fail on the launch prompt. Pseudo-formal task briefs specify success predicates, non-counting outcomes, persistence rules with audit-gated return conditions, effort floors, diversity policies for parallel portfolios, and contamination guards, applying the discipline of formal verification linguistically to problems with no machine-checkable success condition.

**Memory System Design**
Memory architectures range from simple scratchpads to sophisticated temporal knowledge graphs. Vector RAG provides semantic retrieval but loses relationship information. Knowledge graphs preserve structure but require more engineering investment. The file-system-as-memory pattern enables just-in-time context loading without stuffing context windows.

**Filesystem-Based Context**
The filesystem provides a single interface for storing, retrieving, and updating effectively unlimited context. Key patterns include scratch pads for tool output offloading, plan persistence for long-horizon tasks, sub-agent communication via shared files, and dynamic skill loading. Agents use `ls`, `glob`, `grep`, and `read_file` for targeted context discovery, often outperforming semantic search for structural queries.

**Hosted Agent Infrastructure**
Background coding agents run in remote sandboxed environments rather than on local machines. Key patterns include pre-built environment images refreshed on regular cadence, warm sandbox pools for instant session starts, filesystem snapshots for session persistence, and multiplayer support for collaborative agent sessions. Critical optimizations include allowing file reads before git sync completes (blocking only writes), predictive sandbox warming when users start typing, and self-spawning agents for parallel task execution.

**Tool Design Principles**
Tools are contracts between deterministic systems and non-deterministic agents. Effective tool design follows the consolidation principle (prefer single comprehensive tools over multiple narrow ones), returns contextual information in errors, supports response format options for token efficiency, and uses clear namespacing.

### Operational Excellence

**Context Compression**
When agent sessions exhaust memory, compression becomes mandatory. The correct optimization target is tokens-per-task, not tokens-per-request. Structured summarization with explicit sections for files, decisions, and next steps preserves more useful information than aggressive compression. Artifact trail integrity remains the weakest dimension across all compression methods.

**Context Optimization**
Techniques include compaction (summarizing context near limits), observation masking (replacing verbose tool outputs with references), prefix caching (reusing KV blocks across requests), and strategic context partitioning (splitting work across sub-agents with isolated contexts).

**Self-Managed Context**
The model, not the harness, decides what stays in its live context: the editable region is exposed as a file the model rewrites with code tools and re-parsed each turn. The harness keeps the invariants (pinned system and task prefix, role folding, edit gate, receipts, deterministic budget readouts, rollback on overflow). Edit cost scales with the text after the edit under prefix caching, so edits are batched and placed with the tail in mind; strategy can be steered by instruction, evolved as a skill, or trained with a success-gated efficiency reward.

**Latent Briefing (KV Memory Sharing)**
Orchestrator-worker systems can compound tokens when supervisors accumulate long trajectories but workers see only narrow text slices. Latent Briefing compacts the orchestrator trajectory in the worker model's KV cache using task-guided attention (Attention Matching-style compaction) so workers receive relevant latent state without full-text replay when the stack exposes worker KV state and the models are compatible.

**Evaluation Frameworks**
Production agent evaluation requires deterministic checks and multi-dimensional rubrics covering factual accuracy, completeness, tool efficiency, and process quality. Use model judges only after structure, evidence, and rubric math are valid; route judge design, pairwise comparison, and bias mitigation to Advanced Evaluation.

**Harness Engineering**
Reliable autonomous agents need explicit operating loops around the model: locked metrics, editable surfaces, durable logs, novelty checks, rollback rules, and human approval boundaries. Harnesses prevent agents from weakening the evaluator, losing state across compaction, or turning ambiguous goals into unreviewable changes.

**Self-Improvement Loops**
When the harness itself becomes the optimization target, a different discipline applies: recursive self-improvement, meta-harness search, failure-driven bounded self-edits, evolutionary scaffold search, and context mechanism evolution. The controlling constraints are empirical two-split acceptance gates, filesystem experience archives with raw traces, runtime-enforced constraints outside every editable surface, and diversity preservation to prevent collapse.

### Development Methodology

**Project Development**
Effective LLM project development begins with task-model fit analysis: validating through manual prototyping that a task is well-suited for LLM processing before building automation. Production pipelines follow staged, idempotent architectures (acquire, prepare, process, parse, render) with file system state management for debugging and caching. Structured output design with explicit format specifications enables reliable parsing. Start with minimal architecture and add complexity only when proven necessary.

### Cognitive Architecture

**BDI Mental States**
Belief-desire-intention modeling provides a formal way to translate structured external context into agent mental states. Use it for rational agency, explainability, and systems that need auditable links between beliefs, goals, and chosen actions.

## Core Concepts

The collection is organized around four core themes. First, context fundamentals establish what context is, how attention mechanisms work, and why context quality matters more than quantity. Second, architectural patterns cover the structures and coordination mechanisms that enable effective agent systems. Third, operational excellence addresses optimization, evaluation, and harness reliability. Fourth, development methodology and cognitive architecture cover project execution and formal mental-state modeling.

## Practical Guidance

Each skill can be used independently or in combination. Start with fundamentals to establish context management mental models. Branch into architectural patterns based on your system requirements. Reference operational skills when optimizing production systems.

The skills are platform-agnostic and work with Claude Code, Cursor, or any agent framework that supports custom instructions or skill-like constructs.

## Integration

This collection integrates with itself—skills reference each other and build on shared concepts. The fundamentals skill provides context for all other skills. Architectural skills (multi-agent, memory, tools) can be combined for complex systems. Operational skills (optimization, evaluation) apply to any system built using the foundational and architectural skills.

## References

Internal skills in this collection:
- [context-fundamentals](../x-muratcankoylan-context-fundamentals-ad2a946/SKILL.md)
- [context-degradation](../x-muratcankoylan-context-degradation-cd1f0f8/SKILL.md)
- [context-compression](../x-muratcankoylan-context-compression-2ee2b24/SKILL.md)
- [multi-agent-patterns](../x-muratcankoylan-multi-agent-patterns-9f53d2f/SKILL.md)
- [long-horizon-prompting](../x-muratcankoylan-long-horizon-prompting-581c4c9/SKILL.md)
- [memory-systems](../x-muratcankoylan-memory-systems-fc3798f/SKILL.md)
- [tool-design](../x-muratcankoylan-tool-design-c0e61e2/SKILL.md)
- [filesystem-context](../x-muratcankoylan-filesystem-context-79e5008/SKILL.md)
- [hosted-agents](../x-muratcankoylan-hosted-agents-5ec64e0/SKILL.md)
- [context-optimization](../x-muratcankoylan-context-optimization-eaacc11/SKILL.md)
- [self-managed-context](../x-muratcankoylan-self-managed-context-70bc045/SKILL.md)
- [latent-briefing](../x-muratcankoylan-latent-briefing-8703952/SKILL.md)
- [evaluation](../x-muratcankoylan-evaluation-09f8e7b/SKILL.md)
- [advanced-evaluation](../x-muratcankoylan-advanced-evaluation-1a6cf04/SKILL.md)
- [harness-engineering](../x-muratcankoylan-harness-engineering-a4ee296/SKILL.md)
- [self-improvement-loops](../x-muratcankoylan-self-improvement-loops-11b60a4/SKILL.md)
- [project-development](../x-muratcankoylan-project-development-8e452e7/SKILL.md)
- [bdi-mental-states](../x-muratcankoylan-bdi-mental-states-87d55ca/SKILL.md)

External resources on context engineering:
- Research on attention mechanisms and context window limitations
- Production experience from leading AI labs on agent system design
- Framework documentation for LangGraph, AutoGen, and CrewAI

---

## Skill Metadata

**Created**: 2025-12-20
**Last Updated**: 2026-10-01
**Author**: Agent Skills for Context Engineering Contributors
**Version**: 2.6.0
