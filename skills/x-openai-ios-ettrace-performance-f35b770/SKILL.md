---
name: x-openai-ios-ettrace-performance-f35b770
description: Capture and interpret iOS Simulator ETTrace profiles. Use when profiling launch or runtime latency, comparing traces, or finding CPU-heavy stacks.
---

### 导出副本边界与技能别名

迁移、安装、修复和经验回写只作用于当前加载的目标宿主技能副本。原 Codex 技能/MCP、下载的源码和 `original-skills` 均为来源材料，不因执行本副本而写入；只有用户另行明确要求配置 Codex 产品本身时，才按该产品流程处理指定目标。脚本需要安装目录或状态目录时，显式提供目标路径；不得从 `CODEX_HOME` 隐式推断写入位置。

跨技能名称可能沿用源库别名。先查 [技能别名表](../../skill-aliases.json)，优先选择同来源、同插件的条目，再使用其 `id` 调用或读取对应入口；不得假定旧 `$skill`、`superpowers:skill` 名称在新宿主直接注册。不能确定目标时先核对，不替换真实产品命令或 Shell 环境变量。

## 跨宿主使用约定

本副本供支持 Agent Skills 的客户端使用。先检查当前宿主实际提供的工具、权限和已连接服务，再执行正文工作流。原文中的宿主工具标识是能力参考；只有实际发现该工具时才可调用，其他宿主应使用经核验的等价 MCP、CLI 或 API。没有等价能力的步骤必须报告不可用，不能虚构调用或完成状态。

技能资源以本技能目录为基准；输出写入当前项目中用户指定的位置。通过技能名称或自然语言触发，具体快捷命令由宿主决定。涉及真实产品、模型 API、协议字段和官方网址的名称保持原意。授权、审批、隐私和工具范围限制在迁移后仍然有效；不得为兼容而扩大权限。具体依赖与迁移说明见同目录 `PORTABILITY.md`。

# iOS ETTrace Performance

Use this skill to capture a focused, symbolicated ETTrace profile from an iOS simulator app. Pair it with `../x-openai-ios-debugger-agent-197293c/SKILL.md` when the task also needs simulator build, install, launch, UI driving, logs, or screenshots.

## Core Workflow

1. Pick one focused flow and write down the expected start and stop points.
2. Build the exact simulator app that will be installed and profiled.
3. Temporarily link ETTrace into that app target for simulator/debug profiling.
4. Collect UUID-matched dSYMs for the app executable and embedded dynamic frameworks.
5. Capture one launch or runtime trace.
6. Preserve the processed flamegraph JSON immediately after the run.
7. Analyze only the processed JSON and report the flow, artifacts, hotspots, and caveats.

Avoid broad "use the app for a while" captures. One trace should correspond to one user-visible flow.

## Setup

Use a writable run folder for each profiling session:

```bash
if [ -z "${RUN_DIR:-}" ]; then
  RUN_DIR="$(mktemp -d "${TMPDIR:-/tmp}/agent-ios-ettrace.XXXXXX")"
fi
mkdir -p "$RUN_DIR"
```

Install the ETTrace runner CLI if it is not already available:

```bash
brew install emergetools/homebrew-tap/ettrace
```

`ettrace` is the host-side macOS runner. The app must also link an `ETTrace.xcframework` for the iOS Simulator architecture.
This workflow is validated for ETTrace v1.1.0 processed `output_<thread>.json` files with top-level `nodes`.

## Link ETTrace Into The App

Wire ETTrace into the exact app target being profiled. Keep the integration in a clearly temporary patch and remove it when the profiling task is done unless the user explicitly asks to keep it.

Preferred options:

- Reuse an existing simulator-compatible `ETTrace.xcframework` if the repo already vendors one.
- If none exists, build a simulator-only copy into `RUN_DIR` from the upstream ETTrace package.
- Link the framework directly into the app target, not only into tests, resources, data files, or a nested launcher target.
- Confirm launch logs print `Starting ETTrace`.
- Profile only one ETTrace-instrumented simulator app at a time because simulator mode listens on a fixed localhost port.

Build a simulator framework when needed:

```bash
ETTRACE_TAG="${ETTRACE_TAG:-v1.1.0}" # Override to match the installed runner when Homebrew updates.
ETTRACE_SRC="$RUN_DIR/ETTrace-src"
if [ ! -d "$ETTRACE_SRC" ]; then
  git clone --depth 1 --branch "$ETTRACE_TAG" https://github.com/EmergeTools/ETTrace "$ETTRACE_SRC"
fi

rm -rf "$RUN_DIR/ETTrace-iphonesimulator.xcarchive" "$RUN_DIR/ETTrace.xcframework"
pushd "$ETTRACE_SRC" >/dev/null
xcodebuild archive \
  -scheme ETTrace \
  -archivePath "$RUN_DIR/ETTrace-iphonesimulator.xcarchive" \
  -sdk iphonesimulator \
  -destination 'generic/platform=iOS Simulator' \
  BUILD_LIBRARY_FOR_DISTRIBUTION=YES \
  INSTALL_PATH='Library/Frameworks' \
  SKIP_INSTALL=NO \
  CLANG_CXX_LANGUAGE_STANDARD=c++17

xcodebuild -create-xcframework \
  -framework "$RUN_DIR/ETTrace-iphonesimulator.xcarchive/Products/Library/Frameworks/ETTrace.framework" \
  -output "$RUN_DIR/ETTrace.xcframework"
popd >/dev/null
```

For Bazel apps, a temporary import usually looks like:

```python
load("@rules_apple//apple:apple.bzl", "apple_dynamic_xcframework_import")

package(default_visibility = ["//visibility:public"])

apple_dynamic_xcframework_import(
    name = "ETTrace",
    xcframework_imports = glob(["ETTrace.xcframework/**"]),
)
```

