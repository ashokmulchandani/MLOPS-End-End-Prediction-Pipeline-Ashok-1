# 4B.2 — The 3-Pass PR Review

| Pass | Focus | Questions |
|------|-------|-----------|
| ⚙️ Does it work? | Logic, edge cases, tests | "What if the list is empty?" "What if the input is null?" |
| 📖 Can I read it? | Naming, structure, duplication | "Would someone new understand this in 6 months?" |
| 🛡️ Is it safe? | Secrets, error handling, auth | "API key hardcoded?" "What if this call times out?" |

## Rule

> Every PR comment must include a suggestion, not just a criticism.
> "This could break" → "This could break if the API times out — wrap it in try/except with a retry."

## 3 Phrases to Use in Interviews

1. "I review like I'm the person getting paged at 3am when this breaks."
2. "I look for what the tests DON'T cover — everyone checks the happy path."
3. "I treat error handlers as first-class code. Most bugs I've caught were in the error paths."
