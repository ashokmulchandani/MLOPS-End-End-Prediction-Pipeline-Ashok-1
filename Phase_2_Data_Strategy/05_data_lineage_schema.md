# 2.5 — Data Lineage Schema

> **Objective:** Design a schema for tracking every training example's origin.
> Reference: Slide 2.5 of `phase2_data_strategy.html`

---

## Why Lineage Matters

When a model prediction is wrong in production, you need to answer:
- Which training examples influenced this prediction?
- When were those examples added to the dataset?
- Has the labeling schema changed since then?

Without lineage, debugging is guesswork.

---

## House Prices: Lineage Schema

```yaml
# Each row in the training set should carry these fields:
row_id: "ames_0001"
source: "Ames City Assessor, parcel ID 0527400001"
collector: "Dean De Cock, Truman State University"
collection_method: "Public records extraction"
injection_date: "2011-01-15"            # When it entered the dataset
label_version: "v1.0 — nominal sale price, not inflation-adjusted"
label_date: "2008-08-01"                # When the sale was recorded
data_version: "ames_v1.0"
dvc_hash: "a1b2c3d4"                    # Link to exact DVC-tracked data
```

---

## Lineage Pipeline

```
Source → Collector → Injection Date → Label Version → Data Version → Training Row
  │          │             │               │               │
  │          │             │               │               └─ DVC-tracked
  │          │             │               └─ Schema version of the label
  │          │             └─ When this row entered the pipeline
  │          └─ Who/what system created this data
  └─ Origin system (API, database, scrape, sensor)
```

---

## Your Turn

Design your lineage schema:

| Field | Description | Your Value |
|-------|-------------|------------|
| `source` | Where did this data originate? | |
| `collector` | Who/what system collected it? | |
| `injection_date` | When did it enter the training pipeline? | |
| `label_version` | What labeling schema/version was used? | |
| `data_version` | What dataset version is this? | |
| `dvc_hash` | Link to the exact DVC-tracked data file? | |
