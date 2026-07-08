---
name: monitoring-target-manager
description: Create, review, normalize, and validate explicit allowlists of monitoring targets for Globalping and infrastructure health checks. Use when defining approved hostnames, public IPs, URLs, TCP ports, regions, expectations, ownership, or warning thresholds, or when checking a target list for unsafe, ambiguous, duplicate, or secret-bearing entries.
---

# Monitoring Target Manager

Maintain explicit monitoring authorization. Never add a discovered target without direct user approval.

## Operating modes

- **Review:** inspect and validate without changing the target file.
- **Change:** add, edit, or remove targets only when explicitly requested.

## Workflow

1. Identify the target-list file or proposed entries and whether the user requested review or modification.
2. Normalize each entry to the schema in [references/target-schema.md](references/target-schema.md).
3. Require a stable ID, enabled state, target, allowed check types, expectation, and owner/context.
4. Reject wildcard/CIDR expansion, credentials, private URLs, embedded tokens, ambiguous port ranges, and unsupported check types.
5. Deduplicate by normalized target, protocol, port, and path while preserving separate expectations only when justified.
6. Run `scripts/validate_targets.py TARGETS.json` after creating or changing JSON target lists.
7. Preview additions, removals, and behavior changes before writing when the request is ambiguous.
8. Report targets that are disabled, unsafe, incomplete, or awaiting approval.

## Authorization rules

- A target is approved only when explicitly supplied by the user or already present and enabled in the approved list.
- DNS results do not authorize probing returned IPs as independent targets.
- A hostname does not authorize sibling subdomains or additional ports.
- A URL authorizes only its scheme, hostname, explicit/default port, and configured path behavior.
- Do not store secrets, authorization headers, cookies, or sensitive query parameters.

## Output

- Valid enabled targets
- Disabled targets
- Rejected or incomplete entries with reasons
- Deduplication or normalization changes
- Exact monitoring scope granted by each entry
