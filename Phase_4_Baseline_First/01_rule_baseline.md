# 4.1 — The Simplest Possible Baseline

> Reference: Slide 4.1 of `phase4_baseline_first.html`

## House Prices Baseline v0 (Rules)

**Formula:** `Predicted Price = $150 × GrLivArea`

**Performance:** R² ≈ 0.50, RMSE ≈ $55,000, MAE ≈ $40,000

## Other Baseline Options

| Baseline | Formula | Expected R² |
|----------|---------|------------|
| Always Mean | Price = $182,000 | ~0.00 |
| Single Feature | Price = f(OverallQual) | ~0.55 |
| Neighborhood Avg | Price = avg(SalePrice per Neighborhood) | ~0.45 |

## Rule

> If ML can't beat a one-line rule by a meaningful margin, you don't need ML.
