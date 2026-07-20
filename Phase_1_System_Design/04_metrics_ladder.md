# 1.4 — The Metrics Ladder

> **Objective:** Build a 4-rung metrics ladder connecting model performance to business value.
> Reference: Slide 1.4 of `phase1_system_design.html`

---

## House Prices: Metrics Ladder

```
┌─────────────────────────────────────────────────────────────┐
│ 💼 BUSINESS METRIC                                           │
│    Revenue from faster sales                                 │
│    → "Reduce negotiation time by 30%"                        │
│    → Measured: avg days from listing to close                │
├─────────────────────────────────────────────────────────────┤
│ 📱 PRODUCT METRIC                                            │
│    % of predictions within 5% of final sale price            │
│    → "90% of estimates within ±5% of actual"                │
│    → Measured: |predicted - actual| / actual < 0.05         │
├─────────────────────────────────────────────────────────────┤
│ 🤖 MODEL METRIC (North Star)                                 │
│    R² Score on test set                                      │
│    → Target: R² > 0.85                                       │
│    Guardrails: RMSE < $25K, Overfit Δ < 0.05, MAE < $18K    │
├─────────────────────────────────────────────────────────────┤
│ 📊 DATA QUALITY METRICS                                      │
│    % missing values per column                               │
│    → < 5% missing in any feature                             │
│    Feature drift (PSI)                                       │
│    → PSI < 0.1 for all key features                          │
└─────────────────────────────────────────────────────────────┘
```

---

## The Connection Test

For each rung, ask: **"If this metric improves, does the rung above it also improve?"**

| Rung | Example of Broken Connection | Example of Working Connection |
|------|------------------------------|------------------------------|
| Data → Model | More features added but R² doesn't change → data quality wasn't the bottleneck | Missing value imputation improved → R² improved 0.82 → 0.85 |
| Model → Product | R² improved 0.89 → 0.91 but predictions still off by >5% for luxury homes → model overfit on mid-range houses | R² 0.85 → predictions within 5% for 90% of all listings |
| Product → Business | Predictions are accurate but agents don't trust the tool → no adoption → no business impact | Agents trust ±5% estimates → use tool daily → negotiation time ↓ 30% |

---

## Your Turn

Build your metrics ladder:

```
┌─────────────────────────────────────────────────────────────┐
│ 💼 BUSINESS METRIC                                           │
│    _________________________________________________________ │
├─────────────────────────────────────────────────────────────┤
│ 📱 PRODUCT METRIC                                            │
│    _________________________________________________________ │
├─────────────────────────────────────────────────────────────┤
│ 🤖 MODEL METRIC                                              │
│    _________________________________________________________ │
├─────────────────────────────────────────────────────────────┤
│ 📊 DATA QUALITY METRICS                                      │
│    _________________________________________________________ │
└─────────────────────────────────────────────────────────────┘
```

**Check each rung:** If your model metric improves, does the product metric move? If your product metric moves, does the business metric move? If NO to either — your ladder is broken.
