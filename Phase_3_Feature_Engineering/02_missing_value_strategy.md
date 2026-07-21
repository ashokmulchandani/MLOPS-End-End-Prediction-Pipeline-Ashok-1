# 3.2 — Missing Value Strategy

> Reference: Slide 3.2 of `phase3_feature_engineering.html`

## Four Approaches

| Method | When to Use | Example |
|--------|------------|---------|
| Drop Rows | < 1% of data affected | Only 5 rows missing → drop them |
| Mean/Median/Mode | Missing at random, low importance | LotFrontage (17% null) → median |
| Constant ("Missing", 0, -1) | Missing IS the signal | GarageYrBlt null → "No Garage" = 0 |
| Model-Based (KNN, Iterative) | Important feature, worth the cost | GrLivArea missing → train model to predict it |

## House Prices Plan

| Feature | Null % | Strategy |
|---------|--------|----------|
| PoolQC | 99.7% | DROP |
| Alley | 93% | DROP |
| Fence | 80% | DROP |
| MiscFeature | 96% | DROP |
| FireplaceQu | 47% | Fill "None" |
| LotFrontage | 17% | Fill median |
| GarageYrBlt | 5% | Fill 0 (no garage) |
| Electrical | 0.03% | Fill mode |
