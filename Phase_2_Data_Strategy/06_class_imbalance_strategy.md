# 2.6 — Class Imbalance Strategy

> **Objective:** Handle skewed class distributions so the model doesn't ignore minority classes.
> Reference: Slide 2.6 of `phase2_data_strategy.html`

---

## The 99% Accuracy Trap

A model that always predicts "not fraud" gets 99% accuracy when fraud is 1% of transactions. It also catches **zero fraud**. Accuracy is meaningless for imbalanced problems.

---

## Five Techniques (Classification)

| Technique | How It Works | Pros | Cons |
|-----------|-------------|------|------|
| **Undersampling** | Delete majority class rows | Simple, fast | Loses valuable data |
| **Oversampling** | Duplicate minority rows | No data loss | Overfitting on duplicates |
| **SMOTE** | Synthesize NEW minority examples | Better than duplication | Doesn't work well with high-D data |
| **Class Weights** | Penalize minority-class errors more | No data modification | Must tune weight values |
| **Focal Loss** | Auto-downweight easy examples | State of the art | PyTorch/TF only, not sklearn |

---

## House Prices: Regression, Not Classification

Class imbalance applies to **categorical targets** (fraud/not, churn/stay). House Prices uses **regression** (continuous SalePrice).

However, regression has its own "imbalance" problem:

| Issue | Impact | Mitigation |
|-------|--------|------------|
| Price distribution is right-skewed | Model underfits expensive homes | Log-transform SalePrice |
| 90% of homes are $100K-$300K | Model optimizes for the middle | Sample weights by price tier |
| Only 1% of homes > $500K | Luxury predictions are poor | Stratify by price quartile for evaluation |

**For this project:** Log transformation (Phase 5, Step 5D.4) handles most of the skew. Class imbalance techniques aren't needed for regression.

---

## Your Turn

| Question | Your Answer |
|----------|-------------|
| Is your target categorical or continuous? | |
| If categorical: what's the minority class percentage? | |
| If continuous: is the target skewed? | |
| Which technique will you use? | |
| How will you verify the technique is working? | |
