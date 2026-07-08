# Container exposure risk matrix

| Evidence | Typical concern | Starting priority |
|---|---|---|
| Docker socket or equivalent runtime socket mounted | host/container control | critical |
| `privileged: true` | broad device and kernel capability access | critical/high |
| host PID/network/IPC namespace | isolation reduction and host visibility | high |
| sensitive host bind mount, especially writable | host data or configuration modification | high |
| broad device mapping | hardware/kernel attack surface | high |
| all capabilities added or dangerous capability retained | privilege escalation potential | high |
| administrative/database port on all interfaces | remotely reachable sensitive service | high/medium |
| container runs as root with writable rootfs | reduced defense in depth | medium; raise with other exposure |
| no-new-privileges absent | hardening opportunity | low/medium |
| mutable or unpinned image tag | provenance and drift risk | medium/low |

## Context that changes priority

- public versus private host reachability
- authentication and TLS at the exposed service
- host firewall or reverse proxy controls
- read-only versus writable mount
- production versus disposable development workload
- capability set, seccomp/AppArmor profile, and user namespace isolation
- whether the container processes untrusted input

Report the effective configuration and contextual uncertainty. Do not overstate a finding as exploitable without an attack path.
