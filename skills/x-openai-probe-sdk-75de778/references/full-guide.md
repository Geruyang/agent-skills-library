# Zoom Probe SDK

Background reference for preflight diagnostics on user devices and networks before meeting or session workflows.

Official docs:
- https://developers.zoom.us/docs/probe-sdk/
- https://marketplacefront.zoom.us/sdk/probe/index.html

Reference sample:
- https://github.com/zoom/probesdk-web

## Routing Guardrail

- Use Probe SDK when the user needs client-side diagnostics and readiness scoring (device/network/browser capability), not meeting/session join.
- If user needs embedded meeting flows, route to [../meeting-sdk/SKILL.md](../../x-openai-build-zoom-meeting-sdk-app-f579820/SKILL.md).
- If user needs custom real-time session UX, route to [../video-sdk/SKILL.md](../../x-openai-build-zoom-video-sdk-app-93497e9/SKILL.md).
- If user needs backend orchestration of events/APIs, chain with [../rivet-sdk/SKILL.md](../../x-openai-rivet-sdk-cdbf846/SKILL.md), [../oauth/SKILL.md](../../x-openai-zoom-oauth-13e78b7/SKILL.md), and [../rest-api/SKILL.md](../../x-openai-build-zoom-rest-api-app-fa8ade3/SKILL.md).

## Quick Links

Start here:
1. [probe-sdk.md](../probe-sdk.md)
2. [concepts/architecture-and-lifecycle.md](../concepts/architecture-and-lifecycle.md)
3. [scenarios/high-level-scenarios.md](../scenarios/high-level-scenarios.md)
4. [examples/diagnostic-page-pattern.md](../examples/diagnostic-page-pattern.md)
5. [examples/comprehensive-network-pattern.md](../examples/comprehensive-network-pattern.md)
6. [references/probe-reference-map.md](probe-reference-map.md)
7. [references/environment-variables.md](environment-variables.md)
8. [references/versioning-and-compatibility.md](versioning-and-compatibility.md)
9. [references/samples-validation.md](samples-validation.md)
10. [references/source-map.md](source-map.md)
11. [troubleshooting/common-issues.md](../troubleshooting/common-issues.md)
12. [RUNBOOK.md](../RUNBOOK.md)

## Common Lifecycle Pattern

1. Initialize `Prober` / `Reporter`.
2. Request media permissions and enumerate devices.
3. Run targeted diagnostics (`diagnoseAudio`, `diagnoseVideo`).
4. Run comprehensive network diagnostic (`startToDiagnose`) and stream stats to UI.
5. Produce final report and apply readiness gates.
6. Stop/cleanup (`stopToDiagnose`, `stopToDiagnoseVideo`, `releaseMediaStream`, `cleanup`).

## High-Level Scenarios

- Pre-join diagnostics page before Meeting SDK join action.
- Support workflow that captures structured report for customer troubleshooting.
- Device certification flow for kiosk or controlled endpoint environments.
- Browser capability gating for advanced media features.

See [scenarios/high-level-scenarios.md](../scenarios/high-level-scenarios.md) for details.

## Chaining

- Meeting pre-join gate: [../meeting-sdk/web/SKILL.md](../../x-openai-zoom-meeting-sdk-web-c3851c6/SKILL.md)
- Video session readiness gate: [../video-sdk/web/SKILL.md](../../x-openai-zoom-video-sdk-web-0622b99/SKILL.md)
- Telemetry/report ingestion backend: [../rivet-sdk/SKILL.md](../../x-openai-rivet-sdk-cdbf846/SKILL.md) + [../rest-api/SKILL.md](../../x-openai-build-zoom-rest-api-app-fa8ade3/SKILL.md)

## Environment Variables

- See [references/environment-variables.md](environment-variables.md) for optional `.env` keys and how to source values.

## Operations

- [RUNBOOK.md](../RUNBOOK.md) - 5-minute preflight and debugging checklist.
