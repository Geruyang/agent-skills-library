---
name: x-openai-mixpanel-headless-setup-1c898d2
description: This skill installs mixpanel_headless, pandas, numpy, matplotlib, seaborn, networkx, anytree, scipy (and pyarrow on Python 3.11+), then verifies Mixpanel credentials. It should be invoked when setting up a new environment for Mixpanel data analysis, when dependencies are missing, or when configuring service account or OAuth credentials for the first time.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# mixpanel-headless — Setup

Install dependencies and verify credentials for CodeMode analytics.

## Run Setup

Before running bundled scripts, set `SKILL_DIR` to the absolute path of this
skill directory. Discover a shell with Bash support and Python 3.10+ first. If Bash is unavailable, use an available Python execution tool to install the same listed dependencies in an authorized environment and perform the import/auth checks; if execution or package installation is unavailable, report setup as blocked.

```bash
bash "$SKILL_DIR/scripts/setup.sh"
```

This will:
1. Verify Python 3.10+ is available
2. Install `mixpanel_headless`, `pandas`, `numpy`, `matplotlib`, `seaborn`, `networkx>=3.0`, `anytree>=2.8.0`, `scipy`, and `pyarrow>=17.0` on Python 3.11+ (tries uv, pip in order)
3. Verify all packages import successfully (including pyarrow on 3.11+, networkx, anytree, and scipy)
4. Check for configured Mixpanel credentials (single schema — Account → Project → Workspace)

## Check Credentials

After installation, locate the installed `mixpanelyst` companion skill by its name or source manifest and set `MIXPANELYST_DIR` to its verified absolute directory. Its `auth_manager.py` is not bundled here. Check that the script exists before running it. If absent, inspect `mp --help` and the installed command help for an equivalent session/account check; if no supported equivalent is available, report authentication verification as blocked. When the helper exists, check the active session:

```bash
python3 "$MIXPANELYST_DIR/scripts/auth_manager.py" session
```

Parse the JSON `state` field:
- **`ok`** — credentials configured. Show `account.name` → project `project.id` and proceed to verification.
- **`needs_account`** — no account configured. Read `next` for onboarding suggestions and follow "If Credentials Are Missing" below.
- **`needs_project`** — account configured but no project pinned. Suggest `mp project list` then `mp project use <id>`.
- **`error`** — show `error.message`. If `error.actionable` is true, the message names a concrete next command.

## If Credentials Are Missing

If no credentials are configured, guide the user to one of these methods:

### Recommended: `mp login`

The frictionless one-shot path. Tell the user to run:

```bash
mp login
```

`mp login` runs the right auth flow for the environment, derives the
account name from `/me`, and pins a default project. For laptops with a
usable browser, this opens the PKCE flow; for environments with
`MP_USERNAME` + `MP_SECRET` set, it skips the browser and uses the
service-account path; for `MP_OAUTH_TOKEN` set, it uses the static
bearer.

Region behavior:
- `service_account` and `oauth_token` paths probe `us → eu → in` when
  `--region` is omitted.
- `oauth_browser` (the bare-`mp login` default) defaults to `us`. EU and
  India browser users must pass `--region eu` or `--region in`.

Useful flags: `--name NAME`, `--region us|eu|in`, `--project ID`,
`--service-account`, `--token-env VAR`, `--no-browser`, `--secret-stdin`.

### Alternative: Guided Setup (explicit account add)

Use the `mixpanel-auth` skill's account-add workflow for a
step-by-step walkthrough. The workflow never prompts for secrets in
conversation — it instructs the user to run `mp account add ...`
themselves so the secret is read with hidden input. Use this path when
the user wants explicit control over the account name, region, and type
at registration time.

### Alternative: Service-Account Environment Variables (temporary)

For quick testing, set all four variables in the shell — the resolver
picks them up directly without account registration:

```bash
export MP_USERNAME="service-account-username"
export MP_SECRET="service-account-secret"
export MP_PROJECT_ID="12345"
export MP_REGION="us"  # or "eu", "in"
```

