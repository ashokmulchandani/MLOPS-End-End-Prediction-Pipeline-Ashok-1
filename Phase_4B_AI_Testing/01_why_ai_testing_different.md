# 4B.1 — Why Testing AI Is Different

## 3 Key Differences from Regular Software

1. **Non-Deterministic:** Same input can produce different output. Test ranges and invariants, not exact values.
2. **Data IS Part of the System:** Code unchanged but data changed → system broken. Test data as rigorously as code.
3. **Degrades Over Time:** The world drifts. Production monitoring is mandatory, not optional.

## Interview Answer

"Three things. AI outputs are non-deterministic — you test ranges, shapes, and invariants, not `result == expected`. The data IS part of the system — you test the data pipeline as rigorously as the code. And AI degrades silently over time in ways regular software doesn't — you need production monitoring for drift, not just uptime."
