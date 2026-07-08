# Read-only Docker command patterns

## Connection and inventory

```bash
docker --version
docker context show
docker ps -a --format '{{json .}}'
```

If `docker ps` fails, stop and classify the connection error. Do not use `sudo` as a workaround.

## Focused inspection

```bash
docker inspect CONTAINER
docker stats --no-stream --format '{{json .}}'
docker system df
docker port CONTAINER
docker logs --tail 100 --timestamps CONTAINER
```

Use exact container IDs or validated names. Do not interpolate untrusted output into shell commands.

## Compose validation

```bash
docker compose -f /approved/path/compose.yaml config --quiet
```

Run only against an already readable Compose file. Validation may interpolate environment variables; do not print the rendered configuration because it can contain secrets.

## Interpretation notes

- `unhealthy` is direct healthcheck evidence; inspect recent health log entries.
- `restarting` plus increasing restart count indicates a crash loop.
- `exited (0)` can be normal for jobs; confirm intended service type.
- `0.0.0.0` or `::` publishes on all host interfaces; assess port sensitivity and host controls.
- High point-in-time CPU is not sufficient for a saturation claim; corroborate with repeated samples or metrics.
- Reclaimable disk is informational. Never prune in a diagnostic workflow.
