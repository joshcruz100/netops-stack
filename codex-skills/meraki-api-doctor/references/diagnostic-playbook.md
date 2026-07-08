# Diagnostic playbook

## Probe order

1. `cache_stats` — confirm the MCP process responds and note read-only mode.
2. `get_mcp_config` — inspect non-secret runtime configuration when needed.
3. `getOrganizations` — test authenticated Dashboard API access.
4. One organization-scoped read — separate global from tenant-specific failure.
5. The original endpoint with minimal scope and bounded pagination.

## Symptom matrix

| Symptom | Likely layer | Next read-only test |
|---|---|---|
| Local method responds; every Dashboard read times out | upstream API, DNS, proxy, or credentials path | retry one cheap Dashboard read and record duration |
| Authentication error | credentials | confirm configured credential source without printing the secret |
| 403 or permission error | Dashboard role or organization scope | test the same read against another authorized organization |
| 429 | rate limit | stop parallel calls, honor retry timing, and retry one bounded request |
| Empty array with success | legitimate empty scope or wrong organization/network ID | verify parent inventory and identifiers |
| Response marked truncated | MCP response limit | use `get_cached_response` with offset and limit |
| Only one endpoint fails | endpoint parameters, SDK mismatch, or API defect | inspect method metadata and minimize parameters |
| Intermittent long latency | upstream degradation or excessive fan-out | run sequential cheap probes and compare durations |

## Safe method selection

- Prefer dedicated `get*` and `list*` tools.
- Use `search_methods` to locate a read method.
- Use `get_method_info` to verify parameters.
- Use `call_meraki_api` only after confirming the method begins with `get` or `list`.
- Treat cache paths and API output as potentially sensitive; summarize rather than reproduce unnecessary identifiers or URLs.

## Timeout discipline

- Start with one request.
- Avoid broad `Promise.all` fan-out while the service is degraded.
- Reduce page size or organization scope before increasing timeouts.
- After two equivalent timeouts, report degraded access instead of repeating the same call.
