# NetOps Codex agents

## Operating policy

- Default to read-only inspection. Make infrastructure, Meraki, Docker, monitoring, repository, or external-system changes only when the user explicitly requests the specific change.
- Never treat missing access, a timeout, stale telemetry, or an empty partial response as proof of health.
- Keep logs, events, metrics, and external probes bounded. Do not discover or scan unapproved targets.
- Redact credentials and secret values. Report only whether a required credential source is present and usable.
- Preserve unrelated user changes and use focused validation proportional to the requested work.
- Spawn subagents only when the user explicitly requests agents, delegation, or parallel work.

## Project agent roster

| Agent | Use for | Primary skills |
|---|---|---|
| `infrastructure_health_monitor` | Unified Meraki, Docker, external, and observability health checks | `infrastructure-health-check`, `monitoring-data-quality`, `incident-diff-report` |
| `meraki_incident_investigator` | Focused Meraki device, uplink, VPN, wireless, switching, or sensor incidents | `meraki-incident-triage`, `meraki-api-doctor`, `meraki-health-audit` |
| `docker_compose_diagnostician` | Container health, logs, Compose validation, resources, and exposure | `docker-health-triage`, `compose-healthcheck-builder`, `container-exposure-audit` |
| `observability_analyst` | Grafana, Prometheus, ClickHouse, metrics, logs, alerts, and telemetry quality | `monitoring-data-quality`, `incident-diff-report`, `infrastructure-health-check` |
| `network_change_planner` | Pre-checks, implementation plans, approvals, rollback, and validation | `network-change-plan`, `read-only-safety-guard` |
| `security_exposure_auditor` | Ports, privileges, mounts, sockets, credentials, and runtime attack surface | `container-exposure-audit`, `read-only-safety-guard` |
| `executive_operations_reporter` | Leadership-ready infrastructure and incident summaries | `executive-brief-builder`, `incident-diff-report`, `monitoring-data-quality` |

## Delegation

- Use one agent for a focused task. Use multiple agents only for independent read-heavy work whose results can be combined safely.
- Give each agent an explicit target, time window, data sources, authorization boundary, and expected output.
- Keep implementation and production changes with the main thread after explicit approval; the project agents are intentionally read-only.
- Wait for delegated agents and consolidate their evidence. Do not present duplicated or contradictory findings without reconciliation.

Example request:

> Spawn `meraki_incident_investigator`, `docker_compose_diagnostician`, and `observability_analyst` in parallel. Keep all work read-only, wait for all three, and summarize only material findings and evidence gaps.
