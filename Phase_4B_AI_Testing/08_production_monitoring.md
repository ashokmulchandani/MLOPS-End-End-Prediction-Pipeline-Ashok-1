# 4B.8 — Layer 4: Production Monitoring

## What to Monitor

| Signal | Tool | Alert If |
|--------|------|----------|
| Model Drift | Evidently AI | PSI > 0.2 |
| Data Drift | WhyLabs | Feature distribution shifted |
| Prediction Drift | Custom | Mean prediction shifted > 20% |
| Null Rate | Custom | > 5% change from baseline |
| Latency | Prometheus | p95 > 2× baseline |
| Cost | Custom | Per-prediction cost spike |

## Key Point

> The model can be "healthy" by DevOps standards (100% uptime, low latency) and broken by ML standards (drifting, biased, wrong). Monitor BOTH.
