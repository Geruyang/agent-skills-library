# Zoom

Zoom connects Codex to Zoom meeting context through the Zoom app connector and provides developer workflows for planning, building, debugging, and reviewing Zoom integrations across APIs, SDKs, webhooks, WebSockets, bots, and automation use cases.

## Plugin Shape

This repository is packaged as a Codex plugin:

- plugin manifest: [`.codex-plugin/plugin.json`](https://github.com/openai/plugins/blob/main/plugins/zoom/.codex-plugin/plugin.json)
- Zoom app mapping: [`.app.json`](.app.json)
- deterministic command workflows: [`commands/`](https://github.com/openai/plugins/blob/main/plugins/zoom/commands)
- focused reviewer agents: [`agents/`](agents/)
- explicit-only developer workflows and references: [`skills/`](../../../../skills)
- branding and screenshot assets: [`assets/`](assets/)

This plugin contains the Zoom app connector mapping, local developer guidance, commands, skills, reviewer agents, and branding assets.

## Upstream Source

- Repo: [zoom/zoom-plugin-codex](https://github.com/zoom/zoom-plugin-codex)
- Imported commit: `6f30034c94b4594daaf814cd9bf4cf972b90a323`
- Local plugin id: `zoom`

## What Zoom Does In Codex

Use `Zoom` when you want Codex to:

- search Zoom meetings by topic, attendee, or content
- retrieve summaries, transcripts, recordings, and related meeting assets
- pull meeting context into coding, documentation, or follow-up workflows
- choose the right Zoom product surface for an integration
- build Zoom REST API, SDK, webhook, WebSocket, bot, and automation workflows
- debug Zoom auth, event delivery, SDK, and API issues

## Using In Codex

Codex can use this plugin through the Zoom app connector plus command, skill, and reviewer-agent surfaces:

- install the plugin from `/plugins`
- authenticate the Zoom app connector when Codex prompts for it
- mention the plugin as `@Zoom` if the UI exposes it
- use natural language requests that need live Zoom meeting context
- use slash commands for deterministic flows such as `/setup-zoom-oauth`, `/debug-zoom-auth`, `/debug-zoom-webhook`, and `/zoom-integration-doctor`
- invoke a bundled skill explicitly with `$skill-name`, for example `$start` or `$setup-zoom-oauth`

The Zoom app connector auth is managed by Codex. It is not exposed as a shell environment variable or raw bearer token.

The developer skills in this curated package are explicit-only: each bundled developer skill has an `agents/openai.yaml` file with `policy.allow_implicit_invocation: false`, so they are available when invoked directly but should not be selected implicitly from normal task wording.

## Command Workflows

Use the bundled slash commands when you want a deterministic flow rather than open-ended routing:

| Command | Description |
|---|---|
| [`/plan-zoom-product`](https://github.com/openai/plugins/blob/main/plugins/zoom/commands/plan-zoom-product.md) | Choose the right Zoom product surface for a use case and explain the tradeoffs clearly |
| [`/plan-zoom-integration`](https://github.com/openai/plugins/blob/main/plugins/zoom/commands/plan-zoom-integration.md) | Turn a Zoom product idea into a practical build plan with auth, architecture, and milestones |
| [`/debug-zoom`](https://github.com/openai/plugins/blob/main/plugins/zoom/commands/debug-zoom.md) | Triage a broken Zoom integration when the failing layer is not yet obvious |
| [`/setup-zoom-oauth`](https://github.com/openai/plugins/blob/main/plugins/zoom/commands/setup-zoom-oauth.md) | Inspect the repo, choose the right Zoom OAuth flow, and wire the auth path cleanly |
| [`/setup-zoom-webhooks`](https://github.com/openai/plugins/blob/main/plugins/zoom/commands/setup-zoom-webhooks.md) | Implement or correct a Zoom webhook receiver with validation, signature checks, and reliable delivery handling |
| [`/setup-zoom-websockets`](https://github.com/openai/plugins/blob/main/plugins/zoom/commands/setup-zoom-websockets.md) | Implement or correct a Zoom WebSocket event stream with connection lifecycle and reconnect handling |
| [`/debug-zoom-auth`](https://github.com/openai/plugins/blob/main/plugins/zoom/commands/debug-zoom-auth.md) | Isolate OAuth, SDK auth, or token lifecycle failures and propose the minimal fix |
| [`/debug-zoom-webhook`](https://github.com/openai/plugins/blob/main/plugins/zoom/commands/debug-zoom-webhook.md) | Triage webhook registration, signature validation, delivery, and handler issues |
| [`/zoom-integration-doctor`](https://github.com/openai/plugins/blob/main/plugins/zoom/commands/zoom-integration-doctor.md) | Run a read-first integration audit across auth, SDK/API choice, and eventing |

## Build Commands

Use the bundled build commands when you want Codex to drive a specific Zoom implementation path:

| Command | Description |
|---|---|
| [`/build-zoom-rest-api-app`](https://github.com/openai/plugins/blob/main/plugins/zoom/commands/build-zoom-rest-api-app.md) | Implement a Zoom REST API integration with the right resources, auth path, and verification loop |
| [`/build-zoom-apps-sdk-app`](https://github.com/openai/plugins/blob/main/plugins/zoom/commands/build-zoom-apps-sdk-app.md) | Implement a Zoom Apps SDK app that runs inside the Zoom client with the right running context and auth path |
| [`/build-zoom-meeting-app`](https://github.com/openai/plugins/blob/main/plugins/zoom/commands/build-zoom-meeting-app.md) | Implement an embedded or managed Zoom meeting flow in the current codebase |
| [`/build-zoom-meeting-sdk-app`](https://github.com/openai/plugins/blob/main/plugins/zoom/commands/build-zoom-meeting-sdk-app.md) | Implement a Zoom Meeting SDK integration with the right platform-specific join or start flow |
| [`/build-zoom-video-sdk-app`](https://github.com/openai/plugins/blob/main/plugins/zoom/commands/build-zoom-video-sdk-app.md) | Implement a custom Zoom Video SDK session workflow |
| [`/build-zoom-ui-toolkit-app`](https://github.com/openai/plugins/blob/main/plugins/zoom/commands/build-zoom-ui-toolkit-app.md) | Implement a Zoom Video SDK UI Toolkit integration for a prebuilt web session UI |
| [`/build-zoom-cobrowse-app`](https://github.com/openai/plugins/blob/main/plugins/zoom/commands/build-zoom-cobrowse-app.md) | Implement a Zoom Cobrowse integration with session lifecycle, privacy controls, and support workflow wiring |
| [`/build-zoom-rivet-app`](https://github.com/openai/plugins/blob/main/plugins/zoom/commands/build-zoom-rivet-app.md) | Implement a server-side Zoom integration with Rivet modules for auth, APIs, and webhooks |
| [`/build-zoom-probe-flow`](https://github.com/openai/plugins/blob/main/plugins/zoom/commands/build-zoom-probe-flow.md) | Implement readiness checks with Zoom Probe SDK before users join meetings or sessions |
| [`/build-zoom-rtms-app`](https://github.com/openai/plugins/blob/main/plugins/zoom/commands/build-zoom-rtms-app.md) | Implement a Zoom RTMS workflow for live media, transcript, or event-stream processing |
| [`/build-zoom-scribe-app`](https://github.com/openai/plugins/blob/main/plugins/zoom/commands/build-zoom-scribe-app.md) | Implement a Zoom Scribe transcription pipeline for uploaded or stored media |
| [`/build-zoom-bot`](https://github.com/openai/plugins/blob/main/plugins/zoom/commands/build-zoom-bot.md) | Implement a Zoom meeting bot, recorder, or real-time media workflow |
| [`/build-zoom-team-chat-app`](https://github.com/openai/plugins/blob/main/plugins/zoom/commands/build-zoom-team-chat-app.md) | Implement a Zoom Team Chat integration or chatbot flow |
| [`/build-zoom-phone-integration`](https://github.com/openai/plugins/blob/main/plugins/zoom/commands/build-zoom-phone-integration.md) | Implement a Zoom Phone integration around APIs, Smart Embed, or events |
| [`/build-zoom-contact-center-app`](https://github.com/openai/plugins/blob/main/plugins/zoom/commands/build-zoom-contact-center-app.md) | Implement a Zoom Contact Center integration for web, mobile, or backend workflows |
| [`/build-zoom-virtual-agent`](https://github.com/openai/plugins/blob/main/plugins/zoom/commands/build-zoom-virtual-agent.md) | Implement a Zoom Virtual Agent integration for web or mobile wrappers |

## Reviewer Agents

The plugin also bundles focused reviewer agents for specialist analysis:

| Agent | Description |
|---|---|
| [`zoom-oauth-scope-auditor`](agents/zoom-oauth-scope-auditor.md) | Review scope sets for least privilege, missing scopes, and cross-surface mistakes |
| [`zoom-integration-reviewer`](agents/zoom-integration-reviewer.md) | Review a Zoom integration end to end for architectural, auth, webhook, and SDK risks |

## Primary Workflows

Invoke developer skills explicitly by mentioning a skill such as `$start` or `$setup-zoom-oauth`.

| Skill | Description |
|---|---|
| [`start`](../../../../skills/x-openai-start-120ae45/SKILL.md) | Start with a Zoom app idea and route to the right product and build path |
| [`setup-zoom-oauth`](../../../../skills/x-openai-setup-zoom-oauth-442899b/SKILL.md) | Choose the auth model, scopes, and redirect flow for a Zoom app |
| [`build-zoom-meeting-app`](../../../../skills/x-openai-build-zoom-meeting-app-c3f8e89/SKILL.md) | Build an embedded or managed Zoom meeting flow |
| [`build-zoom-bot`](../../../../skills/x-openai-build-zoom-bot-0582b85/SKILL.md) | Build bots, recorders, and real-time meeting processors |
| [`debug-zoom`](../../../../skills/x-openai-debug-zoom-2565b25/SKILL.md) | Triage a broken Zoom integration and isolate the failing layer |
| [`build-zoom-rest-api-app`](../../../../skills/x-openai-build-zoom-rest-api-app-fa8ade3/SKILL.md) | Route into Zoom REST endpoints, scopes, and resource patterns |
| [`build-zoom-meeting-sdk-app`](../../../../skills/x-openai-build-zoom-meeting-sdk-app-f579820/SKILL.md) | Route into embedded Zoom meeting implementation details |
| [`build-zoom-video-sdk-app`](../../../../skills/x-openai-build-zoom-video-sdk-app-93497e9/SKILL.md) | Route into custom video-session implementation details |
| [`build-zoom-rtms-app`](../../../../skills/x-openai-zoom-rtms-ae86f57/SKILL.md) | Route into Zoom RTMS for live media, transcript, and event-stream workflows |
| [`setup-zoom-webhooks`](../../../../skills/x-openai-setup-zoom-webhooks-e8837c7/SKILL.md) | Set up Zoom webhook subscriptions, signature verification, and handlers |
| [`setup-zoom-websockets`](../../../../skills/x-openai-setup-zoom-websockets-c8c09ef/SKILL.md) | Set up Zoom WebSocket event delivery when it fits better than webhooks |
| [`build-zoom-team-chat-app`](../../../../skills/x-openai-build-zoom-team-chat-app-dc08987/SKILL.md) | Build Team Chat user or chatbot integrations |
| [`build-zoom-phone-integration`](../../../../skills/x-openai-build-zoom-phone-integration-e2a7e6c/SKILL.md) | Build Zoom Phone integrations around Smart Embed, APIs, and events |
| [`build-zoom-contact-center-app`](../../../../skills/x-openai-build-zoom-contact-center-app-20fb7cf/SKILL.md) | Build Contact Center app, web, or native integrations |
| [`build-zoom-virtual-agent`](../../../../skills/x-openai-build-zoom-virtual-agent-6f67c33/SKILL.md) | Build Virtual Agent web or mobile wrapper integrations |

## Supporting References

The plugin keeps the Zoom product-specific reference library under `skills/`. These are supporting references, not the primary entry surface:

- [`skills/general/`](../../../../skills/x-openai-zoom-general-37cf44c/SKILL.md)
- [`skills/rest-api/`](../../../../skills/x-openai-build-zoom-rest-api-app-fa8ade3/SKILL.md)
- [`skills/meeting-sdk/`](../../../../skills/x-openai-build-zoom-meeting-sdk-app-f579820/SKILL.md)
- [`skills/video-sdk/`](../../../../skills/x-openai-build-zoom-video-sdk-app-93497e9/SKILL.md)
- [`skills/webhooks/`](../../../../skills/x-openai-setup-zoom-webhooks-e8837c7/SKILL.md)
- [`skills/websockets/`](../../../../skills/x-openai-setup-zoom-websockets-c8c09ef/SKILL.md)
- [`skills/rtms/`](../../../../skills/x-openai-zoom-rtms-ae86f57/SKILL.md)
- [`skills/oauth/`](../../../../skills/x-openai-zoom-oauth-13e78b7/SKILL.md)

## Example Prompts

```text
Search my recent Zoom meetings for the discussion about SDK migration.
```

```text
Use $start to plan an internal meeting assistant that extracts action items and stores summaries.
```

```text
Run /build-zoom-meeting-app to add a Zoom join flow to this React app with the right auth and server-side pieces.
```

```text
Run /debug-zoom-webhook to diagnose why Zoom events reach the endpoint but signature validation fails.
```

```text
Run /plan-zoom-product for an internal meeting assistant that needs summaries, action items, and follow-up docs so we pick the right Zoom surface first.
```
