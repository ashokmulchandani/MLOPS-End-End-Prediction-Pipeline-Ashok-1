# 4B.6 — Layer 2: Model Testing

## 5 Behavioral Tests

| Test | What It Checks | Example |
|------|---------------|---------|
| Output Shape | Returns correct dimensions | 10 inputs → 10 outputs |
| Never NaN | Predictions always valid | assert not isnan(preds) |
| Directional | Sanity check on logic | bigger house → higher price |
| Baseline | Beats dumb rule | ML > $/sqft formula |
| Invariance | Stable with small noise | ±5% with tiny perturbation |

## Why

Accuracy alone is misleading. Behavioral tests catch what accuracy hides.
