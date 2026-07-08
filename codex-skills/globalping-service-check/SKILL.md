---
name: globalping-service-check
description: Verify explicitly approved public services with Globalping using DNS, ping, traceroute, HTTP, TLS, and TCP measurements from representative global probes. Use for external availability checks, regional reachability comparisons, DNS inconsistencies, latency investigations, TLS expiry reviews, and confirmation that a reported outage is externally visible.
---

# Globalping Service Check

Measure only approved public targets and return bounded, reproducible evidence. Do not scan address ranges or discover targets implicitly.

## Authorization boundary

- Accept targets only from the user's current request or an approved target list produced by `$monitoring-target-manager`.
- Never expand a hostname into neighboring hosts, subdomains, CIDRs, or ports.
- Do not probe private, loopback, link-local, multicast, or metadata-service addresses through public probes.
- Exclude credentials, tokens, sensitive query strings, and private paths from URLs.

## Workflow

1. Resolve the approved target, measurement type, expected result, regions, and probe count.
2. Choose the least invasive measurement that answers the question:
   - DNS for resolution consistency
   - HTTP for status, response time, and TLS evidence
   - ping for ICMP latency/loss when supported
   - traceroute for path differences
   - TCP for an explicitly approved port
3. Use a small representative probe set. Read [references/probe-strategy.md](references/probe-strategy.md).
4. Run a single baseline measurement before adding regions or repetitions.
5. Compare regions only when the same target, protocol, and expectation are used.
6. Treat ICMP failure as inconclusive when HTTP or TCP succeeds.
7. Flag DNS failure/inconsistency, repeated HTTP 4xx/5xx, unexpected redirects, TCP failure, material latency/loss, or TLS expiry within the configured window.
8. Report measurement IDs/timestamps when available and distinguish probe failure from target failure.

## Output

- Approved target and expectation
- Probe locations and measurement type
- Result by region
- DNS, latency/loss, HTTP/TLS, or TCP findings
- Cross-region differences
- Confidence and caveats
- One next bounded measurement
