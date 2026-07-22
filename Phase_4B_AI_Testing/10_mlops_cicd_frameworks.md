# 4B.10 — MLOps CI/CD + Framework Cheat Sheet

## Commit → Production Flow

```
Commit → Unit Tests → Data Validation → Feature Validation →
Train Model → Evaluate → Compare with Previous → Deploy Staging →
Smoke Tests → Human Approval → Production → Monitor Drift
```

## Framework Categories

| Category | Tools |
|----------|-------|
| Testing | pytest, Great Expectations, Pandera, Promptfoo, DeepEval, Ragas |
| Tracking | MLflow, Weights & Biases |
| Monitoring | Evidently AI, WhyLabs, Arize AI, LangSmith |
| CI/CD | GitHub Actions, GitLab CI, Jenkins |
| Workflow | Kubeflow, Airflow, Dagster, Prefect |
