# 3.6 — Feature Crosses

> Reference: Slide 3.6 of `phase3_feature_engineering.html`

## What Is a Feature Cross?

Multiplying two features to capture their interaction: `NewFeature = FeatureA × FeatureB`

## House Prices Candidates

| Cross | Formula | Intuition |
|-------|---------|-----------|
| Luxury Score | GrLivArea × OverallQual | Large AND high-quality = luxury |
| Bath Ratio | TotalBath ÷ Bedrooms | More baths per bedroom = nicer |
| Garage Density | GarageArea ÷ GarageCars | Space per car |
| Quality Age | YearBuilt × OverallQual | Well-maintained old vs poor new |
| Basement Value | TotalBsmtSF × BsmtQual | Large AND finished = valuable |

## For Phase 5

**Start with ZERO crosses.** Only add if baseline R² < 0.85.

82 features → 3,321 possible crosses. Adding them blindly = overfitting.
