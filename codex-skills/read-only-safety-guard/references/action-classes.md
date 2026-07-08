# Action classes

| Class | Meaning | Examples |
|---|---|---|
| Read | Observes existing state without durable external change | list/get/search, bounded logs, `docker ps`, `docker inspect`, status queries |
| Local write | Changes files or local durable state | edit config, generate artifact, create cache, install a skill |
| Remote write | Changes an external system | update Meraki settings, modify dashboard, create ticket, send message |
| Lifecycle | Changes running state | start, stop, restart, deploy, scale, reboot, acknowledge |
| Destructive | Removes or irreversibly changes state | delete, prune, revoke, reset, overwrite, purge |
| Transmission | Sends data to another party/system | upload, post, email, webhook, form submission |
| Ambiguous | Generic capability whose operation determines risk | shell, SQL, arbitrary API call, browser/computer use, code execution |

## Classification rules

- Classify by effect, not command name.
- Treat dry-run or validation as read-only only when documentation guarantees no writes.
- Treat authentication/login side effects separately from data reads.
- A local cache write is still a write, even if operationally low risk.
- A read through a privileged socket remains high-capability; restrict the command and scope.
- When uncertain, stop at the read boundary and state the uncertainty.

## Safer substitutions

- update -> get current configuration and propose a patch
- restart -> inspect state, health, restart count, and logs
- prune -> report disk use and reclaimable space
- deploy -> validate configuration and produce a deployment plan
- acknowledge alert -> summarize alert and recommend ownership
- broad scan -> probe only explicitly approved targets
