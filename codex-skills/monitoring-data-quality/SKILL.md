---
name: monitoring-data-quality
description: Assess whether infrastructure monitoring evidence is complete, fresh, consistent, comparable, and trustworthy enough for health conclusions or incident decisions. Use for stale telemetry, partial inventories, truncated pages, conflicting statuses, missing targets, failed collectors, baseline comparisons, alert-count changes, or reports that may confuse unavailable monitoring with healthy systems.
---

# Monitoring Data Quality

Evaluate the evidence before interpreting system health. A monitoring failure is a finding, not proof that the monitored system is healthy or unhealthy.

## Workflow

1. Define the decision the evidence must support and the required scope/time window.
2. Inventory every source, query, timestamp, scope, page, cache, and failure.
3. Score the evidence using [references/quality-rubric.md](references/quality-rubric.md):
   - freshness
   - completeness
   - scope fidelity
   - consistency
   - comparability
   - provenance
   - granularity
4. Separate source health from monitored-system health.
5. Reconcile conflicting evidence by preferring live, direct, scoped, timestamped observations over cached summaries or inferred state.
6. Check pagination, truncation, deduplication, stable identifiers, timezones, and count denominators.
7. Determine which conclusions are supported, unsupported, or require caveats.
8. Recommend the smallest additional read-only query that would materially improve confidence.

## Hard rules

- Never treat timeout, permission denial, empty cache, or missing page as healthy.
- Never infer entity removal from a partial current inventory.
- Never compare counts whose scopes or completeness differ without labeling the comparison invalid.
- Never mix observation time with configuration-update time or last-reported time.
- Preserve original status values when normalizing categories.
- State when a result is stale and name the timestamp.

## Output

- Decision supported by the data
- Quality rating: reliable, usable-with-caveats, insufficient, or misleading
- Dimension-by-dimension evidence
- Conflicts and reconciliation
- Unsafe conclusions to avoid
- One highest-value read-only follow-up
