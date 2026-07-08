---
name: meraki-api-doctor
description: Diagnose Meraki MCP and Dashboard API failures without changing Meraki configuration. Use when meraki_magic is slow, times out, returns truncated or stale data, fails authentication, hits pagination or rate limits, exposes missing methods, or behaves differently from the Meraki Dashboard.
---

# Meraki API Doctor

Diagnose the narrowest failing layer: Codex-to-MCP transport, the `meraki_magic` process, Meraki authentication, Dashboard API reachability, rate limiting, pagination, caching, or a specific API method.

## Safety boundary

- Use read-only tools and `get*`, `list*`, or search methods only.
- Never call `create*`, `update*`, `delete*`, `claim*`, `remove*`, `reboot*`, or configuration-changing endpoints.
- Treat `call_meraki_api` as potentially write-capable. Use it only with a verified read method.
- Do not rotate credentials, clear caches, restart services, or alter MCP configuration unless explicitly requested.

## Diagnostic workflow

1. Record the exact symptom, affected method, parameters excluding secrets, elapsed time, and last known successful run.
2. Prove the MCP server is alive with a cheap local method such as `cache_stats` or `get_mcp_config`. A successful local response proves only the MCP process, not Meraki API reachability.
3. Run one cheap Dashboard read such as `getOrganizations`. Do not launch broad parallel inventory calls until it succeeds.
4. If the cheap read succeeds, retry the original endpoint with the smallest scope and page size that answers the question.
5. Prefer dedicated tools over `call_meraki_api`. Use `search_methods` and `get_method_info` before a generic call when the exact SDK section or method is uncertain.
6. Handle truncated responses through `get_cached_response` using the returned cache path and bounded pages. Do not read arbitrary cache files.
7. Distinguish timeout, authentication, authorization, rate limit, empty-success, schema, and truncation failures. Read [references/diagnostic-playbook.md](references/diagnostic-playbook.md) for the symptom matrix.
8. Stop after two equivalent timeouts unless a smaller request or independent health probe can add evidence. Do not create a request storm.
9. Report the failing layer, evidence, impact, and the single most useful next read-only test.

## Output format

Return:

- **Status:** healthy, degraded, or unavailable
- **Failing layer:** transport, MCP process, credentials, Dashboard API, rate limit, endpoint, pagination/cache, or unknown
- **Evidence:** successful and failed probes with durations
- **Scope:** organizations, networks, or devices affected
- **Data confidence:** current, partial, stale, or unavailable
- **Next read-only step:** one concrete test

Never claim the Meraki environment is healthy when only a local MCP method succeeded.
