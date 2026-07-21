# 4.5 — Logging Schema

```json
{
  "prediction_id": "uuid",
  "timestamp": "ISO 8601",
  "model_version": "baseline_v0",
  "input_features": { "...all 82 features..." },
  "predicted_price": 247500,
  "listing_id": "MLS-98765",
  "actual_sale_price": 255000,
  "sale_date": "2026-09-15",
  "error": -7500,
  "error_percent": -2.9
}
```

**Critical:** Actual sale price MUST be captured later. Without it, no feedback loop.
