# Network approvals and sandbox notes

Speech generation uses the OpenAI Audio API and requires outbound network access plus a locally configured API key. Discover the current host’s network, filesystem, and approval facilities before running the CLI.

If a request is denied, report the exact blocked operation and use the host’s documented approval flow. Do not disable approvals or change sandbox settings as a compatibility workaround. Only apply a user-authorized settings change supported by that host. If no approval mechanism is available, provide the prepared command and local execution requirements and report live generation as blocked. Never expose the key in chat, logs, or diagnostics.

This reference retains its original filename for link compatibility; it does not require a Codex configuration file.
