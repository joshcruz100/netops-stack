---
name: mcp-config-doctor
description: Diagnose Model Context Protocol server configuration, startup, transport, authorization, secret, tool-discovery, timeout, and approval problems in Codex. Use when an MCP server is configured but unavailable, fails to start, exposes no tools, requests missing config or secrets, times out, prompts unexpectedly, or behaves differently across threads or automations.
---

# MCP Config Doctor

Identify the failing MCP layer without exposing credentials or changing configuration unless the user explicitly requests a fix.

## Safety boundary

- Inspect first. Do not add, remove, reconfigure, restart, or authorize an MCP server during diagnosis unless requested.
- Never print secret values, bearer tokens, environment contents, or credential files.
- Redact sensitive command arguments, headers, URLs, and error output before reporting.
- Treat tool approval policy, sandbox permissions, connector authorization, and MCP server health as separate layers.

## Workflow

1. Capture the server name, expected tools, surface/thread, exact error, and last known success.
2. Confirm the server is configured and enabled in the effective Codex configuration. Inspect only relevant keys.
3. Determine transport: stdio command, streamable HTTP URL, app connector, plugin-provided server, or MCP_DOCKER gateway.
4. Test a cheap local/read-only tool when available. A successful local method proves process/transport health, not downstream API health.
5. Classify the failure using [references/failure-matrix.md](references/failure-matrix.md):
   - configuration/schema
   - executable/path/cwd
   - startup timeout
   - transport/protocol
   - missing secret or authorization
   - server tool discovery
   - per-tool timeout
   - approval or sandbox policy
   - downstream service/API
6. Compare interactive-thread and automation environments when behavior differs. Check project trust and whether project `.codex/config.toml` is loaded.
7. Use MCP catalog discovery only to confirm an exact server name or required config; do not install adjacent servers automatically.
8. Recommend the smallest fix and specify whether restart/new-thread activation is required.

## Output

- Server and transport
- Status: healthy, degraded, unavailable, or misconfigured
- Failing layer
- Redacted evidence
- Interactive versus automation differences
- Smallest corrective action
- Verification step after the fix
