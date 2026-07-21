# 3.4 — Binning Strategy

> Reference: Slide 3.4 of `phase3_feature_engineering.html`

## When to Bin

Binning helps when the relationship between a feature and target is NON-LINEAR.

## House Prices Candidates

| Feature | Bins | Rationale |
|---------|------|-----------|
| YearBuilt | Pre-1900, 1900-1950, 1950-1980, 1980-2000, Post-2000 | Victorian homes have different pricing than 1950s ranches |
| LotArea | Small (<5K), Medium (5-10K), Large (10-20K), Estate (>20K) | Lot size has diminishing returns |
| HouseAge | New (<5yr), Recent (5-20yr), Mid (20-50yr), Old (50-100yr), Historic (>100yr) | Alternative to YearBuilt bins |

## For Phase 5

**Start without binning.** Linear Regression can handle continuous YearBuilt. Only add bins if:
1. Residuals show a non-linear pattern with YearBuilt
2. Adding binned YearBuilt improves R² by >0.02
3. The bins make business sense to real estate agents
