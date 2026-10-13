# Data Analytics Automations

Use this reference when Data Analytics is setting up, checking, repairing, or offering recurring Data Analytics automations. Keep this file as the runtime owner for automation setup.

The automation catalog is ../plugin-author-config/automation-config.md. Always read it before setup and use its Name, Frequency, and Instructions; do not duplicate focused-skill workflow rules in automation prompts.

## Default Setup

After the current semantic layer has a stable target skill path and a usable, pollable source inventory, Data Analytics offers exactly one refresh automation unless the user skips or defers it:

| Automation id | Thread | Model/thinking | Schedule | Prompt | Kickoff |
| --- | --- | --- | --- | --- | --- |
| `weekly_semantic_layer_refresh` | Dedicated projectless thread titled `Semantic Layer Weekly Source Polling`, pinned | Inherit the current host model; choose a supported research-capable configuration only when requested | Weekly Monday 9:00 AM local time | Configured `Instructions` from `automation-config.md` | Send one setup kickoff to the pinned thread |

The refresh automation is optional: do not create it before those prerequisites exist, or without explicit user approval unless the user already directly instructed Data Analytics to set up weekly polling.

Do not pass unsupported model or reasoning fields. Report configuration limits; use the host's supported inherited model unless the user selected an available alternative.

The current chat thread is not the automation target by default. Do not rename, pin, unpin, attach a heartbeat to, or send kickoff messages into the current thread while setting up Data Analytics automations unless the user explicitly chooses it. Prefer the dedicated automation target thread.

## Fast Setup Checklist

After the user approves Data Analytics automation setup:

1. Discover the current host's real scheduling, independent-task creation, naming/pinning, and task-messaging capabilities. Names such as `automation_update` describe the source host contract only; use actual documented schemas, never guessed API names. Use the actual task-list capability only to reuse a clearly matching existing pinned automation thread with the exact configured title; do not treat the current thread as reusable unless the user explicitly selected it for this automation.
2. Read `../plugin-author-config/automation-config.md` and identify the default automation id, name, frequency, and prompt.
3. For the default automation, create or reuse its dedicated projectless thread, capture the returned or reused thread id, set the exact configured title on only that thread id, pin only that thread id, and keep its thread id.
4. Create or update a recurring follow-up bound to the exact dedicated task identity, configured prompt, and weekly cadence through the advertised scheduler schema. The source host calls this a heartbeat; do not transmit its field names to another host unless that host advertises them. If an equivalent dedicated follow-up cannot be persisted, use the manual fallback below.
5. Read back the job through the actual scheduler inspection API or its documented state file. Verify its recurring follow-up kind, exact dedicated task identity, prompt, cadence, and enabled status; do not assume a Codex home path.
6. Send one kickoff message only to the pinned Semantic Layer Weekly Source Polling thread after readback succeeds: run the configured semantic-layer source polling instructions now.
7. Do not update hidden local setup or context state. Keep operational metadata in the created automation/thread artifacts and summarize the result in the current response. Do not copy semantic-layer content, polling results, source URLs, or source data into setup metadata.
8. Stop. Report the concise setup result and return to the active user request. Do not inspect focused workflow skill files or run another guided workflow unless the user picks one.

## Readiness Rules

Only say the default automation setup is complete when the default automation is heartbeat-backed, targeted to its dedicated pinned thread, read back successfully, and the Semantic Layer Weekly Source Polling kickoff has started or was explicitly deferred by the user.

Do not mark setup complete after a plain cron automation, an automation attached to the wrong thread, missing readback, missing target thread metadata, or a missing first Semantic Layer Weekly Source Polling kickoff.

If the selected scheduler cannot persist a dedicated heartbeat thread after one repair attempt, use the fallback path: leave semantic-layer refresh manual and report the limitation as a fallback rather than full setup.

Ask for explicit user approval before deleting automations, pausing automations, unpinning threads, or cleaning up duplicate/stale Data Analytics automation resources.

## Thin Prompts

Automation prompts and kickoff prompts should be thin launchers:

- Semantic Layer Weekly Source Polling: load and follow `semantic-layer/weekly-polling-automation.md` in scheduled source polling mode, using that reference's source inventory, update boundary, validation, and output contract.

Do not paste source precedence, evidence standards, update boundaries, validation commands, output examples, model names, reasoning effort, or focused-skill workflow contracts into automation prompts or kickoff messages.

## User-Facing Result

When setup succeeds, use this shape:

```md
Semantic-layer refresh is set up and read back cleanly.

- **Semantic Layer Weekly Source Polling**: checks the saved source inventory each week and posts its review summary in the pinned **Semantic Layer Weekly Source Polling** thread. I also kicked off the first source polling run in that thread.
```

When setup cannot be completed, use this shape:

```md
Weekly semantic-layer refresh is still manual because the automation could not be persisted and read back cleanly.

- **Current setup**: the semantic layer and source inventory are saved.
- **Refresh status**: manual for now. The blocker can be revisited later without repeating semantic-layer setup.
```
