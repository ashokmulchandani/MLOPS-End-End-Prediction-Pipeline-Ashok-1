# 4B.7 — Layer 3: Pipeline Testing

## End-to-End Test

Run the ENTIRE pipeline on test input. Verify status, output, model version.

## Error Path Tests

- Malformed input → graceful error, not crash
- API failure → retry logic works
- Missing file → clear error message
- Duplicate ID → idempotent handling

## Rule

> Test the error handlers harder than the happy path. Error handler bugs cause outages.
