# 2.4 — Implicit Negatives

> **Objective:** Define rules for inferring negative labels when only positives are explicit.
> Reference: Slide 2.4 of `phase2_data_strategy.html`

---

## What Are Implicit Negatives?

When you only have positive signals (clicks, purchases, saves), you must INFER what counts as a negative:

> "User was SHOWN this listing and did NOT click within X time → implicit negative"

---

## The Time Window Tradeoff

| Window | Pro | Con |
|--------|-----|-----|
| 1 second | Fast feedback | User hasn't even read the content — false negative |
| 1 minute | User had time to scan | May have been distracted |
| 10 minutes | Reasonable engagement window | Delayed training signal |
| 1 day | Covers revisit behavior | Many confounds (user was busy, on vacation) |
| Never | No false negatives | Can't train a classifier with only positives |

---

## House Prices: NOT Applicable

This step is NOT relevant to the House Prices project because:
- We have **explicit labels** — the actual sale price for every row
- No inference needed — every house in the dataset sold, so the label is known

### Where This WOULD Apply

If we built a real estate **recommendation system**:
- **Implicit Positive:** User saved listing, shared listing, spent > 60s viewing
- **Implicit Negative:** User saw listing in search results, did NOT click (within 10 min session)
- **Strong Negative:** User saw listing 3+ times across sessions, never clicked

---

## Your Turn

| Question | Your Answer |
|----------|-------------|
| Do you need implicit negatives? (Or do you have explicit labels?) | |
| What user action counts as positive? | |
| What time window defines a negative? | |
| What's the risk of false negatives? | |
