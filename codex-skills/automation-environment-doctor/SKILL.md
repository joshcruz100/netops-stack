---
name: automation-environment-doctor
description: Diagnose why a scheduled Codex automation, heartbeat, cron job, background thread, or worktree behaves differently from an interactive run. Use for missing tools, denied files or sockets, unavailable secrets, wrong working directory, ignored project configuration, MCP startup failures, PATH differences, timeouts, or checks that succeed manually but fail on schedule.
---

# Automation Environment Doctor

Compare interactive and automated execution layer by layer without changing the automation or environment unless the user explicitly requests a fix.

## Workflow

1. Capture the automation ID, kind, schedule, destination, workspace/project, host, and latest exact failure.
2. Establish a known-good interactive comparison using the smallest equivalent read-only command or tool call.
3. Compare the two environments using [references/environment-checklist.md](references/environment-checklist.md).
4. Identify the first divergent layer rather than attributing every failure to permissions.
5. Distinguish:
   - automation definition problem
   - workspace/cwd or project-trust problem
   - config loading or precedence problem
   - permission/sandbox problem
   - environment/PATH/runtime problem
   - MCP/connector/secret availability problem
   - timing, concurrency, or rate-limit problem
   - downstream service failure
6. Preserve evidence from independent checks. A failed Docker check does not invalidate a successful Meraki check.
7. Recommend the smallest durable fix and state whether it requires automation update, local-environment configuration, Codex restart, or a new thread.
8. Do not update or recreate the automation unless explicitly requested.

## Diagnostic discipline

- Compare effective values, not only configuration files.
- Redact secrets and environment values; report presence/source only.
- Treat a project config as inactive until project trust and load behavior are confirmed.
- Treat thread heartbeat and standalone local/worktree automation as different execution contexts.
- Do not infer that a permission profile loaded because its file exists.

## Output

- Interactive result versus automation result
- First divergent layer
- Redacted evidence
- Root cause or bounded uncertainty
- Smallest durable fix
- One verification run
