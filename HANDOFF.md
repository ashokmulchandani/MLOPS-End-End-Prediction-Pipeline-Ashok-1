# Handoff Document — MLOps & ML System Design Learning

## Session Summary

The user (Ashok) is working through their **MLOps & ML System Design Master Plan** interactively. The project follows a **Project-First Approach** — Phase 5 (Prices Predictor System) is the core implementation, with Phases 1-4 teaching the thinking beforehand. A new Phase 6G was added covering AI/ML Testing & QA with runnable practice tests.

**Session dates:** July 21-22, 2026

## Key Files

All files are in: `C:\Users\ashok\OneDrive\NOblox\MLOPS_System_Design_Thinking\`

| File/Dir | Purpose |
|-----------|---------|
| `MLOPS_SYSTEM_DESIGN_PLAN.md` | Master plan — 8 phases + 6G, all steps and deliverables |
| `CLAUDE.md` | Guidance for Claude Code when working in this repo |
| `README.md` | Project overview with phase status, visual explainer links |
| `index.html` | Dashboard landing page with all phase cards + visual explainers |
| `HANDOFF.md` | This file — session handoff document |

## Current Progress: 5/9 Modules Complete

| # | Phase | Status | HTML |
|---|-------|--------|------|
| ✅ 1 | ML System Design Thinking | Done | [phase1_system_design.html](phase1_system_design.html) |
| ✅ 2 | Data Strategy & Engineering | Done | [phase2_data_strategy.html](phase2_data_strategy.html) |
| ✅ 3 | Feature Engineering & Pipeline | Done | [phase3_feature_engineering.html](phase3_feature_engineering.html) |
| ✅ 4 | Baseline First | Done | [phase4_baseline_first.html](phase4_baseline_first.html) |
| ⬜ 5 | House Prices Predictor System | Pending | — |
| ⬜ 6 | Enterprise Training Data Pipeline | Pending | — |
| ✅ 6G | AI/ML Testing & QA | Done | [phase4b_ai_testing.html](phase4b_ai_testing.html) |
| ⬜ 7 | Monitoring & Production Ops | Pending | — |
| ⬜ 8 | Capstone Project | Pending | — |

## Visual Explainers (Interactive HTMLs)

| Topic | File | Description |
|-------|------|-------------|
| Class Imbalance (2.6) | [class_imbalance_visualizer.html](class_imbalance_visualizer.html) | 5 techniques applied live to same dataset |
| Train/Test Split (2.7) | [train_test_split_visualizer.html](train_test_split_visualizer.html) | Which split for houses vs stocks vs users |
| Data Quality Gates (2.8) | [data_quality_visualizer.html](data_quality_visualizer.html) | 4-layer inspection pipeline |
| Label Strategy (2.3) | [label_strategy_visualizer.html](label_strategy_visualizer.html) | 6 ways to get labels compared |
| Feature Profiling (3.1) | [feature_profiling_visualizer.html](feature_profiling_visualizer.html) | Histograms, correlations, missing charts |
| Missing Values (3.2) | [missing_values_visualizer.html](missing_values_visualizer.html) | WHY before HOW — 5 scenarios |
| Feature Monitoring (3.10) | [feature_monitoring_visualizer.html](feature_monitoring_visualizer.html) | Live drift dashboard |

## Phase 6G Practice Tests

5 runnable test files in [Phase_4B_AI_Testing/test_practice/](Phase_4B_AI_Testing/test_practice/):
- `test_data_quality.py` — schema, ranges, leakage
- `test_model_behavior.py` — shape, NaN, directional, stability
- `test_pipeline_e2e.py` — E2E flow, error paths, retry
- `monitor_drift.py` — PSI drift detection
- `test_enterprise_pipeline.py` — Unit tests for Phase 6 patterns

## User Preferences

- Prefers **interactive HTML** over static explanations
- Likes **quizzes** at the end of each topic
- Wants **concrete examples** (House Prices project throughout)
- Prefers **dark/light theme toggle** on every HTML
- Uses **arrow keys** for navigation
- Wants the **"why"** before the "how"
- Prefers **visual, interactive explainers** for complex concepts

## What Needs to Happen Next

1. **Phase 5 (House Prices Predictor)** — The core implementation. Set up ZenML + MLflow locally, run the pipeline.
2. **Phase 6 (Enterprise Pipeline)** — Async document loading, AI generation, quality evaluation.
3. **Phase 7 (Monitoring)** — Drift detection, retraining triggers.
4. **Phase 8 (Capstone)** — Customer churn end-to-end.

## Repo URLs

- **Project repo:** https://github.com/ashokmulchandani/MLOPS-End-End-Prediction-Pipeline-Ashok-1.git
- **GitHub Pages:** https://ashokmulchandani.github.io/MLOPS-End-End-Prediction-Pipeline-Ashok-1/
