# Public Equity Investing Automation Setup

Use this reference only when the user explicitly asks to create, inspect, update, pause, resume, or remove a Public Equity Investing automation, or accepts the optional automation step during saved-context onboarding.

## Default Catalog

Read `plugin-author-config/automation-config.md` from this skill's directory for the configured automation id, name, frequency, launcher, and canonical automation prompt. The catalog is an author-owned menu, not evidence that an automation exists.

## Setup Rules

1. Do not create an automation until the user explicitly accepts the configured launcher or directly asks for a recurring Public Equity Investing workflow.
2. Discover the current host's supported recurring-task capability. Use `automation_update` only if actually exposed with a matching schema. If no scheduler is available, provide the proposed schedule and prompt as local setup material; do not claim it was scheduled.
3. Before creating an automation, inspect existing schedules through the current host's documented read-only API or user-approved configuration location, matching by id, name, or prompt intent. Prefer updating a matching automation over creating a duplicate. Do not assume another product's private storage layout.
4. Prefer a follow-up attached to the current conversation when the host supports it. The `heartbeat` and `destination="thread"` fields are valid only on tools whose discovered schema defines them. If no equivalent exists, report that limitation. Keep the first version reviewable. Do not create a detached scheduled job unless the user explicitly requests one and provides an appropriate workspace.
5. Pass cadence through the automation tool's schedule field. Keep schedule details out of the automation prompt.
6. After creation or update, use `automation_update` readback when available and record concise operational metadata under `onboarding-state.json` `automations.configured.<automation-id>`.

## Prompt Requirements

Use the configured canonical automation prompt substantially verbatim. Do not replace it with a generic reminder. Preserve these requirements:

- invokes the Public Equity Investing router and applies user-context preflight before substantive work;
- reviews only saved watchlist pointers already present;
- produces only `Upcoming Catalysts`, `Stale Sources`, and `Missing Inputs`;
- includes the ticker or watchlist pointer, dated item or gap, source pointer, and as-of date when known;
- returns an honest missing-context or no-material-changes result instead of inventing a portfolio or watchlist;
- does not perform broad research or draft investment analysis;
- does not trade, send messages, edit source systems, or save new durable preferences without an explicit user request;
- remains concise and scan-friendly.

## State Metadata

Store only operational metadata under `onboarding-state.json`:

```json
{
  "automations": {
    "status": "completed",
    "configured": {
      "weekday-watchlist-brief": {
        "automation_id": "<automation id>",
        "name": "Weekday Public Equity Watchlist Brief",
        "kind": "heartbeat",
        "status": "ACTIVE"
      }
    }
  }
}
```

Do not copy automation metadata into `user-context.md`. Do not treat saved metadata as proof that the live automation still exists; inspect live automation state when a user asks about status or changes.

## Cleanup

Ask for explicit confirmation before deleting, replacing, or disabling a Public Equity Investing automation. After an approved cleanup, update the matching operational metadata instead of silently removing the history.
