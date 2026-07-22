# 4B.5 — Layer 1: Data Testing

## Key Tools

- **Pandera:** Schema validation for pandas DataFrames
- **Great Expectations:** Data quality test suite
- **Pydantic:** Type validation for data models
- **DVC:** Data versioning

## What to Validate

- [ ] Schema: right columns, right types
- [ ] Ranges: values in valid bounds
- [ ] Nulls: expected null rates
- [ ] Labels: valid label values
- [ ] Leakage: no target-derived features

## Rule

> If validation fails, DON'T train. Fix the data first.
