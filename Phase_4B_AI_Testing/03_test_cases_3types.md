# 4B.3 — Test Cases: Happy Path, Edge, Failure

## The 3 Types

| Type | Question | Example |
|------|----------|---------|
| ✅ Happy Path | Does it work normally? | 3 valid features → correct prediction |
| ⚠️ Edge Cases | What breaks at boundaries? | Empty list, 1 row, 1M rows, NaN |
| 💥 Failure Modes | What if outside world fails? | API timeout, DB down, corrupt file |

## Rule

> If a bug reaches production, a test gets written for it BEFORE the fix. No repeat bugs.

## Interview Phrases

- "I test the error handlers harder than the happy path."
- "Every bug that hits production gets a test written before the fix."
- "What's the worst thing that happens if this fails? Then I write a test for exactly that."
