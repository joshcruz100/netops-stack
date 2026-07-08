---
name: compose-healthcheck-builder
description: Design, review, and validate Docker Compose healthchecks and dependency readiness behavior. Use when adding or improving healthcheck test commands, intervals, timeouts, retries, start periods, start intervals, depends_on service_healthy conditions, startup ordering, or diagnosing healthchecks that are missing, flaky, too expensive, or dependent on unavailable image tools.
---

# Compose Healthcheck Builder

Design a check that measures service readiness from inside the container, fails predictably, and does not mutate application state.

## Modes

- **Review:** inspect Compose and Dockerfile health behavior without editing.
- **Change:** modify files only when the user explicitly requests implementation.

## Workflow

1. Identify the service contract: protocol, internal port/socket, readiness condition, startup behavior, and dependencies.
2. Inspect the image/Dockerfile for an existing `HEALTHCHECK`, available shell, and installed client tools.
3. Select the least expensive reliable check. Read [references/patterns.md](references/patterns.md).
4. Prefer exec-form `CMD` when shell behavior is unnecessary. Use `CMD-SHELL` only for pipelines, interpolation, or compound logic.
5. Choose `interval`, `timeout`, `retries`, `start_period`, and optional `start_interval` from expected startup and failure-detection timing.
6. Ensure the check has a nonzero failure exit, bounded runtime, no state mutation, no external dependency unless intentional, and no secrets in output.
7. Add long-form `depends_on: condition: service_healthy` only when a dependent service truly requires readiness. Do not confuse startup ordering with runtime resilience.
8. Validate with `docker compose config --quiet`. Do not start services unless explicitly requested.
9. Explain detection time, startup grace, tool assumptions, and failure modes.

## Quality rules

- Check the service through its internal interface, not the host-published port.
- Avoid `curl` or other tools not present in the image.
- Avoid checks that write records, enqueue jobs, modify sessions, or require external Internet access.
- Avoid unrealistically short intervals or timeouts.
- Use escaped Compose interpolation such as `$$VAR` when the variable must expand inside the container.
- Do not expose credentials in YAML, command arguments, or health output.

## Output

- Proposed healthcheck YAML
- Readiness condition measured
- Timing and worst-case failure-detection estimate
- Image/tool prerequisites
- Dependency-order changes
- Validation command and remaining caveats
