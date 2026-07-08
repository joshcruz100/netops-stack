---
name: docker-health-triage
description: Perform read-only Docker and Docker Compose health diagnostics. Use when containers are unhealthy, restarting, exited, slow, resource constrained, exposing unexpected ports, failing healthchecks, producing suspicious logs, or when Docker CLI or socket access fails.
---

# Docker Health Triage

Inspect local Docker state without changing containers, images, volumes, networks, or Compose projects.

## Safety boundary

- Use only read operations: `docker ps`, `inspect`, `stats --no-stream`, `system df`, `logs`, `events --until`, `port`, `version`, `context show`, and `compose config`.
- Never run `start`, `stop`, `restart`, `kill`, `rm`, `rmi`, `prune`, `pull`, `push`, `build`, `run`, `exec`, `update`, `compose up`, or `compose down` unless explicitly requested.
- Bound logs by line count and timestamps. Inspect abnormal containers only.
- Treat Docker socket access as equivalent to powerful local control even when issuing read commands.

## Workflow

1. Verify the CLI and connection with `docker --version`, `docker context show`, and a formatted `docker ps -a`.
2. If access fails, classify it before doing anything else:
   - `permission denied` on a socket: sandbox or OS socket access
   - `cannot connect`: daemon/Desktop unavailable or wrong context
   - missing command: CLI installation or PATH
3. Inventory containers with stable fields: ID, name, image, state, status, health, ports, and creation time.
4. Inspect only abnormal or ambiguous containers for state, restart count, healthcheck output, image ID, mounts, and labels.
5. Run `docker stats --no-stream` and `docker system df` for pressure and capacity evidence.
6. Review port bindings and flag broad host bindings or sensitive administrative/database ports. Do not label an exposure a vulnerability without context.
7. Discover Compose projects from labels. Run `docker compose config --quiet` only when the source file is already within readable scope.
8. Read at most 100 timestamped log lines per abnormal container unless the user requests a different bound.
9. Read [references/commands.md](references/commands.md) for safe command forms and interpretation guidance.
10. Report evidence, likely cause, and the next read-only diagnostic. Do not implement a fix unless requested.

## Severity

- **Critical:** repeated crash loop, dead container required for service, failed healthcheck with outage evidence, or exhausted disk.
- **High:** unhealthy/restarting service, severe resource saturation, or unexpected sensitive public binding.
- **Medium:** exited service of uncertain importance, missing healthcheck, image drift, or sustained warnings.
- **Low:** hygiene or optimization issue without current service impact.

## Output format

- Overall Docker status
- Container totals by state and health
- Abnormal containers with evidence
- Resource and disk pressure
- Port exposure and missing healthchecks
- Relevant bounded-log findings
- Data-access caveats
- One next read-only command
