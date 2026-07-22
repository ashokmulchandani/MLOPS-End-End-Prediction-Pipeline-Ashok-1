# 4B.4 — AI Testing: 4 Layers

| Layer | What | Tools |
|-------|------|-------|
| 📊 Data | Is data broken BEFORE training? | Great Expectations, Pandera, DVC |
| 🤖 Model | Does model learn the right thing? | pytest, MLflow, W&B |
| 🔗 Pipeline | Does the whole system work E2E? | pytest + Docker, GitHub Actions |
| 📈 Production | Is it still working right now? | Evidently AI, WhyLabs, Prometheus |

## Tools to Name in Interviews

- **pytest** — standard (table stakes)
- **Great Expectations** — data quality (defence data is messy)
- **MLflow** — traceability ("which model made this decision?")
- **Evidently AI** — safety-critical drift detection
