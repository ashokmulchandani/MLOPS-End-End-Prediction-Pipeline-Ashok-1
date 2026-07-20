# 1.5 — North Star & Guardrail Metrics

> **Objective:** Choose exactly 1 North Star metric and 2-3 guardrail metrics with rationale.
> Reference: Slide 1.5 of `phase1_system_design.html`

---

## House Prices: Metric Choices

### ⭐ North Star: R² Score (Coefficient of Determination)

**Target:** R² > 0.85 on held-out test set

**Why R²:**
- Scale-independent (0 to 1) — easy to compare across markets
- Intuitive meaning: "85% of price variation is explained by our features"
- Industry-standard for regression problems
- Works for both cheap and expensive homes (unlike RMSE which scales with price)

**Why NOT:**
- RMSE alone — $25K error means different things for a $100K house vs a $500K house
- MAE alone — doesn't penalize large errors enough (a $100K mistake is much worse than 5 × $20K mistakes)

---

### 🛡️ Guardrail 1: RMSE < $25,000

**Why:** Prevents the model from making catastrophically large errors. R² can be high even with a few massive outliers. RMSE penalizes large errors quadratically — it screams when the model is badly wrong on ANY prediction.

**Trigger:** If RMSE exceeds $25K, block deployment regardless of R².

---

### 🛡️ Guardrail 2: Overfit Delta (R²_train − R²_test) < 0.05

**Why:** Detects memorization. If the model scores 0.95 on training but 0.85 on test, it has memorized noise in the training set. This model will fail on new listings.

**Trigger:** If delta > 0.05, reduce model complexity or add regularization.

---

### 🛡️ Guardrail 3: MAE < $18,000

**Why:** MAE is more robust to outliers than RMSE. If RMSE is fine but MAE spikes, it means a few specific houses are getting terrible predictions while most are okay. This is a distribution problem — some segment of the market is being underserved.

**Trigger:** If MAE violates but RMSE is fine, investigate per-neighborhood or per-price-segment errors.

---

## The Guardrail Contract

```
Before deploying any new model version:
✅ North Star (R²) improved OR stayed within 1% of previous
✅ All 3 guardrails are NOT WORSE than the previous model
❌ If any guardrail degrades → BLOCK deployment, investigate
```

---

## Your Turn

| Metric | Type | Target | Rationale |
|--------|------|--------|-----------|
| _____________ | ⭐ North Star | ________ | ________ |
| _____________ | 🛡️ Guardrail | ________ | ________ |
| _____________ | 🛡️ Guardrail | ________ | ________ |
| _____________ | 🛡️ Guardrail | ________ | ________ |

**Questions to answer:**
1. Why THIS North Star and not the alternatives? ________________
2. What specific guardrail violation would make you block deployment? ________________
3. How often will you re-evaluate these choices? ________________
