# 2.10 — Data Changelog

> **Objective:** Maintain a human-readable log of every data change — what, when, why, and impact.
> Reference: Slide 2.10 of `phase2_data_strategy.html`

---

## DATA CHANGELOG — Ames Housing Dataset

```
═══════════════════════════════════════════════════════════════

[2026-07-21] v1.0 — Initial import
  • Downloaded ames_housing.csv from Kaggle (Dean De Cock)
  • 2,930 rows × 82 features + SalePrice target
  • Verified: no duplicate rows, SalePrice range $12,789–$755,000
  • DVC hash: a1b2c3d4

[2026-07-22] v1.1 — Outlier removal
  • Removed 12 rows with Z-score > 3 on SalePrice
  • Removed 5 rows with GrLivArea > 4,000 sqft (likely commercial)
  • New count: 2,913 rows
  • DVC hash: e5f6g7h8
  • ⚠️ Model retrained — R² changed from 0.85 → 0.87

[2026-08-15] v1.2 — Feature engineering
  • Added: Log_SalePrice (log-transformed target)
  • Added: House_Age (2026 − Year_Built)
  • Dropped: PoolQC (99.7% null, not useful for prediction)
  • New schema: 2,913 rows × 84 features
  • DVC hash: i9j0k1l2
  • ⚠️ Breaking change — all downstream models must retrain

[____-__-__] v__ — _________________
  • _________________
  • DVC hash: ____
  • ⚠️ _________________
```

---

## Changelog Template

Every entry should include:

| Field | Example |
|-------|---------|
| **Date** | `[2026-07-21]` |
| **Version** | `v1.0` — semantic, bump major for breaking changes |
| **What** | Rows added/removed, features added/dropped, labels updated, transformations applied |
| **Why** | The REASON — not just "cleaned data" but "removed commercial properties that skewed regression" |
| **DVC Hash** | Link to the exact data file |
| **Impact** | Did model metrics change? Was retraining required? Is this a breaking change? |

---

## Why This Matters

When someone asks "Why did the model start performing differently last month?", the changelog is your first stop:

1. Check if data changed → changelog
2. Check if code changed → git log
3. Check if the world changed → drift monitor

Without the changelog, #1 is a guessing game.

---

## Your Turn

Copy this template and start your own changelog:

```
═══════════════════════════════════════════════════════════════

[____-__-__] v1.0 — Initial import
  • _________________
  • Rows: ____, Features: ____, Target: ____
  • DVC hash: ____

[____-__-__] v__ — _________________
  • _________________
  • DVC hash: ____
  • ⚠️ _________________
```
