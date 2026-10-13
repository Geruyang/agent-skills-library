# Network approvals and sandbox notes for image CLI mode

This reference applies only after the user explicitly selects the bundled `scripts/image_gen.py` CLI. The fallback uses the OpenAI Image API and requires outbound network access plus `OPENAI_API_KEY` supplied through an approved local credential mechanism.

Inspect the current host's network, process and filesystem policy before running the CLI. Use its actual scoped approval mechanism when required. A denied call, absent executor or missing network permission is a blocker; report it and preserve the local prompt/command handoff. Never bypass policy or change global sandbox settings merely to make the request run.

Codex-specific example: some Codex versions use `approval_policy`, `sandbox_mode`, and `[sandbox_workspace_write] network_access` in `~/.codex/config.toml`. These are product configuration fields, not universal host settings. Verify the selected Codex version's documentation before suggesting an authorized configuration change. `--ask-for-approval never` does not itself enable network access. Other hosts must use their own documented equivalents, and missing support must remain explicit.

Do not imply that installation, credential setup, network permission or image generation succeeded without actual results.