### Alternative: Raw OAuth Bearer Token (best for agents / CI)

If the user has an OAuth 2.0 access token from another source, they can use
it directly without the PKCE browser flow:

```bash
export MP_OAUTH_TOKEN="<bearer-token>"
export MP_PROJECT_ID="12345"
export MP_REGION="us"  # or "eu", "in"
```

This is the recommended mode for non-interactive contexts. The full
service-account env-var set (`MP_USERNAME` + `MP_SECRET` + `MP_PROJECT_ID`
+ `MP_REGION`) takes precedence when both sets are complete.

## Remote Environment

Determine the actual session capabilities rather than inferring them from a host name, a cloud environment variable, or a `/sessions` directory. A remote session may have a usable browser, terminal, or supported OAuth device flow; use only flows advertised by the installed `mp` version and allowed by the current host.

If interactive authentication is unavailable, use the documented service-account or OAuth environment variables above, a persisted Mixpanel account supported by the installed library, or an explicitly configured credential bridge. Do not request secrets in conversation.

### Optional credential bridge

A bridge is useful only when the receiving Mixpanel runtime documents how to consume it. Verify that contract and the destination before export; do not assume that a file copied into a particular agent's directory will be imported or refreshed automatically.

```bash
# Example only: set this to the verified path consumed by the receiving runtime.
export MP_AUTH_BRIDGE_FILE="/absolute/authorized/path/mixpanel-auth.json"
mp account export-bridge --to "$MP_AUTH_BRIDGE_FILE"
```

`MP_AUTH_BRIDGE_FILE` is an input to this skill's setup diagnostic, not a claim that the Mixpanel library recognizes that variable. The script inspects only the explicitly supplied file and does not import or transmit it. The original `~/.claude/mixpanel/auth.json` path belongs to a Claude-specific bridge integration; use it only if that integration is actually installed and documents it. Apply restrictive file permissions and keep the bridge out of source control.

If there is no supported secure authentication route, stop credential verification and state the missing capability. If a token expires, use the installed library's documented refresh mechanism or have the user reauthenticate in a supported environment; verify access again before reporting success. Restart a session only when that receiver's bridge contract requires it.

## Verify Everything Works

```bash
python3 "$MIXPANELYST_DIR/scripts/auth_manager.py" account test
```

The subcommand never raises — read `result.ok` to determine outcome.
- `result.ok: true` → setup is complete; the user can ask analytics questions.
- `result.ok: false` → suggest the `mixpanel-auth` account-test workflow for detailed diagnostics.

## Post-Setup: Explore Your Data

Once authenticated, these named companion-skill workflows help orient the user. Locate the skill in the current catalog; slash-command support is host-specific:

- `mixpanel-auth` project-list workflow — discover all accessible projects via `/me`
- `mixpanel-auth` session workflow — see active account / project / workspace
- `mixpanel-auth` project-use workflow — switch to a different project
- `mixpanel-auth` target-add workflow — save a named cursor position

The user can also construct a Workspace targeting a specific account / project /
workspace directly:

```python
import mixpanel_headless as mp

ws = mp.Workspace()                                  # default session
ws = mp.Workspace(account="team")                    # named account
ws = mp.Workspace(project="67890")                   # explicit project (active account)
ws = mp.Workspace(account="team", project="67890")   # both axes
ws.use(project="98765").events()                     # in-session switch (no re-auth)
```

_For analytics questions, load the companion [mixpanelyst skill](../x-openai-mixpanelyst-cd72fae/SKILL.md).
Its [Exploratory Analysis Workflow](../x-openai-mixpanelyst-cd72fae/SKILL.md#exploratory-analysis-workflow)
guides investigations, and its [API reference](../x-openai-mixpanelyst-cd72fae/SKILL.md#mixpanel_headless-api-reference)
contains the supported query patterns. Verify actual method signatures with its bundled
[help.py](../x-openai-mixpanelyst-cd72fae/scripts/help.py), as the companion skill requires._
