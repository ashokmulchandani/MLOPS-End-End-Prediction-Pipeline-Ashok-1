# 3.10 — Feature Health Monitoring

> Reference: Slide 3.10 of `phase3_feature_engineering.html`

## Four Monitoring Checks (Weekly)

| Check | Metric | Alert Threshold |
|-------|--------|----------------|
| Distribution Drift | PSI (Population Stability Index) | PSI > 0.1 = investigate, > 0.2 = retrain |
| Null Rate | % null per feature | > 5% change from baseline |
| Range Violations | % predictions outside training range | > 5% of predictions |
| Prediction Stability | Mean, std, p95 of predictions | Shift > 2σ from baseline |

## House Prices: Top 10 Features to Monitor

GrLivArea, OverallQual, GarageCars, TotalBsmtSF, YearBuilt, LotArea, Bedrooms, FullBath, TotRmsAbvGrd, Fireplaces

## Tools

- **Evidently AI:** Open-source drift + data quality reports
- **Great Expectations:** Schema validation + data quality tests
- **Custom:** pandas profiling + statistical tests (KS test, PSI)

## Phase 5 Integration

Monitoring is implemented in Phase 7 (Production Ops). For Phase 5, the foundation is:
1. Pipeline is versioned (MLflow artifact)
2. Features are profiled (EDA notebook)
3. Baseline distributions are known
4. Monitoring code is scaffolded and ready
