# 2.7 — Train / Validation / Test Split Strategy

> **Objective:** Split data so the model is tested on truly unseen examples.
> Reference: Slide 2.7 of `phase2_data_strategy.html`

---

## Three Split Methods

| Method | Logic | When to Use | Leakage Risk |
|--------|-------|-------------|-------------|
| **Random** | Shuffle all rows, split 70/15/15 | Independent observations (houses, images) | Low — but check for duplicates |
| **Time-Based** | Train on older, test on newer | Forecasting (stocks, weather, sales) | High if done wrong — NEVER random-split time series |
| **Entity-Based** | All rows for one user/customer go to same split | User-level predictions (churn, recommendations) | HIGH if done wrong — same user in train AND test = cheating |

---

## The Leakage Test

> "Can any information from a test-set row be inferred from a training-set row?"

- ✅ **Random split on houses:** House #123 in test doesn't help predict House #456. No leakage.
- ❌ **Random split on users:** User #123's Jan data in training, June data in test. The model already knows this user. Leakage.
- ❌ **Random split on time series:** Tomorrow's stock price in training, yesterday's in test. The model sees the future. Leakage.

---

## House Prices: Decision

**Strategy:** Simple Random Split — 80% train / 20% test

**Why random is correct:**
- Each house is an independent observation
- No user entity linking houses together
- Sale years (2006-2010) have similar market conditions in Ames
- 5-fold cross-validation on training portion provides additional robustness

**Split ratios:**
| Set | Rows | Purpose |
|-----|------|---------|
| Train | 2,344 (80%) | Model training |
| Test | 586 (20%) | Final evaluation |

---

## Your Turn

| Question | Your Answer |
|----------|-------------|
| Are your data points independent? | |
| Is there a time component? | |
| Is there a user/entity grouping? | |
| Which split method? | |
| What ratio? (70/30? 80/20? 90/10?) | |
