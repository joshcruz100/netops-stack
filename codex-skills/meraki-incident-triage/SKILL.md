---
name: meraki-incident-triage
description: Investigate a focused Cisco Meraki incident without changing configuration. Use for one offline or unstable device, network outage, uplink failure, AutoVPN problem, wireless or DHCP issue, switch-port event, camera outage, cellular degradation, sensor alert, or a specific Meraki error and time window.
---

# Meraki Incident Triage

Build a focused evidence timeline, constrain the blast radius, and identify the most likely failing layer using read-only `meraki_magic` tools.

## Safety boundary

- Use verified read methods only.
- Do not reboot devices, bounce ports, alter SSIDs/VLANs/firewall/VPN settings, acknowledge alerts, or change configuration.
- Do not widen from one incident to a full organization audit unless evidence shows a broader scope.

## Workflow

1. Resolve the target by stable identifier: organization ID, network ID, serial, MAC, or exact client/device identifier.
2. Record the incident start, reported symptoms, expected behavior, and current impact. State assumptions when the time window is unknown.
3. Check current target status and last-reported time.
4. Determine blast radius by checking the immediate parent network and same-path peers, not the whole organization.
5. Retrieve bounded events spanning before and after the incident. Preserve timestamps and event types.
6. Follow the dependency path:
   - device power/connectivity
   - switch port or wireless association
   - DHCP/DNS/authentication
   - gateway/uplink
   - AutoVPN or external path
7. Correlate status, events, uplinks, loss/latency, firmware, and recent inventory/configuration metadata.
8. Rank at most three hypotheses by evidence. Include evidence against each hypothesis.
9. Read [references/triage-paths.md](references/triage-paths.md) for symptom-specific paths.
10. Return the next read-only check. Offer a change only if the user separately requests remediation.

## Output

- Incident scope and impact
- Current state
- Timeline of material evidence
- Blast radius
- Ranked hypotheses with confidence
- Missing or stale evidence
- Next read-only diagnostic
