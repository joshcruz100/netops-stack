# Probe strategy

## Default progression

1. Start with one probe near the expected user region.
2. Add two geographically distinct probes only when regional comparison matters.
3. Repeat only when distinguishing transient loss from a persistent problem.
4. Keep target, protocol, port, and request path identical across comparisons.

## Interpretation

- DNS: compare answer presence and expected records; resolver or CDN variation can be legitimate.
- HTTP: record final status, redirects, timing, and certificate evidence without reproducing sensitive content.
- TLS: warn at the configured threshold; default to 30 days when none is supplied.
- Ping: packet loss or ICMP blocking does not prove application outage.
- Traceroute: path differences are diagnostic context, not proof of fault by themselves.
- TCP: test only explicitly approved ports; success proves reachability, not application correctness.

## Safe bounds

- Avoid wildcard domains and CIDR targets.
- Avoid broad multi-port checks.
- Avoid more probes than needed for the stated regional question.
- Stop if the target resolves to a private, loopback, link-local, multicast, or cloud metadata address.
