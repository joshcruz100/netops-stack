# Target-list schema

Store target lists as JSON:

```json
{
  "version": 1,
  "targets": [
    {
      "id": "public-web",
      "enabled": true,
      "target": "https://example.com/health",
      "checks": ["dns", "http", "tls"],
      "expect": {
        "http_status": [200],
        "tls_warn_days": 30
      },
      "regions": ["north-america", "europe"],
      "owner": "platform",
      "notes": "Public health endpoint"
    }
  ]
}
```

## Fields

- `version`: integer schema version; currently `1`.
- `id`: unique lowercase identifier using letters, numbers, and hyphens.
- `enabled`: whether automated checks may run.
- `target`: hostname, public IP, or HTTP/HTTPS URL. Do not include credentials.
- `checks`: subset of `dns`, `http`, `tls`, `ping`, `traceroute`, and `tcp`.
- `port`: required for hostname/IP TCP checks; integer 1–65535.
- `expect`: expected HTTP statuses, TLS warning days, or other documented thresholds.
- `regions`: optional approved region labels.
- `owner`: accountable team or context, not personal secrets.
- `notes`: optional non-sensitive context.

Targets must not be wildcards, CIDRs, localhost, private/link-local/multicast IPs, or cloud metadata endpoints.
