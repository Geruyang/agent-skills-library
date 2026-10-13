# Figma MCP config reference

First inspect the current host’s MCP settings and available tools. Connect the official endpoint `https://mcp.figma.com/mcp` using the host’s documented streamable HTTP and authentication flow. In TRAE or Claude, use that client’s actual MCP configuration schema; do not copy another client’s TOML or invent equivalent fields. Use OAuth or an authorized bearer token only where that host supports it. If connection or authentication is unavailable, report the missing capability and work from user-provided design exports without claiming a live Figma read.

## Authentication and verification

- If bearer authentication is used, keep `FIGMA_OAUTH_TOKEN` in an approved local secret/environment store visible to the host process. Never print its value; check only whether it is set.
- Preserve required `X-Figma-Region` headers and align them with the actual organization region.
- Reload the MCP connection using the host’s documented mechanism, list the actual server tools, then make a small authorized read to verify access.
- CLI, desktop, and MCP authentication can differ; do not assume one login authenticates another.

## Optional Codex configuration example

The following is specifically a Codex TOML example for a user configuring that product. Verify support in the installed version; it is not required by other hosts:

```toml
[mcp_servers.figma]
url = "https://mcp.figma.com/mcp"
bearer_token_env_var = "FIGMA_OAUTH_TOKEN"
http_headers = { "X-Figma-Region" = "us-east-1" }
```

For an actual Codex installation, use its documented configuration location (commonly `~/.codex/config.toml`) and supported client/auth settings. Do not assume historical feature flags are valid on the current version.

## Usage reminders

- The server is link-based: supply the actual Figma frame/layer URL and preserve its node ID.
- Follow the main skill’s required design-context → metadata when needed → screenshot workflow using tools actually exposed by the server. Tool names vary by integration; inspect their schemas before calling.
- Diagnose token presence, expiry, network errors, and region headers without disclosing secrets.
