# 2.9 — DVC Setup (Data Version Control)

> **Objective:** Version your data the way Git versions your code.
> Reference: Slide 2.9 of `phase2_data_strategy.html`

---

## Why DVC?

Git + large files = pain:
- GitHub rejects files > 100MB
- `git clone` takes forever with 1GB of CSV history
- Can't diff data files meaningfully

**DVC solves this:** Stores metadata in Git (tiny `.dvc` files), stores actual data elsewhere.

---

## DVC Quick Start

```bash
# 1. Install
pip install dvc

# 2. Initialize (in your project root)
dvc init
git add .dvc/ .dvcignore
git commit -m "Initialize DVC"

# 3. Track a data file
dvc add extracted_data/AmesHousing.csv
# → Creates: extracted_data/AmesHousing.csv.dvc (tiny metadata file)
# → Adds: extracted_data/AmesHousing.csv to .gitignore

# 4. Commit the .dvc file to Git
git add extracted_data/AmesHousing.csv.dvc extracted_data/.gitignore
git commit -m "Track Ames Housing v1.0 with DVC"

# 5. Set up remote storage (S3, GCS, or local)
dvc remote add -d myremote s3://my-bucket/dvc-store
# Or for local:
dvc remote add -d myremote /path/to/shared/drive

# 6. Push data to remote
dvc push

# 7. Anyone can now clone + pull data
git clone <repo>
dvc pull   # gets the exact data version
```

---

## What Gets Committed to Git vs DVC

| Git (small files) | DVC (large files) |
|-------------------|-------------------|
| `data.csv.dvc` (hash reference) | `data.csv` (actual data) |
| `dvc.yaml` (pipeline definition) | Model weights, embeddings |
| `.dvc/` (config) | Any file > a few MB |

---

## House Prices: DVC Plan

```bash
# Track the Ames Housing dataset
dvc add extracted_data/AmesHousing.csv

# Track any processed versions
dvc add data/train.csv
dvc add data/test.csv

# Re-run when data changes
dvc add extracted_data/AmesHousing.csv  # updates hash in .dvc file
git commit -m "Ames Housing v1.1 — removed outliers"
dvc push
```

---

## Your Turn

```bash
# Steps to version your data:
dvc init
dvc add _________________
git add _________________
git commit -m "_________________"
dvc remote add -d myremote _________________
dvc push
```
