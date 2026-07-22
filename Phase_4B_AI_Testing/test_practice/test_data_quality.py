"""
Layer 1: Data Testing
Run BEFORE training. If any test fails, fix the data first.
Usage: pytest test_data_quality.py -v
"""
import pytest
import pandas as pd
import numpy as np

# ── Fixtures ──
@pytest.fixture
def sample_df():
    """Create a small test DataFrame that mimics Ames Housing"""
    return pd.DataFrame({
        "GrLivArea":   [1500, 2400, 1800, 3500, 900],
        "SalePrice":   [215000, 340000, 185000, -50000, 620000],  # Note: row 3 has negative!
        "YearBuilt":   [2005, 2010, 1998, 2027, 1972],  # Note: row 3 is year 2027!
        "OverallQual": [7, 8, 6, 9, 99],  # Note: row 4 has 99 (out of range)!
        "Bedrooms":    [3, 4, 3, -1, 5],  # Note: row 3 has -1!
    })

@pytest.fixture
def df_with_leakage():
    """DataFrame with target leakage"""
    return pd.DataFrame({
        "GrLivArea": [1500, 2400],
        "SalePrice": [215000, 340000],
        "PricePerSqft": [143, 141],  # LEAKAGE: SalePrice / GrLivArea
    })

# ── Schema Tests ──
class TestSchemaValidation:
    def test_grlivarea_in_valid_range(self, sample_df):
        """GrLivArea should be between 300 and 6000 sqft"""
        invalid = sample_df[(sample_df["GrLivArea"] < 300) | (sample_df["GrLivArea"] > 6000)]
        assert len(invalid) == 0, f"Found {len(invalid)} rows with invalid GrLivArea:\n{invalid}"

    def test_saleprice_not_negative(self, sample_df):
        """SalePrice must be positive"""
        negative = sample_df[sample_df["SalePrice"] < 0]
        assert len(negative) == 0, f"Found negative SalePrice:\n{negative}"

    def test_yearbuilt_in_valid_range(self, sample_df):
        """YearBuilt must be between 1800 and current year"""
        current_year = 2026
        invalid = sample_df[(sample_df["YearBuilt"] < 1800) | (sample_df["YearBuilt"] > current_year)]
        assert len(invalid) == 0, f"Found invalid YearBuilt:\n{invalid}"

    def test_overallqual_in_range_1_to_10(self, sample_df):
        """OverallQual must be 1-10"""
        invalid = sample_df[~sample_df["OverallQual"].isin(range(1, 11))]
        assert len(invalid) == 0, f"Found invalid OverallQual:\n{invalid}"

    def test_bedrooms_non_negative(self, sample_df):
        """Bedrooms cannot be negative"""
        negative = sample_df[sample_df["Bedrooms"] < 0]
        assert len(negative) == 0, f"Found negative Bedrooms:\n{negative}"

# ── Leakage Tests ──
class TestLeakageDetection:
    def test_no_target_derived_columns(self, df_with_leakage):
        """Features must not contain columns derived from the target"""
        forbidden = ["PricePerSqft", "SalePrice_Normalized", "LogSalePrice",
                     "SalePricePerBedroom", "SalePricePerSqft"]
        for col in forbidden:
            assert col not in df_with_leakage.columns, \
                f"LEAKAGE DETECTED: '{col}' is derived from SalePrice!"

# ── Null Rate Tests ──
def test_required_columns_no_nulls():
    """Critical columns should NEVER be null"""
    df = pd.DataFrame({
        "GrLivArea": [1500, None, 1800],
        "SalePrice": [215000, 340000, None],
    })
    critical_cols = ["GrLivArea", "SalePrice"]
    for col in critical_cols:
        null_count = df[col].isnull().sum()
        assert null_count == 0, f"{col} has {null_count} nulls — should be 0!"
