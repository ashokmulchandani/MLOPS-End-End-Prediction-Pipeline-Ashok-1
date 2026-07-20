# 1.1 — Does This Problem Need ML? (Decision Doc)

> **Objective:** Apply the 6-word test to determine if ML is the right approach.
> Reference: Slide 1.1 of `phase1_system_design.html`

---

## The Problem (1-liner)

Real estate agents need fast, accurate house price estimates. Currently they manually compare comparable properties — slow, inconsistent, and experience-dependent.

---

## The 6-Word Test

A problem is a good ML candidate if **ALL six** words apply:

| Word | Question | House Prices Answer | Pass? |
|------|----------|---------------------|-------|
| **Learn** | Can the solution be derived from first principles, or must it be learned from data? | No formula exists — price depends on 80+ interacting features. Must be learned. | ✅ |
| **Complex** | Is the input→output relationship too complex for hand-coded rules? | Yes — location quality, basement finish, lot slope, neighborhood trends. Rules would be brittle. | ✅ |
| **Patterns** | Are there recurring patterns in the data? | Yes — similar houses sell for similar prices. OverallQual correlates at 0.80 with price. | ✅ |
| **Existing Data** | Does labeled data already exist? | Yes — 2,930 rows of historical sales from Ames, Iowa with 82 features + SalePrice. | ✅ |
| **Predictions** | Is the goal to predict on unseen cases (not just describe the past)? | Yes — predict price for new listings that have never sold before. | ✅ |
| **Unseen Data** | Must the model generalize to examples never seen during training? | Yes — every new listing is a unique combination of features. | ✅ |

---

## Verdict

**✅ ML IS justified.** All 6 words apply. The House Prices problem passes the test.

---

## Your Turn

For your own project, fill this out:

| Word | Question | Your Answer | Pass? |
|------|----------|-------------|-------|
| **Learn** | Can it be derived from first principles, or must be learned? | | ⬜ |
| **Complex** | Too complex for hand-coded rules? | | ⬜ |
| **Patterns** | Are there recurring patterns? | | ⬜ |
| **Existing Data** | Does labeled data exist? | | ⬜ |
| **Predictions** | Is the goal prediction on unseen cases? | | ⬜ |
| **Unseen Data** | Must it generalize to unseen examples? | | ⬜ |

**Verdict:** ⬜ ML Justified / ⬜ Use Rules / ⬜ Not Now (Collect Data)

---

## Notes

- If even ONE word fails, seriously consider rules or "not now"
- "Existing Data" is the most common failure — no labels = no supervised ML
- The 6-word test saves months of wasted effort. Use it on every project.
