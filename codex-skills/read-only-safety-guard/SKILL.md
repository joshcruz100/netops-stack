---
name: read-only-safety-guard
description: Review commands, MCP tools, API methods, automation prompts, and operational workflows for unintended mutations or external side effects. Use when a task must remain read-only, when tool names are ambiguous, before running diagnostics against production systems, or when separating safe inspection from explicitly authorized change mode.
---

# Read-Only Safety Guard

Classify every planned action before execution and keep diagnostics within the user's authorized mode.

## Core rule

Assume read-only mode unless the user explicitly requests a change. Permission to inspect a system does not authorize fixing, restarting, acknowledging, deleting, deploying, or reconfiguring it.

## Workflow

1. Restate the authorized objective and systems in scope.
2. Inventory planned tool calls, commands, files, and external destinations.
3. Classify each action using [references/action-classes.md](references/action-classes.md).
4. Replace broad or ambiguous operations with narrower read equivalents.
5. Split mixed workflows into an executable read phase and a blocked change phase.
6. Reject mutation hidden inside a nominally diagnostic command, script, API wrapper, or generic tool.
7. Treat generic execution surfaces such as shell, `call_*_api`, SQL, Docker socket, browser UI, and arbitrary code as capability containers; classify the actual operation, not the tool label.
8. Verify bounds for logs, events, pagination, probing, and target scope.
9. Execute only read-class actions. Report blocked steps and the explicit authorization needed for each.

## Read-only invariants

- Do not create, edit, move, delete, or upload files unless explicitly requested.
- Do not start, stop, restart, exec into, update, or remove containers.
- Do not alter network, Meraki, monitoring, alert, dashboard, credential, or automation configuration.
- Do not acknowledge or close incidents or alerts.
- Do not send messages, publish reports, open tickets, or notify third parties without authorization.
- Do not broaden targets discovered during diagnostics.
- Do not bypass a sandbox or permission denial.

## Output

- Authorized mode and scope
- Allowed read actions
- Blocked or ambiguous actions with reasons
- Safer substitutions
- Required explicit authorization for any change phase

When all actions are safe, say so briefly and continue with the task.
