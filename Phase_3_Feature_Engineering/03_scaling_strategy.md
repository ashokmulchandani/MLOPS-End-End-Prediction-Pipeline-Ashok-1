# 3.3 — Scaling Strategy

> Reference: Slide 3.3 of `phase3_feature_engineering.html`

## Three Scalers

| Scaler | Formula | Best For | Outlier Sensitive? |
|--------|---------|----------|-------------------|
| StandardScaler | (x − μ) / σ | LinearRegression, kNN, SVM, neural nets | Somewhat |
| MinMaxScaler | (x − min) / (max − min) | Neural nets, images | VERY |
| RobustScaler | (x − median) / IQR | Data with known outliers | NO |

## House Prices Decision

**Use: StandardScaler** on all 38 numerical columns.

**Rationale:**
- Linear Regression works best with standardized features
- After outlier removal (Phase 5, Z-score threshold=3), outliers are controlled
- StandardScaler preserves the shape while centering

**Implementation:**
```python
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])
```
