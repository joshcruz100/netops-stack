# Monitoring evidence quality rubric

| Dimension | Strong | Weak |
|---|---|---|
| Freshness | live query within required window | old cache, unknown timestamp, stale last report |
| Completeness | all scopes/pages succeeded | timeout, truncation, missing scope/page |
| Scope fidelity | exact organizations, networks, containers, or targets | mixed or undocumented scope |
| Consistency | independent evidence agrees or differences are explained | contradictory status/counts |
| Comparability | same definitions, scope, and completeness across runs | changed population or collector behavior |
| Provenance | source, method, parameters, and timestamp known | copied summary or unknown origin |
| Granularity | evidence matches the decision level | aggregate used to infer individual state |

## Ratings

- **Reliable:** all material dimensions are strong; conclusions can drive action.
- **Usable with caveats:** limited weakness that does not undermine the main conclusion.
- **Insufficient:** missing or stale evidence prevents the requested conclusion.
- **Misleading:** the available evidence would likely support a false conclusion without correction.

## Reconciliation priority

1. Live direct observation
2. Live authoritative API summary
3. Current cached page linked from the live response
4. Historical baseline with timestamp
5. Human summary or inference

Higher priority does not automatically win when scopes differ; reconcile scope first.
