# 3.9 — Pipeline Versioning

> Reference: Slide 3.9 of `phase3_feature_engineering.html`

## What Must Be Versioned

| Artifact | Example | Stored In |
|----------|---------|-----------|
| Scaler (mean, std per col) | GrLivArea: μ=1515, σ=525 | pipeline.pkl (MLflow) |
| Encoder mappings | "Downtown" → column 5 | pipeline.pkl (MLflow) |
| Imputer values | LotFrontage median = 68ft | pipeline.pkl (MLflow) |
| Dropped columns list | PoolQC, Alley, Fence | MLflow param |
| Feature cross formulas | GrLivArea × OverallQual | MLflow param |
| Pipeline version | v1.0 | MLflow tag |

## When to Bump Version

| Change | Version |
|--------|---------|
| New imputation strategy | Minor (v1.1) |
| New feature added | Minor (v1.2) |
| Feature removed | Major (v2.0) |
| New scaler type | Major (v2.0) |
| New encoder | Major (v2.0) |

## MLflow Logging Template

```python
mlflow.log_param("pipeline_version", "v1.0")
mlflow.log_param("scaler", "StandardScaler")
mlflow.log_param("imputer_num", "median")
mlflow.log_param("encoder", "OneHotEncoder(handle_unknown=ignore)")
mlflow.log_param("dropped_cols", "PoolQC,Alley,Fence,MiscFeature")
mlflow.set_tag("pipeline_version", "v1.0")
```
