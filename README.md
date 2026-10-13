<p align="center"><img src="assets/banner.svg" alt="Agent Skills Library — 667 upstream skills and 2 synthesis skills" /></p>

<p align="center"><strong>让 Agent 少一点重复解释，多一点可复用的工作方法。</strong><br/>从 6 个公开来源整理 667 项技能，另附 2 项 Agent 设计整合技能。</p>

<p align="center"><b>中文</b> · <a href="README.en.md">English</a> · <a href="SKILLS_INDEX.md">浏览技能</a> · <a href="SOURCES.md">查看来源</a> · <a href="https://github.com/Geruyang/agent-design-sourcebook">配套源码库</a></p>

你可能已经有了好用的模型，却还在反复解释：怎么审查代码、怎么做调研、怎么处理文档、怎么设计 Agent。这个仓库把分散的工作方法整理成可检索、可按需安装的 **Agent Skills**，帮助你找到适合当前任务的那一项。

## 从这里开始

| 你想做什么 | 从哪里入手 |
|---|---|
| 找开发、调试、评审、测试工作流 | [完整技能索引](SKILLS_INDEX.md)，搜索 `debug`、`review`、`testing` |
| 写文档、做演示、处理表格与 PDF | 索引搜索 `docx`、`pptx`、`xlsx`、`pdf` |
| 设计 Agent 的工具、记忆、上下文与评估 | [agent-designer](skills/agent-designer/SKILL.md) |
| 研究 Agent Foundation 的集成方式 | [agent-foundation](skills/agent-foundation/SKILL.md) |
| 找到原作者和原始版本 | [来源目录](SOURCES.md)与[逐项清单](catalog/skills.json) |

## 为什么收藏这个仓库

- **667 项下载技能 + 2 项整合技能**：覆盖开发、文档、设计、上下文工程、工具集成等场景。
- **来源可追溯**：每项下载技能都有原始仓库、固定提交和路径；附原始副本，方便比较适配内容。
- **三种客户端的安装入口**：面向 Codex、TRAE 和 Claude Code；用同一套目录与资源组织方式安装。
- **按需选，不必全装**：先装一项试用；来源前缀区分同名技能，安装器遇到已有不同内容就停止。
- **配套真实源码**：想继续理解运行时、工具协议和交互设计，可以接着看 [35 个项目的源码合集](https://github.com/Geruyang/agent-design-sourcebook)。

## 三分钟开始

需要 Python 3.10+。可以点击 GitHub 的 **Code → Download ZIP** 并解压，也可以：

```bash
git clone https://github.com/Geruyang/agent-skills-library.git
cd agent-skills-library
python scripts/install.py --list
```

先安装一项试试。下面第一条只预览，第二条才写入：

```bash
python scripts/install.py --client codex --skill agent-designer
python scripts/install.py --client codex --skill agent-designer --apply
```

安装到 TRAE / Claude Code 的当前项目：

```bash
python scripts/install.py --client trae --project /path/to/project --skill agent-designer --apply
python scripts/install.py --client claude --project /path/to/project --skill agent-designer --apply
```

将 `/path/to/project` 换成真实路径；Windows 路径含空格时加引号。安装全部 669 个入口时使用 `--all` 替代 `--skill agent-designer`。`--dest` 可指定客户端数据目录。安装器会复制共享资源、索引和许可证，不安装 MCP 或运行依赖，也不改客户端配置。

安装后新建或重新加载会话，明确要求使用该技能。例如：**“使用 agent-designer，帮我设计一个能调用工具、保存状态并恢复任务的研究助手。”** 具体调用语法以客户端为准。

## 收录与实测边界

6 个来源为 OpenAI skills/plugins、Anthropic skills/official plugins、Superpowers 和 Agent Skills for Context Engineering。这里的数量是本次固定快照，不代表上游实时数量。

整理时，667 项下载技能通过了 Codex 真实加载检查与 TRAE 解析检查；Claude Code 发现了全部入口，并对样本做了展开和调用验证。**没有逐一运行所有技能的第三方业务。** 部分技能仍需要账号、API、特定系统、硬件或额外工具；技能文件不等于这些依赖已经安装。大量技能的描述也可能受客户端上下文预算限制，建议按需选择。

## 目录

```text
skills/           667 个适配入口 + 2 个整合技能
original-skills/  667 个原始副本，仅供对照
resources/        共享参考和资源
licenses/         原始许可证与声明
catalog/          逐项来源、版本及路径
scripts/install.py  不覆盖已有不同文件的安装器
```

## 致谢与贡献

本仓库做整理、适配与索引，原技能的贡献属于各上游作者。请阅读 [SOURCES.md](SOURCES.md) 和 [NOTICE.md](NOTICE.md)，按各组件原始许可证使用；没有统一改为 MIT，也没有收录本机内部插件或私人配置。

发现坏链接、缺资源、客户端兼容问题，欢迎提交 Issue，附技能 ID、客户端版本和最小复现。觉得有帮助，欢迎 **Star 收藏这个入口，也给你实际使用的上游项目一个 Star**。
