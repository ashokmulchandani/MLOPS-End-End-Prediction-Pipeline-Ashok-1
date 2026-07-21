# 3.1 — Feature Profiling Report

> Reference: Slide 3.1 of `phase3_feature_engineering.html`

## House Prices: Profiling Summary

| Category | Count | Key Findings |
|----------|-------|-------------|
| Numerical | 38 | SalePrice right-skewed (1.88), LotArea high variance |
| Categorical | 43 | 25 unique neighborhoods, PoolQC 99.7% null |
| Total | 82 | 2,930 rows, 0 duplicates |

### Top Correlations with SalePrice

| Feature | Correlation | Action |
|---------|------------|--------|
| OverallQual | 0.80 | Keep, standardize |
| GrLivArea | 0.71 | Keep, standardize |
| GarageCars | 0.64 | Keep, standardize |
| TotalBsmtSF | 0.63 | Keep, standardize |
| YearBuilt | 0.56 | Consider binning |

### Decisions from Profiling

- [ ] Log-transform SalePrice (positive skew)
- [ ] StandardScaler on numerical features
- [ ] OneHotEncode categorical features
- [ ] Drop PoolQC, Alley, Fence, MiscFeature (>80% null)
- [ ] Check for outliers in GrLivArea and LotArea
