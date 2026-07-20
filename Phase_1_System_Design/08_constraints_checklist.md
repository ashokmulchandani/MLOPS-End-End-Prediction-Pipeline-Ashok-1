# 1.8 — Operational Constraints Checklist

> **Objective:** Define the hard operational constraints that limit what models you can use.
> Reference: Slide 1.8 of `phase1_system_design.html`

---

## House Prices: Constraints Checklist

### ⏱️ Latency Budget

| Constraint | Value | Rationale |
|-----------|-------|-----------|
| Max latency per prediction | **< 500ms** | Web page load — prediction must return before the user scrolls away |
| p95 latency | < 350ms | 95% of requests faster than this |
| p99 latency | < 500ms | Even tail latency must stay under budget |

**Design impact:** Rules out large ensembles (Random Forest with 500 trees on CPU ≈ 2s). Linear Regression predicts in < 1ms.

---

### 📊 Throughput

| Constraint | Value | Rationale |
|-----------|-------|-----------|
| Peak requests/second | ~100 | Normal browsing traffic for a real estate site |
| Average requests/second | ~10 | Off-peak usage |
| Burst capacity | 200/s for 30 seconds | Flash sale or market event |

**Design impact:** Single server sufficient. No need for autoscaling or load balancing at launch.

---

### 🔒 Privacy & Compliance

| Constraint | Status | Notes |
|-----------|--------|-------|
| PII in features? | ✅ NONE | Property data is public record. No names, SSNs, or personal data. |
| GDPR applicable? | ✅ NO | No personal data means GDPR right-to-explanation doesn't strictly apply. Still good practice to be explainable. |
| Data residency? | ✅ N/A | No sensitive data to localize |
| Audit trail required? | ⚠️ MINIMAL | Log predictions for debugging, but no regulatory audit requirement |

**Design impact:** Low privacy burden. Can use any model architecture without privacy constraints.

---

### 📖 Interpretability

| Constraint | Value | Rationale |
|-----------|-------|-----------|
| Interpretability level | **MEDIUM** | Agents need to answer "Why this price?" to clients |
| What needs explanation? | Top 5 features driving this specific prediction | "This home's price is driven by Overall Quality, Living Area, and Garage Size" |
| Global or local? | Both — global feature importance for trust, local explanations per prediction | |

**Design impact:** Linear Regression is naturally interpretable (coefficients = $ per feature). If we later use XGBoost, need SHAP/LIME.

---

### 💰 Cost

| Constraint | Value | Rationale |
|-----------|-------|-----------|
| Cost per prediction | **< $0.001** | At 100K predictions/month, that's < $100/month |
| Training cost per run | < $5 | Monthly retraining on 2,930 rows |
| Infrastructure budget | < $50/month | Single VM or serverless function |
| GPU required? | NO | scikit-learn runs on CPU. Linear Regression trains in seconds. |

**Design impact:** No cloud GPU needed. Can run on a $20/month cloud VM or even a Raspberry Pi.

---

### 📅 Maintenance

| Constraint | Value | Rationale |
|-----------|-------|-----------|
| Retraining cadence | Monthly | Housing market shifts slowly |
| Model A/B test duration | 2 weeks | Need enough sales to compare statistically |
| Model version retention | Keep last 5 versions | Fast rollback to any recent version |
| On-call burden | Business hours only | Not a critical system (nobody dies if prediction is wrong) |

---

### 🌐 Availability

| Constraint | Value | Rationale |
|-----------|-------|-----------|
| Uptime target | 99.5% | ~3.6 hours/month acceptable downtime |
| Degraded mode | Return neighborhood median price if model is down | Graceful degradation > hard failure |
| Health check | `/health` endpoint returning model version + last training date | |

---

## Your Turn

Fill out for your project:

| Category | Constraint | Your Value |
|----------|-----------|------------|
| ⏱️ Latency | Max ms per prediction | |
| 📊 Throughput | Peak requests/second | |
| 🔒 Privacy | PII / GDPR / residency requirements | |
| 📖 Interpretability | What must be explained? | |
| 💰 Cost | Budget per month | |
| 📅 Maintenance | Retraining cadence | |
| 🌐 Availability | Uptime % | |

**Key question:** Which constraint is the binding one — the one that forces the biggest design compromise?
