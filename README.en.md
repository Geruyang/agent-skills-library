<p align="center"><img src="assets/banner.svg" alt="Agent Skills Library" /></p>

<p align="center"><strong>Give your agent repeatable workflows, not the same instructions again.</strong><br/>667 skills from 6 public upstream collections, plus 2 agent-design synthesis skills.</p>

<p align="center"><a href="README.md">中文</a> · <b>English</b> · <a href="SKILLS_INDEX.md">Browse skills</a> · <a href="SOURCES.md">Sources</a> · <a href="https://github.com/Geruyang/agent-design-sourcebook">Source companion</a></p>

You have a capable model. You still repeat how to review code, research a topic, prepare documents, or design an agent. This collection brings those reusable methods into a searchable **Agent Skills** library, with provenance and a selective installer.

## Pick your starting point

| Your task | Start here |
|---|---|
| Development, debugging, reviews and tests | Search the [skill index](SKILLS_INDEX.md) for `debug`, `review`, or `testing` |
| Documents, slides, spreadsheets and PDFs | Search for `docx`, `pptx`, `xlsx`, or `pdf` |
| Agent tools, state, memory and evaluation | [agent-designer](skills/agent-designer/SKILL.md) |
| Agent Foundation integration | [agent-foundation](skills/agent-foundation/SKILL.md) |
| Original authors and versions | [Sources](SOURCES.md) and the [per-skill catalog](catalog/skills.json) |

## What you get

- **667 upstream skills + 2 synthesis skills**, spanning development, documents, design, context engineering and tool integration.
- **Traceable provenance**: original repository, pinned commit and source path for every downloaded skill, with original copies for comparison.
- **Installation paths for Codex, TRAE and Claude Code**, with shared resources kept beside the installed skills.
- **Selective installation**: start with one skill. Source-prefixed IDs distinguish similarly named entries; conflicting existing files are never overwritten.
- **A source companion**: explore implementations in the [35-project Agent Design Sourcebook](https://github.com/Geruyang/agent-design-sourcebook).

## Quick start

Requires Python 3.10+. Download through **Code → Download ZIP**, or clone:

```bash
git clone https://github.com/Geruyang/agent-skills-library.git
cd agent-skills-library
python scripts/install.py --list
```

Preview one skill, then install it:

```bash
python scripts/install.py --client codex --skill agent-designer
python scripts/install.py --client codex --skill agent-designer --apply
```

For a TRAE or Claude Code project:

```bash
python scripts/install.py --client trae --project /path/to/project --skill agent-designer --apply
python scripts/install.py --client claude --project /path/to/project --skill agent-designer --apply
```

Replace the project path with yours; quote Windows paths containing spaces. Use `--all` instead of `--skill agent-designer` to select all 669 entries. Use `--dest` to specify a client data directory. The installer includes companion resources, indexes and license notices, but does not install MCP servers or runtime dependencies, or change client configuration.

Start or reload a session, then explicitly request a skill: **“Use agent-designer to design a research assistant with tool calls, persistent state and task recovery.”** Invocation syntax depends on your client.

## Sources and validation

The six collections are OpenAI skills/plugins, Anthropic skills/official plugins, Superpowers, and Agent Skills for Context Engineering. Counts refer to the curated snapshot, not the live upstream totals.

During collection, all 667 downloaded entries passed actual Codex discovery and TRAE parsing. Claude Code discovered every entry, with expansion and tool-call checks on samples. **Every third-party business workflow has not been executed.** Some skills require accounts, APIs, operating systems, hardware or other tools. Installing a skill does not install those dependencies. Large catalogs may also exceed a client's description budget; selective installation is recommended.

## Layout

```text
skills/              667 adapted entries + 2 synthesis skills
original-skills/     667 original copies, for comparison only
resources/           Shared references and assets
licenses/            Upstream licenses and notices
catalog/             Original locations and pinned versions
scripts/install.py   Conflict-preserving installer
```

## Attribution and contributions

This project provides curation, adaptation and indexing; upstream authors retain credit and rights. Read [SOURCES.md](SOURCES.md) and [NOTICE.md](NOTICE.md). Each component retains its own license; there is no blanket MIT relicensing. No private client configuration or internal plugin bundle is included.

Found a broken link, missing resource or compatibility issue? Open an issue with the skill ID, client version and a minimal reproduction. **Star this library if it helps you find useful workflows—and support the upstream projects you use.**
