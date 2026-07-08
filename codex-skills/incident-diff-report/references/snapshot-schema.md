# Snapshot schema

Use this normalized JSON shape when machine comparison is useful:

```json
{
  "observed_at": "2026-07-08T09:00:00-07:00",
  "systems": {
    "meraki": {
      "complete": true,
      "entities": [
        {
          "id": "SERIAL-OR-STABLE-ID",
          "kind": "device",
          "name": "Example device",
          "status": "online",
          "severity": "ok",
          "attributes": {
            "network_id": "N_123",
            "last_reported_at": "2026-07-08T08:59:00-07:00"
          }
        }
      ]
    }
  }
}
```

## Requirements

- `observed_at`: ISO-8601 timestamp.
- `systems`: mapping of source name to source snapshot.
- `complete`: whether absence can reliably mean removal.
- `entities`: list of normalized entities.
- `id`: stable identifier within `system` and `kind`.
- `kind`: device, network, container, alert, endpoint, license, or another stable category.
- `status`: original normalized state such as online, dormant, unhealthy, or firing.
- `severity`: one of `unknown`, `info`, `ok`, `low`, `warning`, `high`, or `critical`.
- `attributes`: source-specific evidence. Avoid secrets.

The diff script keys entities by `system`, `kind`, and `id`. It reports removals only when both snapshots mark that system complete.
