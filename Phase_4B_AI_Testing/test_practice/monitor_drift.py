"""
Layer 4: Production Monitoring
Checks that run WEEKLY after deployment to detect drift.
Usage: python monitor_drift.py
In production, this would run as a scheduled job (cron / GitHub Actions).
"""
import numpy as np
import pandas as pd
from dataclasses import dataclass
from typing import List

# ── Simplified PSI (Population Stability Index) Calculator ──
def calculate_psi(expected: np.ndarray, actual: np.ndarray, bins: int = 10) -> float:
    """
    Population Stability Index — measures how much a distribution has shifted.
    PSI < 0.1 = stable
    PSI 0.1-0.2 = investigate
    PSI > 0.2  = retrain
    """
    # Create bins from combined data
    combined = np.concatenate([expected, actual])
    bin_edges = np.percentile(combined, np.linspace(0, 100, bins + 1))

    # Count per bin
    expected_counts, _ = np.histogram(expected, bins=bin_edges)
    actual_counts, _ = np.histogram(actual, bins=bin_edges)

    # Convert to proportions (add small epsilon to avoid division by zero)
    eps = 0.0001
    expected_props = (expected_counts / len(expected)) + eps
    actual_props = (actual_counts / len(actual)) + eps

    # PSI = sum((actual% - expected%) * ln(actual% / expected%))
    psi = np.sum((actual_props - expected_props) * np.log(actual_props / expected_props))
    return psi

# ── Alert System ──
@dataclass
class Alert:
    feature: str
    severity: str  # 'ok', 'warn', 'critical'
    psi_score: float
    message: str

def check_feature_health(train_df: pd.DataFrame, live_df: pd.DataFrame) -> List[Alert]:
    """Check all numerical features for drift"""
    alerts = []
    numerical_cols = train_df.select_dtypes(include=[np.number]).columns

    for col in numerical_cols:
        psi = calculate_psi(train_df[col].values, live_df[col].values)

        if psi > 0.2:
            alerts.append(Alert(col, "critical", psi,
                f"🔴 {col}: PSI={psi:.3f} — RETRAIN RECOMMENDED"))
        elif psi > 0.1:
            alerts.append(Alert(col, "warn", psi,
                f"🟡 {col}: PSI={psi:.3f} — investigate"))
        else:
            alerts.append(Alert(col, "ok", psi,
                f"🟢 {col}: PSI={psi:.3f} — stable"))

    return alerts

def check_null_rates(train_df: pd.DataFrame, live_df: pd.DataFrame, tolerance: float = 0.05):
    """Alert if null rate changes significantly from baseline"""
    train_nulls = train_df.isnull().mean()
    live_nulls = live_df.isnull().mean()

    for col in train_df.columns:
        drift = abs(live_nulls[col] - train_nulls[col])
        if drift > tolerance:
            yield Alert(col, "critical", drift,
                f"🔴 {col}: null rate changed {drift:.1%} (train={train_nulls[col]:.1%}, live={live_nulls[col]:.1%})")

# ── Self-Test ──
if __name__ == "__main__":
    print("=" * 60)
    print("FEATURE HEALTH MONITORING — Weekly Check")
    print("=" * 60)

    # Simulate training data (baseline)
    np.random.seed(42)
    train_df = pd.DataFrame({
        "GrLivArea":   np.random.normal(1515, 525, 2930),
        "OverallQual": np.random.normal(6.1, 1.4, 2930),
        "LotArea":     np.random.lognormal(9, 0.7, 2930),
        "YearBuilt":   np.random.normal(1971, 30, 2930),
        "SalePrice":   np.random.lognormal(12, 0.4, 2930),
    })

    # Simulate live data (with drift on some features)
    live_df = pd.DataFrame({
        "GrLivArea":   np.random.normal(1800, 600, 1000),   # ↑ shifted +285 sqft
        "OverallQual": np.random.normal(6.1, 1.4, 1000),    # stable
        "LotArea":     np.random.lognormal(9.2, 0.8, 1000),  # ↑ slightly bigger lots
        "YearBuilt":   np.random.normal(2005, 15, 1000),    # ↑ much newer!
        "SalePrice":   np.random.lognormal(12.2, 0.5, 1000),# ↑ prices up
    })

    # Run drift check
    print("\n📈 PSI DRIFT CHECK:")
    print("-" * 40)
    alerts = check_feature_health(train_df, live_df)
    for alert in alerts:
        print(alert.message)

    # Summary
    criticals = [a for a in alerts if a.severity == "critical"]
    warnings = [a for a in alerts if a.severity == "warn"]
    print(f"\n📊 SUMMARY: {len(criticals)} critical, {len(warnings)} warnings, "
          f"{len(alerts)-len(criticals)-len(warnings)} stable")

    if criticals:
        print("\n⚠️  RECOMMENDATION: Schedule retraining. Drift detected on:")
        for a in criticals:
            print(f"   - {a.feature} (PSI={a.psi_score:.3f})")
    else:
        print("\n✅ All features within acceptable range. No retraining needed.")