For Xcode projects, temporarily add the simulator `ETTrace.xcframework` to the app target's Link Binary With Libraries / Embed Frameworks phases for the debug simulator build you are profiling, then remove that wiring after profiling.

## Symbolication Gate

Do not draw conclusions from an unsymbolicated flamegraph. Before every capture, prepare a dSYM folder that includes the app dSYM and any embedded first-party dynamic framework dSYMs.

Collect dSYMs after the final build that produced the installed app:

```bash
SKILL_DIR="<absolute path to this loaded skill folder>"
APP="<path-to-built-simulator-App.app>"
DSYMS="$RUN_DIR/dsyms"

"$SKILL_DIR/scripts/collect_ios_dsyms.sh" \
  --app "$APP" \
  --out-dir "$DSYMS" \
  --search-root "$(dirname "$APP")" \
  --search-root "$PWD" \
  --extra-dsym "$RUN_DIR/ETTrace-iphonesimulator.xcarchive/dSYMs/ETTrace.framework.dSYM"
```

Add `--require-framework <FrameworkName>` for app-owned dynamic frameworks that must symbolicate; use `--require-all-frameworks` only when every embedded framework is app-owned or expected to have symbols. If the helper reports a missing required app or framework dSYM, rebuild the exact simulator app with dSYM generation before tracing, or add the build output directory that contains those dSYMs as another `--search-root`.

Verify important UUIDs before tracing when the report looks suspicious:

```bash
dwarfdump --uuid "$APP/$(/usr/libexec/PlistBuddy -c 'Print :CFBundleExecutable' "$APP/Info.plist")"
find "$DSYMS" -maxdepth 1 -type d -name '*.dSYM' -print -exec dwarfdump --uuid {} \;
```

After ETTrace exits, read its symbolication summary. Treat meaningful first-party "have library but no symbol" lines as a failed trace unless they are tiny noise. Unsymbolicated system-framework or ETTrace internal buckets are usually acceptable.

## Capture

For launch traces:

```bash
cd "$RUN_DIR"
CAPTURE_MARKER="$RUN_DIR/.ettrace-capture-start"
: > "$CAPTURE_MARKER"
find "$RUN_DIR" -maxdepth 1 \( -name 'output.json' -o -name 'output_*.json' \) -delete
ettrace --simulator --launch --verbose --dsyms "$DSYMS"
```

Use `--launch` only when measuring startup or first render. The first launch connection can force quit the app; relaunch from the simulator home screen rather than Xcode if prompted. For first-launch-after-install traces, temporarily set `ETTraceRunAtStartup=YES` in the app Info.plist, then run `ettrace --simulator` and launch from the home screen.

For runtime flow traces:

```bash
cd "$RUN_DIR"
CAPTURE_MARKER="$RUN_DIR/.ettrace-capture-start"
: > "$CAPTURE_MARKER"
find "$RUN_DIR" -maxdepth 1 \( -name 'output.json' -o -name 'output_*.json' \) -delete
ettrace --simulator --verbose --dsyms "$DSYMS"
```

Start from a stable screen, start ETTrace, perform exactly one focused flow, wait until visible work is complete, then stop the runner. For wider attribution, add `--multi-thread`; otherwise start with the main thread.

Run `ettrace` with the current host’s supported TTY/interactive terminal facility and answer prompts through its documented input action. If interactive input is unavailable, report the limitation and have the user run the exact command in a local terminal. Without a TTY, the runner can exit without a useful trace.

## Preserve Outputs

The next ETTrace run can overwrite processed flamegraph files, so preserve fresh `output_<thread-id>.json` files immediately. Do not analyze a saved `output.json`; ETTrace also serves a viewer route with that name, and raw `emerge-output/output.json` files are not the processed flamegraph artifacts this workflow expects.

```bash
PRESERVED_DIR="$(mktemp -d "$RUN_DIR/run-$(date +%Y%m%d-%H%M%S).XXXXXX")"
: > "$PRESERVED_DIR/summary.txt"
if [ ! -e "$CAPTURE_MARKER" ]; then
  echo "error: capture marker missing; start a fresh ETTrace capture before preserving outputs" >&2
  exit 1
fi
find "$RUN_DIR" -maxdepth 1 -name 'output_*.json' -newer "$CAPTURE_MARKER" -print | while IFS= read -r json; do
  preserved="$PRESERVED_DIR/${json##*/}"
  cp "$json" "$preserved"
  {
    echo "## ${preserved##*/}"
    python3 "$SKILL_DIR/scripts/analyze_flamegraph_json.py" "$preserved"
  } >> "$PRESERVED_DIR/summary.txt"
done
if [ ! -s "$PRESERVED_DIR/summary.txt" ]; then
  echo "error: no fresh processed ETTrace output JSON found in $RUN_DIR" >&2
  exit 1
fi
```

Analyze only processed `output_*.json` files in `RUN_DIR`. Ignore `output.json` and raw `emerge-output/output.json` files unless debugging ETTrace itself. If the analyzer rejects the JSON shape, capture again with the Homebrew ETTrace runner and matching app-side `ETTrace.xcframework` tag instead of trying to interpret the rejected file.

## Read The Profile

Start from `run-*/summary.txt`, then inspect processed JSON directly if needed.

Report:

- exact flow, app build, simulator model/runtime, and run count
- processed flamegraph JSON paths
- top active leaves and inclusive first-party stacks with sample weights or percentages
- whether symbols were complete for app-owned binaries
- caveats such as first-run setup, simulator-only cost, network variance, or low sample count
- before/after deltas only when the same flow was captured with comparable setup


## Cleanup

Remove temporary ETTrace app wiring when profiling is complete unless the user asked to keep it. Keep or discard run artifacts based on the active task.
