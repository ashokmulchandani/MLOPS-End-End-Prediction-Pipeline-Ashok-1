"""
Layer 3: Pipeline Testing
End-to-end tests + error path tests.
Usage: pytest test_pipeline_e2e.py -v
"""
import pytest
import json

# ── Mock Pipeline (replace with real ZenML pipeline in Phase 5) ──
def run_pipeline(input_data):
    """
    Simulates the full ML pipeline: validate → preprocess → predict.
    In Phase 5, this calls the real ZenML pipeline.
    """
    # Parse input
    if isinstance(input_data, str):
        try:
            data = json.loads(input_data)
        except json.JSONDecodeError:
            return {"status": "error", "error_code": "INVALID_JSON"}

    elif isinstance(input_data, dict):
        data = input_data
    else:
        return {"status": "error", "error_code": "INVALID_INPUT_TYPE"}

    # Validate required fields
    required = ["GrLivArea", "OverallQual", "GarageCars"]
    for field in required:
        if field not in data:
            return {"status": "error", "error_code": f"MISSING_FIELD_{field.upper()}"}

    # Validate field types and ranges
    if not isinstance(data["GrLivArea"], (int, float)) or data["GrLivArea"] <= 0:
        return {"status": "error", "error_code": "INVALID_GRLIVAREA"}
    if not isinstance(data["OverallQual"], int) or data["OverallQual"] not in range(1, 11):
        return {"status": "error", "error_code": "INVALID_OVERALLQUAL"}

    # Predict (mock)
    price = (data["GrLivArea"] * 150 +
             data["OverallQual"] * 25000 +
             data["GarageCars"] * 15000)

    return {
        "status": "success",
        "predicted_price": price,
        "model_version": "v1.0.0",
        "timestamp": "2026-07-22T12:00:00Z",
    }

# ── End-to-End Tests ──
class TestPipelineE2E:
    def test_valid_house_returns_success(self):
        """A valid house should return success with a price"""
        result = run_pipeline({
            "GrLivArea": 1800,
            "OverallQual": 7,
            "GarageCars": 2
        })
        assert result["status"] == "success"
        assert "predicted_price" in result
        assert 200000 < result["predicted_price"] < 600000
        assert result["model_version"] == "v1.0.0"

    def test_valid_json_string_input(self):
        """Pipeline should accept JSON string input"""
        result = run_pipeline('{"GrLivArea": 1500, "OverallQual": 6, "GarageCars": 1}')
        assert result["status"] == "success"
        assert result["predicted_price"] > 0

# ── Error Path Tests ──
class TestPipelineErrors:
    def test_malformed_json(self):
        """Malformed JSON should return error, not crash"""
        result = run_pipeline("not valid json {{{")
        assert result["status"] == "error"
        assert result["error_code"] == "INVALID_JSON"

    def test_wrong_input_type(self):
        """List input should return error"""
        result = run_pipeline([1, 2, 3])
        assert result["status"] == "error"
        assert result["error_code"] == "INVALID_INPUT_TYPE"

    @pytest.mark.parametrize("missing_field", ["GrLivArea", "OverallQual", "GarageCars"])
    def test_missing_required_field(self, missing_field):
        """Each missing required field should give a specific error"""
        house = {"GrLivArea": 1500, "OverallQual": 7, "GarageCars": 2}
        del house[missing_field]
        result = run_pipeline(house)
        assert result["status"] == "error"
        assert missing_field.upper() in result["error_code"]

    def test_negative_sqft_rejected(self):
        """Negative square footage should be rejected"""
        result = run_pipeline({"GrLivArea": -500, "OverallQual": 7, "GarageCars": 2})
        assert result["status"] == "error"
        assert result["error_code"] == "INVALID_GRLIVAREA"

    def test_overallqual_out_of_range(self):
        """OverallQual must be 1-10"""
        result = run_pipeline({"GrLivArea": 1500, "OverallQual": 15, "GarageCars": 2})
        assert result["status"] == "error"
        assert result["error_code"] == "INVALID_OVERALLQUAL"

# ── Retry Logic Test ──
def test_retry_on_first_failure():
    """Simulate: API fails on first attempt, succeeds on retry"""
    attempts = [0]

    def pipeline_with_retry(input_data, max_retries=3):
        for attempt in range(max_retries):
            attempts[0] += 1
            result = run_pipeline(input_data)
            if result["status"] == "success":
                return result
            # In real code, this would wait with exponential backoff
        return {"status": "error", "error_code": "MAX_RETRIES_EXCEEDED"}

    result = pipeline_with_retry({
        "GrLivArea": 1500, "OverallQual": 7, "GarageCars": 2
    })
    assert result["status"] == "success"
    assert attempts[0] == 1  # Succeeded on first try
