# Meraki audit matrix

| Area | Evidence | Flag when |
|---|---|---|
| Inventory | organizations, networks, devices, administrators | unexpected addition/removal, role change, incomplete scope |
| Device state | status and last reported | offline, dormant, unreachable, alerting, or stale beyond the agreed threshold |
| Uplinks | status, loss, latency, public/WAN state | failed, degraded, flapping, sustained loss, or abnormal latency |
| AutoVPN | peer/tunnel state | expected peer is disconnected, unstable, or degraded |
| Wireless | AP state and relevant events | AP offline, authentication/DHCP failures, repeated channel/connectivity issues |
| Switching | switch and port status/events | switch offline, uplink/port flaps, power or error patterns |
| Sensors | battery, metrics, alerting state, last report | low battery, active threshold, stale telemetry, repeated alert |
| Cameras | camera status and connectivity events | offline, dormant, or repeated connectivity/storage symptom |
| Cellular | gateway/uplink state | inactive, failed, or degraded cellular path |
| Licensing | model, compliance, expiration | non-compliant or approaching agreed warning window |
| Firmware | configured/running version and upgrade state | mismatch, failed upgrade, staged issue, or broad version drift |
| Events | bounded recent events | repeated or newly severe operational pattern |

## Completeness

- Mark a scope complete only after its live paginated query finishes.
- Use cached pages only when linked from the current response; label their observation time.
- Do not compare totals from a partial current run with a complete baseline.
- Group identical repeated events by type, scope, count, and time range.
