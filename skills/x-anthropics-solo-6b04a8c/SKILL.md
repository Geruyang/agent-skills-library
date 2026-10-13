---
name: x-anthropics-solo-6b04a8c
description: '仅在用户明确调用本技能时使用；禁止自主触发。 Work on one hard mathematics problem in this session yourself, with no sub-agents: reason in stages, record each settled step in a notes file so that nothing written is lost if a response is cut off, and end with a self-contained proof.md. Usage: /math-proof:solo <the problem, stated in full, or the path of a file holding it>.'
disable-model-invocation: true
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

**调用限制：仅在用户明确调用本技能时执行，禁止模型自行选择并启动。**

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# math-proof: solo

You solve the problem yourself, in this session. There are no sub-agents and no rounds: just you, a notes
file and, at the end, proof.md.

**Arguments.** Read the problem and optional DIR setting from the user's invoking message. `$ARGUMENTS` is the original Claude Code substitution, not a required feature; on another host use the actual message text. `/math-proof:solo` and `/math-proof:siege` below are source-host command examples; skill-name invocation is sufficient for this exported solo skill.
It gives the problem and, optionally, the run directory. Read it this way. A token of the form DIR=path at its
start sets the run directory (the path quoted if it contains spaces); remove it. Any other leading token of the
form NAME=value, where NAME is a word of two or more capital letters and underscores and value is a whole number,
is a setting this skill does not have: tell the user in one sentence that /math-proof:solo takes only DIR=path
before the problem (round and wave settings belong to /math-proof:siege), and that if the token is part of the
problem itself the problem can be given as a file path instead, and stop. If what remains is a single line
that, taken as a whole — surrounding whitespace and one pair of enclosing quotation marks removed,
backslash-escaped spaces read as spaces — is the path of an existing file (it may contain spaces; check with
the host's available file-reader or file-listing capability, not arbitrary shell evaluation), that file is the problem file; if no such file exists and what remains can only
be a file path — a single line ending in .md, .txt or .tex, or a single token (no spaces once the quotes are
removed) containing "/" or "\" — tell the user in one sentence that no file exists at the absolute path you
looked for (give it) and that the problem can instead be given in full as text after the command, and stop;
otherwise everything that remains, to the end of the message, IS the problem statement, verbatim — mathematics,
line breaks and all ("n=3", "N=pq" and "AB=AC" are mathematics, not settings). The run directory DIR defaults to
./math-proof-solo under the current directory; use DIR's absolute path everywhere below. If the message holds
neither a readable problem file nor any problem text, say so in one sentence — with the usage,
`/math-proof:solo <problem statement, or the path of a file holding it>` — and stop.

**Setup.** The run's files are DIR/problem.md (the problem), DIR/notes.md (your notes) and DIR/proof.md (the
deliverable). Create DIR using the current host's directory creation capability (`mkdir -p` on a compatible shell). If DIR/notes.md already exists, this problem was already being
worked on in DIR: check that DIR/problem.md is the same problem you were given (compare the text, ignoring
differences in whitespace and line endings; for a file, a byte/text comparison capability such as `cmp` on a compatible shell) — if it differs, say in one sentence that DIR
holds work on a different problem and that `DIR=<another directory>` selects a fresh one, and stop; if it is
the same, read DIR/notes.md, and DIR/proof.md if it exists. If they record the solution as complete (proof.md
written and nothing in the notes still to do), the earlier session finished: say where proof.md is and that
`DIR=<another directory>` starts a fresh attempt, and stop. Otherwise the earlier session ended before it
finished, and whatever reasoning it had not written down is lost: continue from the last point recorded there
rather than starting over. If DIR/notes.md does not exist yet, put the problem at DIR/problem.md: if it came as
a file, copy that file there byte for byte with the native file-copy capability (`cp` on a compatible shell); if it came as text in the invoking message, Write
exactly that text (nothing added, removed or reworded). Then Read DIR/problem.md in full; it is the authoritative text of the problem. Use the shell only for those bounded directory creation, file-copy and comparison operations (native equivalents are allowed); use the available file reader/editor for the notes. If file operations are unavailable, report that durable on-disk notes and proof delivery cannot be completed. Do not substitute web access, mathematical code execution or subagents for the prescribed pure-reasoning workflow.

**The task.** Solve the problem stated in DIR/problem.md; the deliverable is DIR/proof.md. After reasoning,
write your answer. This task runs as a conversation that can span many messages, each with a bounded output
allowance; a message that is cut off is normally followed by a request to continue, and only what you have
WRITTEN (not unwritten reasoning) is guaranteed to carry into the next message. So write your work product
out as you go, in a notes file, DIR/notes.md: whenever you settle something — a lemma and its proof, a
reduction, a dead end and why it is dead, the precise statement you are now attempting — write it down before
reasoning further. A partial answer is much more useful than none. Writing to the notes is not finishing —
keep going after each write. Important: each message's output allowance also covers your private reasoning,
and it is far smaller than a hard problem deserves — a message spent entirely on reasoning, with nothing
written, gets cut off, and unwritten reasoning should be assumed lost. So do not try to finish in one
message. Work in stages: early in EVERY message, before any long derivation, write your current plan and the
precise statement you are attempting to DIR/notes.md; then reason toward the next concrete intermediate
result, append it to the notes as soon as you have it, and continue. Many short written steps beat one long
unwritten one. If a message of yours is cut off, re-read DIR/notes.md and continue from the last thing
written there; never start over. You have no web access and no code execution; this is a pure reasoning
task. When the problem is resolved, or you have taken it as far as you can, write your complete solution to
DIR/proof.md. proof.md is read on its own by a referee who cannot open any other file (not your notes
either), so it must be self-contained: every argument the solution relies on is written out in full there.
Work unattended: there is no one to answer questions, so never stop to ask.

When DIR/proof.md is written, reply briefly: where proof.md is, and whether it resolves the problem
completely or, in proof.md's own words, what it leaves open.
