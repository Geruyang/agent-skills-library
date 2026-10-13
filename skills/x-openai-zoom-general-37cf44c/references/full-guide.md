# Zoom General Cross-Product Guide

Background reference for cross-product Zoom developer questions. Prefer the workflow skills first, then use this file for shared platform guidance and routing detail.

## Choose Your Path

| I want to... | Use this skill |
|---|---|
| Build deterministic automation, account management, reporting, or scheduled jobs | [rest-api](../../x-openai-build-zoom-rest-api-app-fa8ade3/SKILL.md) |
| Receive event notifications over HTTP | [webhooks](../../x-openai-setup-zoom-webhooks-e8837c7/SKILL.md) |
| Receive event notifications over WebSocket | [websockets](../../x-openai-setup-zoom-websockets-c8c09ef/SKILL.md) |
| Embed Zoom meetings into an app | [meeting-sdk](../../x-openai-build-zoom-meeting-sdk-app-f579820/SKILL.md) |
| Build custom video experiences | [video-sdk](../../x-openai-build-zoom-video-sdk-app-93497e9/SKILL.md) |
| Build an app that runs inside the Zoom client | [zoom-apps-sdk](../../x-openai-zoom-apps-sdk-0178e47/SKILL.md) |
| Access live meeting media or transcripts | [rtms](../../x-openai-zoom-rtms-ae86f57/SKILL.md) |
| Transcribe uploaded or stored media | [scribe](../../x-openai-scribe-a8317f9/SKILL.md) |
| Enable collaborative browsing for support | [cobrowse-sdk](../../x-openai-zoom-cobrowse-sdk-39cc3a6/SKILL.md) |
| Build Contact Center apps and channel integrations | [contact-center](../../x-openai-build-zoom-contact-center-app-20fb7cf/SKILL.md) |
| Build Virtual Agent web or mobile chatbot experiences | [virtual-agent](../../x-openai-build-zoom-virtual-agent-6f67c33/SKILL.md) |
| Build Zoom Phone integrations | [phone](../../x-openai-build-zoom-phone-integration-e2a7e6c/SKILL.md) |
| Build Team Chat apps and integrations | [team-chat](../../x-openai-build-zoom-team-chat-app-dc08987/SKILL.md) |
| Build server-side integrations with Rivet | [rivet-sdk](../../x-openai-rivet-sdk-cdbf846/SKILL.md) |
| Run browser, device, or network preflight diagnostics | [probe-sdk](../../x-openai-probe-sdk-75de778/SKILL.md) |
| Add prebuilt UI components for Video SDK | [ui-toolkit](../../x-openai-ui-toolkit-e3fb50c/SKILL.md) |
| Implement OAuth authentication | [oauth](../../x-openai-zoom-oauth-13e78b7/SKILL.md) |

## Routing Rules

- If the user asks for meeting embed or join behavior, route to Meeting SDK before REST.
- If the user asks for a fully custom session product, route to Video SDK.
- If the user asks for account, user, meeting, recording, reporting, or scheduled automation, route to REST API.
- If the user asks for event ingestion, choose Webhooks for HTTP delivery and WebSockets for lower-latency persistent connections.
- If the user asks for live media, raw streams, or live transcripts, route to RTMS and pair it with Meeting SDK or REST only when needed.
- If the user asks for an app inside the Zoom client, route to Zoom Apps SDK.
- If auth, scopes, redirect handling, or token refresh are involved, chain OAuth guidance.

## Webhooks vs WebSockets

| Aspect | Webhooks | WebSockets |
|---|---|---|
| Connection | HTTP POST to your endpoint | Persistent WebSocket |
| Latency | Higher | Lower |
| Public endpoint | Required | Not required in the same way |
| Setup | Simpler | More operationally complex |
| Best for | Most event ingestion | Low-latency or private-network event streams |

## Common Use Cases

| Use Case | Description | Skills Needed |
|---|---|---|
| [Meeting + Webhooks + OAuth Refresh](meeting-webhooks-oauth-refresh-orchestration.md) | Create a meeting, process real-time updates, and refresh OAuth tokens safely | [rest-api](../../x-openai-build-zoom-rest-api-app-fa8ade3/SKILL.md) + [oauth](../../x-openai-zoom-oauth-13e78b7/SKILL.md) + [webhooks](../../x-openai-setup-zoom-webhooks-e8837c7/SKILL.md) |
| [Scribe Transcription Pipeline](../use-cases/scribe-transcription-pipeline.md) | Transcribe uploaded files or S3 archives | [scribe](../../x-openai-scribe-a8317f9/SKILL.md) |
| [Custom Meeting UI (Web)](../use-cases/custom-meeting-ui-web.md) | Build a custom video UI for a real Zoom meeting | [meeting-sdk](../../x-openai-build-zoom-meeting-sdk-app-f579820/SKILL.md) |
| [Meeting Automation](../use-cases/meeting-automation.md) | Schedule, update, and delete meetings programmatically | [rest-api](../../x-openai-build-zoom-rest-api-app-fa8ade3/SKILL.md) |
| [Meeting Bots](../use-cases/meeting-bots.md) | Build bots that join meetings for AI, transcription, or recording | [meeting-sdk/linux](../../x-openai-zoom-meeting-sdk-linux-7c38d37/SKILL.md) + [rest-api](../../x-openai-build-zoom-rest-api-app-fa8ade3/SKILL.md) |
| [Recording & Transcription](../use-cases/recording-transcription.md) | Download recordings and get transcripts | [webhooks](../../x-openai-setup-zoom-webhooks-e8837c7/SKILL.md) + [rest-api](../../x-openai-build-zoom-rest-api-app-fa8ade3/SKILL.md) |
| [Real-Time Media Streams](../use-cases/real-time-media-streams.md) | Access live audio, video, and transcript streams | [rtms](../../x-openai-zoom-rtms-ae86f57/SKILL.md) |
| [In-Meeting Apps](../use-cases/in-meeting-apps.md) | Build apps that run inside Zoom meetings | [zoom-apps-sdk](../../x-openai-zoom-apps-sdk-0178e47/SKILL.md) |
| [Zoom Phone Smart Embed CRM Integration](../use-cases/zoom-phone-smart-embed-crm.md) | Build CRM dialer and call logging flows | [phone](../../x-openai-build-zoom-phone-integration-e2a7e6c/SKILL.md) + [oauth](../../x-openai-zoom-oauth-13e78b7/SKILL.md) |
| [Rivet Event-Driven API Orchestrator](../use-cases/rivet-event-driven-api-orchestrator.md) | Combine webhooks and API actions through Rivet | [rivet-sdk](../../x-openai-rivet-sdk-cdbf846/SKILL.md) + [oauth](../../x-openai-zoom-oauth-13e78b7/SKILL.md) + [rest-api](../../x-openai-build-zoom-rest-api-app-fa8ade3/SKILL.md) |

## Detailed References

- [Authentication](authentication.md)
- [App types](app-types.md)
- [Scopes](scopes.md)
- [Marketplace](marketplace.md)
- [Query routing playbook](query-routing-playbook.md)
- [Automatic REST and webhook chaining](automatic-skill-chaining-rest-webhooks.md)
- [Meeting webhook and OAuth refresh orchestration](meeting-webhooks-oauth-refresh-orchestration.md)
- [Distributed meeting fallback architecture](distributed-meeting-fallback-architecture.md)
- [Community repositories](community-repos.md)
- [SDK upgrade guide](sdk-upgrade-guide.md)
- [SDK logs troubleshooting](sdk-logs-troubleshooting.md)
