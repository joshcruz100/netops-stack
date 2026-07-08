---
name: container-exposure-audit
description: Perform a read-only audit of Docker container attack surface and host exposure. Use to review published ports, host networking, privileged mode, Linux capabilities, users, writable filesystems, mounts, Docker sockets, host namespaces, devices, security options, secrets in configuration, image references, and Compose settings without changing running containers.
---

# Container Exposure Audit

Assess effective runtime exposure from Docker and Compose evidence. Do not claim exploitability from configuration alone.

## Safety boundary

- Use read-only Docker commands such as `ps`, `inspect`, `port`, `image inspect`, and `compose config` when safe.
- Do not exec into containers, scan ports, pull images, restart services, or change Compose files unless explicitly requested.
- Do not print environment values, secret contents, registry credentials, or mounted sensitive files.

## Workflow

1. Confirm Docker access and inventory in-scope containers.
2. Inspect effective runtime configuration, not only source YAML.
3. Review exposure using [references/risk-matrix.md](references/risk-matrix.md):
   - published addresses and ports
   - host network/PID/IPC namespaces
   - privileged mode and added capabilities
   - container user and root filesystem writability
   - bind mounts, devices, and Docker/host sockets
   - security options and dropped capabilities
   - environment key names and secret mechanisms
   - image tag/digest provenance
4. Correlate exposure with service purpose, host firewall, network placement, and authentication requirements.
5. Distinguish direct host-control paths from defense-in-depth gaps and informational hygiene.
6. Rank findings by reachable attack surface, privilege gained, sensitive host access, and ease of misuse.
7. Recommend mitigations as proposals only. Do not implement changes unless requested.

## Evidence rules

- `0.0.0.0` or `::` means all host interfaces, but actual external reachability also depends on host/network controls.
- A mounted Docker socket is a high-impact host-control path.
- `privileged: true`, host namespaces, broad devices, and sensitive bind mounts require strong justification.
- Running as root is not automatically a vulnerability; evaluate capabilities, mounts, namespaces, and isolation together.
- Mutable tags indicate provenance/drift risk, not proof of compromise.

## Output

- Scope and Docker-access status
- Critical/high exposure paths
- Published-port inventory
- Privilege, namespace, capability, mount, and socket findings
- Secrets/configuration hygiene
- Image provenance observations
- Mitigation proposals and verification commands
