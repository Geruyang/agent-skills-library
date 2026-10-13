---
name: x-openai-codex-expo-run-actions-2312b50
description: Wire Expo projects into the Codex app with project-local run scripts and .codex/environments/environment.toml actions. Use only when the user explicitly asks to configure the Codex app Run button or Codex-specific Expo actions. A generic Expo run request in another client does not trigger Codex configuration.
license: MIT
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# Codex Run Actions for Expo

Use this skill only for an explicit request to connect an Expo project to the Codex app action bar. The executing assistant may run in another client, but the configured product must still be Codex. Do not create `.codex` files for a TRAE, Claude, or other client's generic Run workflow; use that client's verified task mechanism or deliver only the portable Expo shell script.

The goal is one project-local script plus `.codex/environments/environment.toml`,
so the user can press `Run` in the Codex app and see the Expo CLI / Metro logs in
an action terminal.

## Workflow

1. Confirm the current workspace is an Expo app.
   - Look for `package.json`.
   - Look for `app.json`, `app.config.js`, `app.config.ts`, or `expo` in `package.json`.
   - Do not wire the Codex action at a monorepo root if the Expo app is in a child package.

2. Discover the package runner.
   - Prefer the package manager declared in `packageManager`.
   - Otherwise infer from lockfiles.
   - The generated run script should still have a safe fallback to `npx expo`.

3. Create or update `script/build_and_run.sh`.
   - Use the reference file for the script shape.
   - Default no-argument mode starts the Expo dev server: `expo start`.
   - Keep the dev server in the foreground so the Codex action terminal owns logs and Ctrl-C behavior.
   - Support optional modes for direct buttons:
     - `--ios` starts Expo and opens iOS simulator.
     - `--android` starts Expo and opens Android.
     - `--web` starts Expo for web.
     - `--dev-client` starts in dev-client mode.
     - `--tunnel` starts a tunnel.
     - `--export-web` exports web.

4. Write `.codex/environments/environment.toml`.
   - Always add or update one primary action named `Run`.
   - Wire `Run` to `./script/build_and_run.sh`.
   - Add direct `Run iOS`, `Run Android`, `Run Web`, or `Run Dev Client`
     actions only when the user asks for those buttons or the project clearly needs them.
   - If the environment file already exists, update the existing matching action instead of duplicating it.

5. Use the action script as the default local run path.
   - After wiring, run `./script/build_and_run.sh --help` or a short non-server mode if you need to sanity-check syntax.
   - Do not start a long-lived Metro server during a setup-only task unless the user asked you to run the app.

## References

- `references/expo-run-button-bootstrap.md`: canonical Expo `script/build_and_run.sh` and Codex environment action examples.

## Guardrails

- Try Expo Go / `expo start` first; do not default the Codex Run button to `expo run:ios`, `expo run:android`, prebuild, or EAS Build.
- Do not wire cloud actions such as `eas build`, `eas submit`, or store deployment into Codex buttons unless the user explicitly asks and accepts the auth / time / cost tradeoff.
- Do not create a nested git repo.
- Do not put secrets in `.codex/environments/environment.toml` or in the run script.
- Do not background Metro from the run script; the action terminal should show the active server logs.
- Do not hard-code npm if the project uses pnpm, yarn, or bun.

## Output Expectations

When setup changes are made, summarize:

- the Expo app root you wired
- the run script path
- the Codex environment file path
- the actions added or updated
- how to launch the same path from shell
