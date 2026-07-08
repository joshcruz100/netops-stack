# MCP failure matrix

| Symptom | Likely layer | Read-only evidence |
|---|---|---|
| Server absent from tool list | disabled config, failed startup, lazy loading, or wrong thread | effective config, startup logs, tool catalog |
| Executable not found | command or PATH | configured command and file existence without dumping environment |
| Immediate stdio exit | bad args, cwd, dependency, or protocol output | redacted stderr and direct help/version command |
| Startup timeout | slow initialization or blocked dependency | startup duration and cheap direct process probe |
| Missing required config | catalog schema | exact required field names, not values |
| Missing required secret | credential store | secret name/presence only; never print value |
| Authorization incomplete | OAuth/connector/gateway | authorization status and requested scopes |
| Server responds; downstream calls fail | external API/service | cheap local tool versus cheap downstream read |
| One tool times out | endpoint scope, pagination, or per-tool timeout | smaller read and method metadata |
| Prompts every call | MCP/app approval mode | effective server and per-tool approval settings |
| Works interactively, fails in automation | environment, project config, sandbox, or secret availability | compare cwd, project trust, permissions, and tool exposure |
| Tool exists through gateway but not direct list | dynamic activation | gateway registry and dynamic execution capability |

## Config hygiene

- Keep URLs and non-secret schema fields separate from secret storage.
- Prefer per-server and per-tool approval settings over broad global approval.
- Use explicit startup and tool timeouts only after identifying real latency.
- Restart Codex or open a new thread when the changed surface loads configuration only at startup.
- Report conflicts with managed policy; user config cannot broaden an administrator-enforced restriction.
