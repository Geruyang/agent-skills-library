---
name: x-openai-yeet-7636127
description: Use only when the user explicitly asks to stage, commit, push, and open a GitHub pull request in one flow using the GitHub CLI (`gh`).
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

## Prerequisites

- Require GitHub CLI `gh`. Check `gh --version`. If missing, ask the user to install `gh` and stop.
- Require authenticated `gh` session. Run `gh auth status`. If not authenticated, ask the user to run `gh auth login` (and re-run `gh auth status`) before continuing.

## Naming conventions

- Branch: `{description}` when starting from main/master/default.
- Commit: `{description}` (terse).
- PR title: `{description}` summarizing the full diff.

## PR template discovery

Before creating the PR, resolve the repository root and look for the active GitHub PR template from there:

```shell
repo_root="$(git rev-parse --show-toplevel)"
```

Template candidates, in order:

- `.github/pull_request_template.md`
- `.github/PULL_REQUEST_TEMPLATE.md`
- One `*.md` file under `.github/pull_request_template/`
- One `*.md` file under `.github/PULL_REQUEST_TEMPLATE/`

Use paths as emitted from the repository root, such as `.github/pull_request_template.md`, not `./.github/pull_request_template.md`.

If exactly one template is found, read it before composing the final PR body and pass it to `gh pr create` with `--template "$template"`.

If multiple template files are found, stop before PR creation and ask which template to use. If no template exists, use the fallback body shape in this skill.

## Workflow

- If on main/master/default, create a branch: `git checkout -b "{description}"`
- Otherwise stay on the current branch.
- Confirm status, then stage everything: `git status -sb` then `git add -A`.
- Commit tersely with the description: `git commit -m "{description}"`
- Run checks if not already. If checks fail due to missing deps/tools, install dependencies and rerun once.
- Push with tracking: `git push -u origin $(git branch --show-current)`
- If git push fails due to workflow auth errors, pull from master and retry the push.
- Discover and read the repository PR template, if any.
- Check whether the current branch already has a PR: `gh pr view "$(git branch --show-current)" --json number,isDraft,url`
- If a PR already exists, update that PR in place. Do not create another PR, and do not change whether the existing PR is draft or ready for review.
- If no PR exists, open a new draft PR:
  - With one template: `GH_PROMPT_DISABLED=1 GIT_TERMINAL_PROMPT=0 gh pr create --draft --fill --template "$template" --head "$(git branch --show-current)"`
  - Without a template: `GH_PROMPT_DISABLED=1 GIT_TERMINAL_PROMPT=0 gh pr create --draft --fill --head "$(git branch --show-current)"`
- Edit the PR title and body so they reflect the actual net change in the diff.
- Write the PR description to a temp file with real newlines and pass it via `--body-file` or `gh pr edit --body-file` to avoid `\n`-escaped markdown.

## Determining the PR

When updating a PR created earlier in the flow, infer the PR from the current branch when possible:

```shell
git branch --show-current
gh pr view "$(git branch --show-current)" --json number --jq '.number'
```

If this finds an existing PR, preserve its current review state. Never convert an existing ready-for-review PR back to draft as part of `yeet`; only new PRs created by this flow should start as draft.

## PR Title

Format: `<type>(<scope>): <subject>`

`<scope>` is optional. A scope consist of a noun describing a section of the codebase (component, service or subsytem).

### Example

```
feat: add hat wobble
^--^  ^------------^
|     |
|     +-> Summary in present tense.
|
+-------> Type: chore, docs, feat, fix, refactor, style, or test.
```

More Examples:

- `feat`: (new feature for the user, not a new feature for build script)
- `fix`: (bug fix for the user, not a fix to a build script)
- `docs`: (changes to the documentation)
- `style`: (formatting, missing semi colons, etc; no production code change)
- `refactor`: (refactoring production code, eg. renaming a variable)
- `test`: (adding missing tests, refactoring tests; no production code change)
- `chore`: (updating grunt tasks etc; no production code change)


## PR Body Contents

When invoked, use `gh` to edit the pull request body and title to reflect the contents of the specified PR. Make sure to check the existing pull request body to see if there is key information that should be preserved. For example, NEVER remove an image in the existing pull request body, as the author may have no way to recover it if you remove it.

When a repository PR template exists, adapt the final PR body to that template. Preserve meaningful headings, required checklists, and repo-specific prompts, but replace placeholder text with net-diff-specific content or `N/A` where the template asks for it. Do not discard template sections just because the fallback shape below is shorter.

It is critically important to explain _why_ the change is being made. If the current conversation in which this skill is invoked has discussed the motivation, be sure to capture this in the pull request body.

The body should also explain _what_ changed, but this should appear after the _why_.

Limit discussion to the _net change_ of the commit. It is generally frowned upon to discuss changes that were attempted but later undone in the course of the development of the pull request. When rewriting the pull request body, you may need to eliminate details such as these when they are no longer appropriate / of interest to future readers.

Avoid references to absolute paths on my local disk. When talking about a path that is within the repository, simply use the repo-relative path.

Default to omitting `Verification`. Add it only when you have behavioral evidence worth preserving for reviewers: a reproduced bug, a before/after check, a targeted test that exercises the changed behavior, or a manual scenario with input and observed outcome. Do not use it for generic commands or automation results such as package tests, type checks, linters, formatters, pre-commit/pre-push hooks, or CI status.

If the repository template requires a validation or verification section, keep that section and avoid generic filler: include meaningful commands/results, a targeted manual scenario, or `Not run` with a reason.

Use professional Markdown:

- Put code, paths, commands, flags, and identifiers in backticks.
- Use fenced code blocks for shell transcripts or multi-line examples.
- Use GitHub permalinks when citing existing code relevant to the change.
- Reference relevant issues or related PRs, but do not reference the PR in its own body.

### Suggested PR Body Shape

Use this as a fallback when the repository does not have a PR template:

```markdown
## Why

Describe the user-facing or maintainer-facing problem, including cause and effect where useful.

## What Changed

Describe the net implementation change in concise prose.
```
