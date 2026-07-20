# 1.2 — Three Options Comparison

> **Objective:** Compare Rules/Heuristic vs ML Model vs "Not Now" before committing to ML.
> Reference: Slide 1.2 of `phase1_system_design.html`

---

## House Prices: Three Options Evaluated

| Dimension | 🔴 Option A: Rules/Heuristic | 🔵 Option B: ML Model | 🟢 Option C: Not Now |
|-----------|---------------------------|---------------------|---------------------|
| **Approach** | $/sqft formula + garage/no-garage adjustment | Linear Regression on 82 features via ZenML + MLflow | Collect more data for 6 months first |
| **Setup Cost** | 1 day (Excel formula) | 2-3 weeks (pipeline, training, deployment) | Minimal (logging infra only) |
| **Maintenance Cost** | Near zero | Monthly retraining, drift monitoring | Zero (just collecting) |
| **Accuracy** | ~60% (R² ≈ 0.55) | ~85% (R² ≈ 0.85) | N/A |
| **Interpretability** | Perfect — you wrote every rule | Good — Linear Regression coefficients are explainable | N/A |
| **Risk** | Low — no model to break | Medium — pipeline bugs, drift, train/serve skew | Minimal |
| **Time to Value** | Immediate | 3-4 weeks | 6+ months |
| **Scales to New Markets?** | No — each market needs new rules | Yes — retrain on new city's data | Eventual |

---

## Decision Framework Questions

Before choosing ML, ask these 3 questions:

1. **What's the simplest thing that could possibly work?**
   - Answer: $/sqft × property_area + adjustments for bedrooms/bathrooms
   - This gives ~60% accuracy with zero training cost

2. **How much lift does ML give over the baseline?**
   - Answer: R² improves from ~0.55 to ~0.85 — a 30% improvement
   - This IS worth the investment

3. **Do we have the infrastructure to maintain an ML system?**
   - Answer: For this learning project, yes — ZenML + MLflow run locally
   - For production: need monitoring, retraining pipeline, rollback plan

---

## Verdict

**✅ ML (Option B) is the right choice** for the House Prices project because:
- The accuracy lift over rules is significant (30% R² improvement)
- The infrastructure exists (ZenML + MLflow)
- The constraints are well-understood (low latency, low cost, monthly retrain)

---

## Your Turn

For your own project:

| Dimension | Rules/Heuristic | ML Model | Not Now |
|-----------|----------------|----------|---------|
| **Approach** | | | |
| **Setup Cost** | | | |
| **Accuracy** | | | |
| **Risk** | | | |
| **Time to Value** | | | |

**Questions to answer:**
1. What's the simplest thing that could possibly work? ________________
2. How much lift does ML give over the baseline? ________________
3. Do we have the infra to maintain an ML system? ________________

**Decision:** ⬜ Rules / ⬜ ML / ⬜ Not Now
