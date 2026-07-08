---
name: meraki-health-audit
description: Run a comprehensive read-only Cisco Meraki health audit using meraki_magic. Use for organization-wide or scoped reviews of inventory, device status, uplinks, AutoVPN, wireless, switching, sensors, cameras, licensing, firmware, events, administrators, configuration drift, and changes since a prior baseline.
---

# Meraki Health Audit

Collect current Meraki evidence without changing Dashboard configuration. Preserve partial results and label unavailable scopes rather than treating them as healthy.

## Safety boundary

- Use dedicated read tools or verified `get*` and `list*` API methods only.
- Never call create, update, delete, claim, remove, reboot, bind, unbind, or configuration-changing methods.
- Do not clear caches, rotate credentials, or change MCP settings.
- Stop broad fan-out when the API is slow. Invoke `$meraki-api-doctor` for repeated timeouts or transport failures.

## Audit workflow

1. Record observation time, requested organizations/networks, comparison baseline, and data-access status.
2. Prove live Dashboard access with one cheap organization read before starting the inventory.
3. Inventory organizations, networks, devices, and administrators. Use stable IDs and serial numbers when comparing runs.
4. Retrieve device statuses and last-reported times. Flag offline, dormant, unreachable, alerting, or materially stale devices.
5. Inspect appliance and organization uplinks, loss/latency history, and AutoVPN state. Flag failed, degraded, inactive, or unstable paths.
6. Inspect wireless, switch, camera, cellular gateway, and sensor health only where those product types exist.
7. Review sensor battery state, environmental thresholds, `alertingOn`, and stale telemetry.
8. Review licensing/compliance and approaching expiration dates.
9. Review firmware status, upgrade state, configured-version mismatches, and material version drift.
10. Retrieve a bounded recent event window. Group repeated symptoms instead of listing every event.
11. Compare administrator roles and inventory against the last complete baseline. Do not claim removal from a partial response.
12. Use [references/audit-matrix.md](references/audit-matrix.md) for coverage and evidence thresholds.

## Reporting rules

- Separate observed facts, likely causes, and recommended read-only diagnostics.
- Report counts only when scope completeness is known.
- Include first/last-seen timestamps for continuing issues when available.
- Order findings by service impact, then confidence.
- Notify only for new or materially worsened issues, unresolved monitoring access, or approaching deadlines.

## Output

- Overall Meraki status and data confidence
- Inventory summary
- Offline/stale devices and active alerts
- Uplink, latency/loss, and VPN health
- Sensor, wireless, switching, camera, and cellular findings
- Licensing and firmware risks
- Recent event patterns
- Administrator and inventory changes
- One next read-only diagnostic
