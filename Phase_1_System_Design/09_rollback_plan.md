# 1.9 — Rollback Plan

> **Objective:** Design exactly what happens when the model misbehaves in production.
> Reference: Slide 1.9 of `phase1_system_design.html`

---

## House Prices: Rollback Plan

### Rollback Triggers (When to Pull the Plug)

| # | Trigger | Threshold | Detection | Severity |
|---|---------|-----------|-----------|----------|
| 1 | **R² drops below threshold** | R² < 0.75 on live evaluation set for 3 consecutive hours | Automated hourly eval on recent sales | 🔴 CRITICAL |
| 2 | **RMSE spike** | RMSE > $35,000 on daily evaluation batch | Automated daily eval | 🔴 CRITICAL |
| 3 | **Prediction distribution shift** | Mean predicted price shifts > 2 std dev from training baseline | Statistical process control on prediction stream | 🟡 WARNING |
| 4 | **Null rate spike** | Any feature exceeds 30% null in production traffic | Null rate monitor per feature | 🟡 WARNING |
| 5 | **Latency spike** | p95 latency > 1 second for 10+ minutes | Latency monitor | 🟡 WARNING |

---

### Rollback Procedure

```
1. DETECT — alert fires (R² < 0.75 for 3 hours)

2. ASSESS (5 minutes) — is this a real degradation or a data issue?
   - Check: did the data source change? (schema, missing columns)
   - Check: is there a market event? (new tax law, interest rate shock)
   - Check: did we deploy a new model version recently?

3. ROLLBACK (automatic, < 10 seconds)
   → mlflow models serve --model-uri models:/prices_predictor/production
   → Switch to previous production version in MLflow registry
   → Health check on rolled-back model

4. NOTIFY
   → Slack/email: "prices_predictor rolled back from v1.3 to v1.2.
     Reason: R² dropped to 0.71. Investigating."
   → Include: affected prediction IDs, time window, severity

5. INVESTIGATE (hours to days)
   → Compare v1.3 vs v1.2 predictions on recent data
   → Check feature drift between training data and live data
   → Root cause analysis → fix → test → re-deploy
```

---

### Rollback Infrastructure

| Component | How | Time |
|-----------|-----|------|
| **Model versioning** | MLflow Model Registry — every trained model gets a version tag | Automatic |
| **Serving switch** | `mlflow models serve` with `--model-uri` pointing to previous version | < 10 seconds |
| **Health check** | `/health` endpoint returns model version — verify it's the rolled-back version | < 5 seconds |
| **Prediction log** | All predictions logged with model_version — can query which version served which prediction | Always on |

---

### Shadow Mode (Alternative to Immediate Rollback)

For high-risk deployments (new model architecture, new feature set):

```
Week 1:  New model runs in SHADOW — predictions logged, not shown to users
Week 2:  Compare shadow predictions vs production model on actual outcomes
Week 3:  If shadow model outperforms on all guardrails — switch 5% traffic
Week 4:  5% → 50% (if still healthy) → 100%
```

Shadow mode is safer but slower. Use it when:
- Deploying to a new market segment
- Changing model architecture (Linear Regression → XGBoost)
- Adding/removing features

---

## Your Turn

Fill out for your project:

**Trigger 1:** If _____________ drops below _____________ for _____________ → ROLLBACK

**Trigger 2:** If _____________ exceeds _____________ → ROLLBACK

**Rollback step-by-step:**
1. ___________________________________
2. ___________________________________
3. ___________________________________
4. ___________________________________

**Rollback time from alert to safe state:** _____________ minutes

**Question:** Can you roll back in < 1 minute? If not, what's the bottleneck?
