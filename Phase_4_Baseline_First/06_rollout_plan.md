# 4.6 — Gradual Rollout Plan

| Week | Traffic % | Action |
|------|----------|--------|
| 1-2 | 0% (Shadow) | ML runs silently, compared to agent estimates |
| 3 | 5% | Random listings show ML + agent estimate |
| 4 | 25% | If guardrails pass, expand |
| 5 | 100% | ML is primary. Agent override available. |
| ANY | Rollback | If R² < 0.75 or RMSE > $35K on live data |
