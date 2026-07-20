# 2.1 — Data Source Inventory

> **Objective:** Identify and document every data source, its biases, and its limitations.
> Reference: Slide 2.1 of `phase2_data_strategy.html`

---

## House Prices: Data Source Inventory

| Field | Value |
|-------|-------|
| **Dataset Name** | Ames Housing Dataset |
| **Source** | Kaggle / Ames City Assessor's Office |
| **Collector** | Dean De Cock, Truman State University |
| **Time Period** | 2006–2010 |
| **Geography** | Ames, Iowa, USA |
| **Rows** | 2,930 |
| **Features** | 82 (38 numerical + 43 categorical + 1 target) |
| **Target** | SalePrice (USD) |
| **License** | Public domain (public records) |

### Biases Identified

| Bias | Description | Mitigation |
|------|-------------|------------|
| **Geographic** | Only Ames, Iowa. Model will NOT generalize to NYC, rural Texas, or coastal markets. | Retrain on local data for each market. |
| **Temporal** | 16+ years old. Post-2020 market patterns are different. | Monthly retraining with recent sales. |
| **Selection** | Only properties that SOLD. No data on listings that failed to sell. | Model may overprice — doesn't learn from overpriced failures. |
| **Missing Data** | PoolQC 99.7% null, Alley 93% null, Fence 80% null. | Expected — most homes lack these features. Monitor for CHANGES in null rate. |

### Data Source Quality Score

| Dimension | Score | Notes |
|-----------|-------|-------|
| Completeness | 🟡 7/10 | Some features heavily missing, but expected |
| Accuracy | 🟢 9/10 | Public records — legally required accuracy |
| Consistency | 🟢 9/10 | Standardized assessment format |
| Timeliness | 🔴 3/10 | 16 years old — needs supplementing |
| Bias Risk | 🟡 6/10 | Geographic + temporal bias |

---

## Your Turn

| Field | Your Value |
|-------|-----------|
| **Dataset Name** | |
| **Source** | |
| **Rows / Features** | |
| **Target** | |
| **Time Period** | |

**Biases to watch for:**
- [ ] Geographic: Does this represent all markets you serve?
- [ ] Temporal: Is the data recent enough?
- [ ] Selection: Who/what is EXCLUDED from this data?
- [ ] Missing: Are nulls random or systematic?
