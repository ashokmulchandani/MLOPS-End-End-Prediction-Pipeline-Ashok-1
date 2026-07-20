# 2.8 — Data Quality Checks

> **Objective:** Build automated quality gates that run before every training run.
> Reference: Slide 2.8 of `phase2_data_strategy.html`

---

## Four-Layer Quality Gate

### Layer 1: Schema Validation
- [ ] Correct number of columns? (82 features expected)
- [ ] Correct column names? (no renamed/removed fields)
- [ ] Correct data types? (numerical vs categorical)
- [ ] No unexpected columns? (new fields may break pipelines)

### Layer 2: Range Checks
- [ ] SalePrice: $12,789–$755,000 (no negatives, no $1 outliers)
- [ ] Year Built: 1872–2010 (no future years, no year 0)
- [ ] Lot Area: 1,300–215,245 sqft (physically possible)
- [ ] Bedrooms: 0–8 (no 99-bedroom houses)

### Layer 3: Null Rate Monitor
- [ ] Track null % per feature over time
- [ ] Alert if null rate CHANGES significantly (new missing pattern = upstream bug)
- [ ] Expected nulls: PoolQC (99.7%), Alley (93%), Fence (80%)
- [ ] Unexpected nulls: GrLivArea, SalePrice, OverallQual should ALWAYS be present

### Layer 4: Drift Detection
- [ ] PSI (Population Stability Index) on key features
- [ ] Compare live data distribution vs training baseline
- [ ] Alert threshold: PSI > 0.1 on GrLivArea, OverallQual, or LotArea
- [ ] Weekly distribution comparison on all numerical features

---

## House Prices: Quality Gate Results (Initial)

```
[PASS] Schema:       82 features + target present, correct types
[PASS] Range:        SalePrice $12,789–$755,000 (valid)
[PASS] Range:        Year Built 1872–2010 (valid)
[PASS] Range:        Lot Area 1,300–215,245 (valid, though one 215K lot is suspicious)
[WARN] Nulls:        PoolQC 99.7% — EXPECTED
[WARN] Nulls:        Alley 93.0% — EXPECTED
[WARN] Nulls:        Fence 80.0% — EXPECTED
[WARN] Nulls:        Fireplace 47.0% — EXPECTED
[PASS] Duplicates:   0 duplicates found
[PASS] Drift:        Initial baseline — no drift to compare yet
```

---

## Your Turn

Build your quality gate checklist:

| Layer | Check | Expected | Alert If |
|-------|-------|----------|----------|
| Schema | | | |
| Range | | | |
| Null Rate | | | |
| Drift | | | |
