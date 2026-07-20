# 1.10 — The 1-Page ML Proposal (Capstone)

> **Objective:** Synthesize everything from Steps 1.1–1.9 into a single page.
> Reference: Slide 1.10 of `phase1_system_design.html`

---

# ML PROPOSAL: House Price Predictor

**Author:** Ashok Mulchandani
**Date:** July 2026
**Status:** Phase 1 Design Complete — Ready for Phase 5 Implementation

---

## 1. Problem

Real estate agents spend 2-4 hours manually estimating fair market value for each client. They compare 5-10 "comparable" properties, adjust for differences, and produce an estimate. This is slow, inconsistent across agents, and prone to bias (agents may overprice to win listings).

**6-Word Test Verdict:** ✅ ALL 6 pass — ML is justified.

---

## 2. Solution

An ML model that predicts the sale price of a residential property from 82 structural and locational features, served via REST API with sub-500ms latency for display on listing pages.

**Given** 82 property features → **Predict** SalePrice (USD) → **For** real estate agents → **At** < 500ms → **To** reduce negotiation time by 30%

---

## 3. Value Proposition

| Stakeholder | Benefit | Measurement |
|-------------|---------|-------------|
| Real Estate Agents | Faster, data-backed price estimates | Time per listing: 4 hrs → 15 min |
| Home Buyers | Confident offers based on objective data | Offers within 5% of fair value |
| Business | More deals closed faster | Negotiation time ↓ 30%, close rate ↑ |

---

## 4. Metrics

| Level | Metric | Target |
|-------|--------|--------|
| ⭐ North Star | R² Score | > 0.85 |
| 🛡️ Guardrail 1 | RMSE | < $25,000 |
| 🛡️ Guardrail 2 | Overfit Delta (R²_train − R²_test) | < 0.05 |
| 🛡️ Guardrail 3 | MAE | < $18,000 |
| 📱 Product | % predictions within 5% of actual | > 90% |
| 💼 Business | Avg negotiation days | ↓ 30% |

---

## 5. Baseline Strategy

1. **v0 (Rules):** $/sqft × living_area + garage adjustment → R² ≈ 0.55
2. **v1 (Simple ML):** Linear Regression on all 82 features → Target R² > 0.85
3. **v2 (Advanced):** XGBoost with hyperparameter tuning — only if v1 is insufficient
4. **Ship v1, measure, then decide if v2 is worth the complexity.**

---

## 6. Top Risks & Mitigations

| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|
| Outlier contamination | HIGH | MEDIUM | Z-score detection, log-transform SalePrice |
| Train/serve skew | HIGH | CRITICAL | sklearn.Pipeline, versioned scaler, golden test set |
| Missing values in production | MEDIUM | HIGH | ColumnTransformer + SimpleImputer, null rate monitoring |
| Data drift (market shift) | MEDIUM | HIGH | Monthly retrain, PSI monitoring on key features |
| Unusual property types | LOW | MEDIUM | Out-of-distribution detection, fallback to neighborhood median |

---

## 7. Operational Constraints

| Constraint | Limit | Why This Matters |
|-----------|-------|------------------|
| Latency | < 500ms p99 | Web page load — can't keep user waiting |
| Throughput | 100 req/s peak | Normal browsing traffic |
| Cost | < $0.001/prediction | Linear Regression on CPU achieves this |
| Interpretability | Must explain top 5 drivers per prediction | Agents need to tell clients "why" |
| Privacy | None — public record data | No GDPR burden |
| Retraining | Monthly | Market shifts slowly |
| Availability | 99.5% | Fallback to neighborhood median if model is down |

---

## 8. Rollback Plan

**Triggers:** R² < 0.75 for 3 hours → auto-rollback via MLflow Model Registry
**Time to safe state:** < 10 seconds (switch serving endpoint to previous version)
**Investigation:** Compare versions, check feature drift, root cause → fix → re-deploy

---

## 9. Tech Stack

| Component | Tool | Why |
|-----------|------|-----|
| Pipeline Orchestration | ZenML | Reproducible, cacheable steps |
| Experiment Tracking | MLflow | Compare runs, register models |
| ML Library | scikit-learn | Linear Regression, Pipeline, ColumnTransformer |
| Data Processing | pandas, numpy | Standard data wrangling |
| Serving | MLflow Serving | Built-in, no extra infra |
| Monitoring | Evidently AI (future) | Drift detection, data quality |

---

## 10. Next Steps (Phase 5 Implementation)

1. Set up ZenML + MLflow stack
2. Implement data ingestion (Factory Pattern)
3. Run EDA — verify Phase 1 assumptions against real data
4. Build processing pipeline (Strategy Pattern for each step)
5. Train baseline model + log to MLflow
6. Evaluate against North Star + guardrails
7. Deploy with continuous deployment pipeline
8. Monitor and iterate

---

## Your Turn — ML Proposal Template

```markdown
# ML PROPOSAL: [Your Project Name]

## 1. Problem
[1-liner + 6-word test result]

## 2. Solution
[Given X, Predict Y, For Z, At T, To B]

## 3. Value
[Who benefits + how to measure]

## 4. Metrics
[North Star + 2-3 Guardrails + Product + Business]

## 5. Baseline Strategy
[v0 (rules) → v1 (simple ML) → v2 (advanced if needed)]

## 6. Top Risks
[5 failure modes with mitigations]

## 7. Constraints
[Latency, throughput, privacy, cost, availability]

## 8. Rollback Plan
[Triggers + procedure + time to safe state]

## 9. Tech Stack
[Tools + rationale]

## 10. Next Steps
[What you'll build first]
```

---

**Phase 1 Complete!** 🎉 You now have a complete ML System Design for the House Prices Predictor. Every decision is documented. Every risk has a mitigation. Rollback is planned. Ready to build in Phase 5.
