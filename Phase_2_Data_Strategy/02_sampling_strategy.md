# 2.2 — Sampling Strategy

> **Objective:** Choose a sampling method that gives a representative training set.
> Reference: Slide 2.2 of `phase2_data_strategy.html`

---

## Four Sampling Methods

| Method | How It Works | Best For | Risk |
|--------|-------------|----------|------|
| **Simple Random** | Every row equal probability | Independent, well-mixed data | Rare groups may get zero samples |
| **Stratified** | Split into groups, sample proportionally | When subgroups matter (regions, demographics) | Must know groups in advance |
| **Weighted** | Give important rows higher probability | Rare but critical cases (fraud, disease) | Can distort overall distribution |
| **Reservoir** | Sample from a stream of unknown size | Real-time data pipelines | Implementation complexity |

---

## House Prices: Decision

**Strategy:** Simple Random Split (80/20)

**Why:**
- Houses are independent observations (not time-series, not grouped by user)
- 2,930 rows is small enough that random split works
- SalePrice is continuous — stratification is tricky (would need binning)
- 5-fold cross-validation provides additional robustness

**When to use stratified instead:**
- If you need guaranteed representation across ZIP codes
- If you're comparing model fairness across neighborhoods
- If the dataset has clear subgroups with very different price distributions

---

## Your Turn

| Question | Your Answer |
|----------|-------------|
| Are your data points independent? | |
| Do you have important subgroups? | |
| Is your target categorical or continuous? | |
| How large is your dataset? | |

**Chosen strategy:** _______________

**Rationale:** _______________
