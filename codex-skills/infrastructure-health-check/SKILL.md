---
name: infrastructure-health-check
description: Run a unified read-only infrastructure health review across Meraki, local Docker, Globalping, and optional Prometheus or Grafana data. Use for scheduled health checks, operational status reviews, pre-incident baselines, daily infrastructure reports, or cross-system diagnosis that must not change configuration.
---

# Infrastructure Health Check

Coordinate the narrowest available read-only checks, preserve partial results, and produce an action-oriented report without treating missing telemetry as healthy.

## Safety boundary

- Default to read-only tools and commands.
- Do not change Meraki configuration, container state, monitoring configuration, alert rules, dashboards, or external targets.
- Probe only explicitly approved external domains, IPs, ports, or URLs. Never scan or infer a target range.
- Stop a source after two equivalent timeouts and report the gap.

## Workflow

1. Record observation time, timezone, requested scope, available tools, and approved targets.
2. Establish source health before expensive queries. Preserve independent results when another source fails.
3. For Meraki, invoke `$meraki-api-doctor` when transport or API access is degraded. Otherwise collect inventory, device state, uplinks/VPN, sensors, licensing, firmware, bounded events, and administrator changes.
4. For Docker, invoke `$docker-health-triage` and collect container state, health, restarts, resource pressure, disk use, ports, image drift, Compose validation, and bounded abnormal logs.
5. Use Globalping only for approved targets. Check DNS, HTTP/TLS, ping, traceroute, or TCP reachability from a small representative probe set.
6. Query Prometheus or Grafana only when configured. Prefer existing metrics and alerts over generating new state.
7. Normalize observations using [references/check-matrix.md](references/check-matrix.md). Separate `healthy`, `degraded`, `failed`, and `skipped` checks.
8. Compare with the last successful baseline. Invoke `$incident-diff-report` when structured snapshots are available.
9. Notify only for a new or materially worsened issue, unresolved monitoring-access failure, or approaching certificate/license deadline. Otherwise return a quiet no-action result.

## Confidence rules

- Mark a source **current** only when its live query succeeds.
- Mark cached or previous-run evidence **stale** with its timestamp.
- Mark timed-out or denied sources **unavailable**, not healthy.
- Do not infer recovery from an item disappearing in a partial response.
- Distinguish observed facts from likely causes and recommendations.

## Report format

Keep the report short:

1. Observation timestamp and overall status
2. Important changes since the last successful run
3. Meraki findings
4. Docker findings
5. External and monitoring findings
6. Skipped checks and data-access caveats
7. The single most useful next read-only diagnostic
