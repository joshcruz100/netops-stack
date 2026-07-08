# Health-check matrix

| Source | Minimum live proof | Core checks | Degraded-access handling |
|---|---|---|---|
| Meraki | organization read | inventory, device status, uplinks/VPN, sensors, licensing, firmware, events, admins | retain successful scopes; label timeouts and stale data |
| Docker | formatted `docker ps -a` | state, health, restarts, stats, disk, ports, images, Compose, bounded logs | classify CLI/socket/daemon failure; skip dependent commands |
| Globalping | one approved target measurement | DNS, ping, traceroute, HTTP/TLS, TCP | skip without an approved target or available server |
| Prometheus | successful bounded query | saturation, errors, latency, restarts, capacity | report missing URL/auth/query failure |
| Grafana | successful health or alert read | firing alerts, dashboards, annotations, related metrics/logs | report missing URL/token/access |

## Normalized check states

- `healthy`: live evidence is within defined expectations.
- `degraded`: live evidence shows a problem or materially incomplete service.
- `failed`: the check ran and conclusively failed.
- `skipped`: prerequisite, target, authorization, or tool is unavailable.
- `unknown`: evidence is contradictory or insufficient.

## Change classes

- newly failing or newly offline
- worsened severity
- recovered or alert cleared
- inventory addition or removal
- configuration/version drift observed through read-only data
- monitoring-access regression or recovery

Never compare current partial counts directly with a complete baseline without labeling the comparison unreliable.
