# 3.7 — Leakage Detection (Ablation Test)

> Reference: Slide 3.7 of `phase3_feature_engineering.html`

## The Ablation Test

1. Train model with ALL features → record R²
2. Drop ONE feature → retrain → record new R²
3. If R² drops suspiciously (>0.10 for a single feature) → investigate for leakage

## Common Leakage Sources

| Type | Example | Why It's Leakage |
|------|---------|-----------------|
| Target-derived | PricePerSqft = SalePrice / GrLivArea | Uses the answer in the input |
| Future info | "Days until sold" at listing time | You don't know this yet |
| Row ID correlation | Row ID correlates with SalePrice | Data collection artifact |
| Post-processing | "SalePrice_rounded" | Derived from target after prediction |

## House Prices Check

- [ ] No target-derived features
- [ ] No future-information features (all features available at listing time)
- [ ] Check: does PID (parcel ID) correlate with SalePrice?
- [ ] Check: does Order (row number) correlate with SalePrice?
