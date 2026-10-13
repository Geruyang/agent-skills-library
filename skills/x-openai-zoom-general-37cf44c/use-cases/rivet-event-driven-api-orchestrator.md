# Rivet Event-Driven API Orchestrator

Use Rivet to build a Node.js backend that combines webhook event handling with Zoom REST API actions using typed module clients.

## When to Use

- You need both event-driven workflows and API calls in one service.
- You want to reduce custom OAuth/webhook boilerplate.
- You are composing multiple Zoom surfaces (Team Chat, Meetings, Users, Phone, Video SDK API).

## Skill Chain

- [rivet-sdk](../../x-openai-rivet-sdk-cdbf846/SKILL.md)
- [oauth](../../x-openai-zoom-oauth-13e78b7/SKILL.md)
- [rest-api](../../x-openai-build-zoom-rest-api-app-fa8ade3/SKILL.md)
- [team-chat](../../x-openai-build-zoom-team-chat-app-dc08987/SKILL.md)

## Architecture

```text
Zoom Events -> Rivet webEventConsumer -> business logic -> Rivet endpoints.* -> Zoom APIs
```

## High-Level Flow

1. Instantiate one or more Rivet module clients.
2. Register webhook event handlers.
3. Start receiver(s) and expose `/zoom/events` endpoint(s).
4. Call typed endpoint wrappers from event handlers.
5. Persist state/tokens and return user-visible results.

## Key Risks

- Incorrect per-module endpoint port mapping.
- OAuth redirect/state mismatch.
- Scope mismatch for endpoint calls.
- Event payload drift across versions.

## See Also

- [rivet-sdk examples](../../x-openai-rivet-sdk-cdbf846/examples/getting-started-pattern.md)
- [rivet-sdk multi-client pattern](../../x-openai-rivet-sdk-cdbf846/examples/multi-client-pattern.md)
- [rivet-sdk runbook](../../x-openai-rivet-sdk-cdbf846/RUNBOOK.md)
