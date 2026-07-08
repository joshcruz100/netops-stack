# Environment comparison checklist

| Layer | Compare |
|---|---|
| Automation | kind, status, destination, target thread, schedule, prompt |
| Host | local/remote host, operating system, user identity |
| Workspace | project ID, cwd, checkout/worktree, readable roots |
| Trust | trusted project status and project-local config eligibility |
| Configuration | effective profile, precedence, startup-loaded versus dynamic settings |
| Permissions | filesystem roots, Unix sockets, network destinations, approval policy |
| Runtime | PATH, CLI location/version, shell mode, Python/Node runtime |
| MCP | server enabled state, transport, cwd, secrets, tool exposure, startup/tool timeout |
| Connectors | authorization and workspace/admin restrictions |
| Timing | concurrent calls, schedule overlap, rate limits, cold-start time |
| Downstream | API, daemon, DNS, proxy, service health |

## Common signatures

- File exists but automation is denied: profile is not active in that environment.
- CLI exists but socket is denied: sandbox/socket allowlist differs.
- MCP local probe works but API calls time out: downstream path, not MCP process startup.
- Interactive tool exists but automation lacks it: different plugin/MCP loading or host.
- Works after restart only: setting is loaded at process/thread initialization.
- Broad parallel run fails while serial probe works: rate limit, fan-out, or timeout pressure.
