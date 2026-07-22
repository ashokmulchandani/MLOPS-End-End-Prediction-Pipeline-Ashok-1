"""
Layer 2: Model Behavioral Testing
Tests that go BEYOND accuracy — checks the model learned the right thing.
Usage: pytest test_model_behavior.py -v
"""
import pytest
import numpy as np

# ── Mock Model for Practice ──
class MockHousePriceModel:
    """Simulates a trained model for testing purposes"""
    def predict(self, X):
        """X is a list of dicts with GrLivArea, OverallQual, GarageCars"""
        results = []
        for row in X:
            price = (row["GrLivArea"] * 150 +
                     row["OverallQual"] * 25000 +
                     row["GarageCars"] * 15000)
            results.append(price)
        return np.array(results)

# ── Model Tests ──
class TestModelBehavior:
    @pytest.fixture
    def model(self):
        return MockHousePriceModel()

    def test_output_shape(self, model):
        """10 inputs should produce 10 outputs"""
        houses = [{"GrLivArea": 1500, "OverallQual": 7, "GarageCars": 2}
                  for _ in range(10)]
        preds = model.predict(houses)
        assert preds.shape == (10,), f"Expected (10,), got {preds.shape}"

    def test_never_returns_nan(self, model):
        """Predictions must always be valid numbers"""
        houses = [{"GrLivArea": 1500, "OverallQual": 7, "GarageCars": 2}]
        preds = model.predict(houses)
        assert not np.isnan(preds).any(), "Model returned NaN!"
        assert not np.isinf(preds).any(), "Model returned infinity!"

    def test_always_positive(self, model):
        """House prices should always be positive"""
        houses = [{"GrLivArea": 500, "OverallQual": 1, "GarageCars": 0}]
        pred = model.predict(houses)[0]
        assert pred > 0, f"Predicted price {pred} is not positive!"

    def test_bigger_house_higher_price(self, model):
        """A bigger, better house MUST cost more than a smaller, worse one"""
        small = [{"GrLivArea": 800, "OverallQual": 3, "GarageCars": 0}]
        big = [{"GrLivArea": 3500, "OverallQual": 10, "GarageCars": 3}]
        assert model.predict(big)[0] > model.predict(small)[0], \
            "Bigger/better house predicted cheaper than smaller/worse!"

    def test_stable_with_small_noise(self, model):
        """Tiny changes in input should not cause wild prediction swings"""
        house = {"GrLivArea": 1500, "OverallQual": 7, "GarageCars": 2}
        p1 = model.predict([house])[0]
        # Add 0.1% noise
        house_noisy = {k: v * 1.001 for k, v in house.items()}
        p2 = model.predict([house_noisy])[0]
        change_pct = abs(p1 - p2) / p1
        assert change_pct < 0.01, \
            f"Too sensitive! {change_pct:.3%} change from 0.1% noise"

    @pytest.mark.parametrize("sqft,qual,cars,expected_min,expected_max", [
        (800,  3, 0, 50000,  250000),
        (1500, 7, 2, 200000, 600000),
        (4000, 10, 4, 500000, 1200000),
    ])
    def test_price_in_reasonable_range(self, model, sqft, qual, cars, expected_min, expected_max):
        """Price should be in a reasonable range for the given features"""
        house = [{"GrLivArea": sqft, "OverallQual": qual, "GarageCars": cars}]
        pred = model.predict(house)[0]
        assert expected_min < pred < expected_max, \
            f"Price {pred:.0f} outside expected range {expected_min}-{expected_max}"
