# 1.6 — Failure Mode Analysis

> **Objective:** List 5 ways your model could fail BEFORE writing a single line of code.
> Reference: Slide 1.6 of `phase1_system_design.html`

---

## House Prices: 5 Anticipated Failure Modes

### Failure 1: 🏚️ Outlier Contamination

**What happens:** A few $500K+ luxury mansions skew the Linear Regression coefficients. The model inflates prices for normal homes because it's trying to fit the extreme values.

**Likelihood:** HIGH — Ames dataset has luxury properties. SalePrice std dev is $79K.

**Impact:** MEDIUM — mid-range homes (the majority) get systematically overpriced.

**Mitigation:**
- Z-score outlier detection (threshold = 3) on SalePrice
- Log-transform SalePrice to compress the tail
- Consider RobustScaler instead of StandardScaler

**Detection in production:** Monitor prediction distribution. If the 95th percentile suddenly shifts, outliers are back.

---

### Failure 2: 📉 Data Drift

**What happens:** Model trained on 2006-2010 Ames housing data. Housing market shifts (interest rates, remote work migration). Old patterns no longer hold.

**Likelihood:** MEDIUM — housing markets shift slowly but meaningfully over years.

**Impact:** HIGH — systematically wrong predictions erode user trust.

**Mitigation:**
- Monitor PSI (Population Stability Index) on key features
- Retrain monthly with recent sales data
- Set drift alert threshold: PSI > 0.1 triggers investigation

**Detection in production:** Weekly PSI calculation on feature distributions vs training baseline.

---

### Failure 3: 🕳️ Missing Value Catastrophe

**What happens:** In production, a data source stops sending PoolQC, Fence, or Alley features. 40% of columns arrive as NaN. Drop-null handling deletes half the input — prediction fails.

**Likelihood:** MEDIUM — data source changes are common in production.

**Impact:** HIGH — prediction service returns errors instead of prices.

**Mitigation:**
- ColumnTransformer with SimpleImputer (median for numeric, mode for categorical)
- NEVER drop rows with missing values in production — impute instead
- Monitor null rate per feature — if any feature goes > 20% null, alert

**Detection in production:** Null rate dashboard per feature, refreshed hourly.

---

### Failure 4: 🎭 Train/Serve Skew

**What happens:** Training pipeline applies `StandardScaler.fit(X_train)`. Serving pipeline loads the scaler but applies `StandardScaler.fit(X_live)` instead of `.transform()`. Predictions are silently wrong — no crash, no error, just wrong numbers.

**Likelihood:** HIGH — this is the #1 production ML bug.

**Impact:** CRITICAL — predictions are wrong and you don't know it.

**Mitigation:**
- Use `sklearn.Pipeline` — it guarantees identical transforms
- Serialize the ENTIRE pipeline (not just the model) with MLflow
- Integration test: send a known input, verify prediction matches training-time value
- Version the scaler artifact alongside the model

**Detection in production:** Weekly "golden test set" — 10 hand-verified houses run through the pipeline. If predictions drift > 2%, investigate.

---

### Failure 5: 🦄 The Unicorn Listing

**What happens:** A converted church, a geodesic dome, or a mixed-use commercial/residential property appears. The model has never seen anything like it — the feature vector is far outside the training distribution. Extrapolation produces a nonsense price (negative or absurdly high).

**Likelihood:** LOW — unusual properties are rare.

**Impact:** MEDIUM — one bad prediction won't break the business, but it erodes trust.

**Mitigation:**
- Flag predictions where any feature is > 3 std dev from training mean
- Return a prediction interval instead of a point estimate
- Fall back to "Insufficient data for this property type — consult an agent"

**Detection in production:** Count of "out-of-distribution" predictions per day. If > 5%, the market may have fundamentally changed.

---

## Failure Mode Priority Matrix

| Failure | Likelihood | Impact | Priority | Mitigation Cost |
|---------|-----------|--------|----------|----------------|
| Train/Serve Skew | HIGH | CRITICAL | 🔴 P0 | Medium (pipeline refactor) |
| Outlier Contamination | HIGH | MEDIUM | 🟡 P1 | Low (outlier detection step) |
| Missing Values | MEDIUM | HIGH | 🟡 P1 | Low (imputation) |
| Data Drift | MEDIUM | HIGH | 🟡 P1 | Medium (monitoring infra) |
| Unicorn Listing | LOW | MEDIUM | 🟢 P2 | Low (distribution check) |

---

## Your Turn

For your own project:

| # | Failure Mode | Likelihood | Impact | Mitigation |
|---|-------------|-----------|--------|------------|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

**If you can't list 5 failure modes, you don't understand the problem well enough yet.**
