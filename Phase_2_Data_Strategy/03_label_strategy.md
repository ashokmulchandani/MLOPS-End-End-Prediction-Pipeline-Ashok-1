# 2.3 — Label Strategy

> **Objective:** Define how labels (ground truth) are obtained, at what cost, and with what quality.
> Reference: Slide 2.3 of `phase2_data_strategy.html`

---

## Label Strategy Comparison

| Strategy | Cost | Quality | Speed | Example |
|----------|------|---------|-------|---------|
| **Hand Labels** | $$$$ | ⭐⭐⭐⭐⭐ | Slow | Radiologists labeling tumors |
| **Natural Labels** | Free | ⭐⭐⭐ | Fast | User click = positive signal |
| **Weak Supervision** | $ | ⭐⭐ | Medium | Regex rules label text |
| **Active Learning** | $$ | ⭐⭐⭐⭐ | Medium | Model picks confusing examples for humans |
| **LLM-as-Labeler** | $$ | ⭐⭐⭐ | Fast | GPT-4 classifies support tickets |
| **Existing Records** | Free | ⭐⭐⭐⭐⭐ | Instant | Historical sales data, loan outcomes |

---

## House Prices: Decision

**Strategy:** Existing Records (the ideal scenario)

**Label:** SalePrice — actual sale price in USD from public property records

**Quality assessment:**
- ✅ Legally recorded — minimal noise
- ✅ No labeling cost — historical data already exists
- ✅ Every row has a label — no missing targets
- ⚠️ Label delay: ~30-60 days from listing to recorded sale
- ⚠️ Only captures SOLD properties — no data on overpriced failures

---

## Your Turn

| Question | Your Answer |
|----------|-------------|
| Does labeled data already exist? | |
| If yes: how was it labeled? By whom? | |
| If no: how will you get labels? | |
| What's the cost per label? | |
| What's the expected label quality? | |
| Is there a delay between prediction and label availability? | |

**Chosen strategy:** _______________
