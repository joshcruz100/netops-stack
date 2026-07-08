---
name: incident-diff-report
description: Compare two infrastructure, monitoring, or incident snapshots and report only meaningful changes. Use when identifying new failures, regressions, recoveries, cleared alerts, inventory changes, severity changes, or monitoring-access changes between runs, including JSON snapshots and human-readable reports.
---

# Incident Diff Report

Compare a baseline with a current observation while preserving identity, timestamps, completeness, and evidence quality.

## Workflow

1. Identify the baseline and current observation timestamps. Prefer the last successful complete baseline over the immediately previous failed run.
2. Assess completeness per source. Do not interpret missing entities as removals when the current source is partial, stale, timed out, or denied.
3. Match entities by stable identifiers first, then by a documented composite key. Never match only by display name when IDs exist.
4. Normalize statuses and severity without discarding the original values.
5. Classify changes as added, removed, regressed, recovered, changed, or unchanged.
6. Suppress unchanged inventory and repeated known issues unless their age, count, or severity materially changed.
7. For normalized JSON snapshots, read [references/snapshot-schema.md](references/snapshot-schema.md) and run `scripts/diff_snapshots.py`.
8. Produce a concise narrative ordered by operational impact, followed by confidence and data gaps.

## Comparison rules

- Treat `removed` as reliable only when both source snapshots are complete.
- Treat a timeout or denied source as a monitoring-access regression, not an infrastructure recovery.
- Preserve first-seen and last-reported timestamps when available.
- Distinguish state changes from metadata-only changes.
- Flag count deltas only when the populations and scopes are comparable.
- Say `no material change` when only timestamps or irrelevant metadata differ.

## Output format

- **Material changes:** new failures and worsened issues
- **Recoveries:** resolved or improved issues
- **Inventory changes:** additions/removals with confidence
- **Continuing issues:** only those requiring attention
- **Data quality:** partial, stale, or incomparable sources
- **Next step:** one read-only diagnostic for the highest-impact change
