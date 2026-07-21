# 3.5 — Categorical Encoding Strategy

> Reference: Slide 3.5 of `phase3_feature_engineering.html`

## Methods

| Method | Use When | Example |
|--------|----------|---------|
| One-Hot | < 50 unique values | MSZoning (5 values) |
| Label/Ordinal | Natural order exists | OverallQual: Poor→Excellent |
| Top-K + Unknown | 50-500 unique values | ZIP codes |
| Hashing | 500+ unique values | Product IDs |

## House Prices Plan (43 Categorical Columns)

- **OneHotEncode (37 cols):** MSZoning, Street, Neighborhood, HouseStyle, RoofStyle, Exterior1st, etc.
  - `handle_unknown='ignore'` — new categories in production → all zeros
- **OrdinalEncode (6 cols):** OverallQual, OverallCond, ExterQual, KitchenQual, BsmtQual, FireplaceQu
  - Natural order: Po < Fa < TA < Gd < Ex

## Cardinality Check

| Feature | Unique Values | Method |
|---------|--------------|--------|
| Neighborhood | 25 | OneHot ✅ |
| MSZoning | 5 | OneHot ✅ |
| Exterior1st | 15 | OneHot ✅ |
| HouseStyle | 8 | OneHot ✅ |

No features exceed 50 unique values — OneHot is safe for all.
