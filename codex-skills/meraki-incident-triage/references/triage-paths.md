# Meraki incident triage paths

## Device offline or dormant

Check device status and last report, parent network, same-site peer state, uplink status, and bounded connectivity events. Distinguish a retired/dormant device from a newly unreachable production device.

## Network or appliance outage

Check appliance/uplink status, loss and latency, public IP transition, failover events, AutoVPN state, and whether downstream devices share the outage window.

## AutoVPN failure

Check both peer endpoints, uplink health, tunnel state, peer-specific events, and whether the failure is one tunnel, one site, or organization-wide.

## Wireless client issue

Check AP status, client association history, authentication, DHCP, DNS, roaming, and relevant wireless events. Do not infer an RF cause solely from a failed connection.

## Switch-port issue

Check switch status, port state, link changes, errors, PoE state when available, and whether the attached device appears elsewhere.

## Sensor alert

Check `alertingOn`, current metric, threshold/profile, battery, last report, and whether the value is still abnormal. Separate an active condition from a stale or cleared notification.

## Evidence ranking

Prefer timestamp-correlated status and events over static configuration metadata. Treat firmware age, naming, or topology as contributing context unless directly tied to the incident window.
