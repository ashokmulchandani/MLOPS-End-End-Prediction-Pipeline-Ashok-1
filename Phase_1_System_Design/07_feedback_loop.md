# 1.7 — The Feedback Loop

> **Objective:** Design the closed loop from prediction → user action → logging → labels → retraining.
> Reference: Slide 1.7 of `phase1_system_design.html`

---

## House Prices: Feedback Loop Design

```
┌──────────────────────────────────────────────────────────┐
│                     THE FEEDBACK LOOP                     │
│                                                          │
│   ┌──────────┐     ┌──────────┐     ┌──────────┐        │
│   │ 1.PREDICT │────→│ 2.USER   │────→│  3.LOG   │        │
│   │           │     │   ACTS   │     │          │        │
│   │ Model      │     │ Agent    │     │ Store:    │        │
│   │ serves     │     │ shows    │     │ - features│        │
│   │ price      │     │ price to │     │ - predicted│       │
│   │ estimate   │     │ buyer    │     │ - actual  │        │
│   └──────────┘     └──────────┘     │   price   │        │
│                                      └─────┬────┘        │
│                                            │             │
│   ┌──────────┐     ┌──────────┐            │             │
│   │ 5.RETRAIN│←────│ 4.LABEL  │←───────────┘             │
│   │           │     │          │                          │
│   │ Monthly   │     │ Actual   │                          │
│   │ pipeline  │     │ sale      │                          │
│   │ run with  │     │ price =   │                          │
│   │ new data  │     │ ground    │                          │
│   │           │     │ truth     │                          │
│   └──────────┘     └──────────┘                          │
│                                                          │
│   ⚠️ CRITICAL: If Step 3 (Log) is skipped, the loop      │
│   dies. You'll never know if predictions were right.      │
└──────────────────────────────────────────────────────────┘
```

---

## What to Log (Schema Design)

Every prediction must capture:

```yaml
prediction_id: "uuid"
timestamp: "2026-07-21T14:30:00Z"
model_version: "prices_predictor_v1.2"
input_features: { ... all 82 features ... }
predicted_price: 285000
prediction_interval: [265000, 305000]
listing_id: "MLS-12345"
# Later, when the house sells:
actual_sale_price: 292000    # ← THIS is the label
sale_date: "2026-09-15"
prediction_to_sale_days: 56
error: -7000                  # predicted - actual
error_percent: -2.4%
```

---

## The Self-Fulfilling vs Self-Correcting Loop

| | ❌ Self-Fulfilling (Bad) | ✅ Self-Correcting (Good) |
|---|---|---|
| **What happens** | Model overprices → buyers avoid → no sales → model thinks "I was right, it never sold" | Model overprices → buyer offers less → sale recorded at lower price → model learns it was wrong |
| **Root cause** | Only logging predictions, not outcomes | Logging predictions AND actual outcomes, regardless of whether prediction was used |
| **Fix** | Log the actual sale price for ALL listings, not just the ones where the prediction was followed | — |

---

## Retraining Cadence

| Trigger | Cadence | Rationale |
|---------|---------|-----------|
| **Scheduled** | Monthly | Housing market doesn't shift daily. Monthly captures seasonal trends. |
| **Data-triggered** | After 500 new (prediction, actual) pairs | Enough new data to meaningfully update the model |
| **Drift-triggered** | PSI > 0.1 on any key feature | Something changed in the market — retrain immediately |
| **Performance-triggered** | R² on recent data < 0.75 for 3 days | Model is degrading — investigate and retrain |

---

## Your Turn

Draw your feedback loop:

```
Prediction → ___________ → ___________ → ___________ → New Model
```

**Questions to answer:**
1. What exactly gets logged at prediction time? ________________
2. How do you capture the ground truth label later? ________________
3. What triggers a retrain? (time / data volume / drift / performance) ________________
4. What's the risk of a self-fulfilling feedback loop in your system? ________________
