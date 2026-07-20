# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a hands-on **MLOps & ML System Design learning project** structured as an 8-phase curriculum. It progresses from ML system design thinking through data strategy, feature engineering, baseline modeling, a full ZenML+MLflow pipeline (Phase 5), enterprise training data pipelines, monitoring, and a capstone project. The philosophy is **Think → Build → Scale** — system design thinking first, then hands-on MLOps, then enterprise-grade architecture.

This is **not a library or application** — it's a structured learning repository. There is no build, lint, or test suite. Code lives in phase directories and Jupyter notebooks.

## Repo Architecture

- `MLOPS_SYSTEM_DESIGN_PLAN.md` — the master plan: all 8 phases, 22 sessions, execution order, tools, and design patterns. **Read this first** when starting any phase-related work.
- `README.md` — project overview, phase status table, tech stack, setup instructions.
- `Phase_1_System_Design/` through `Phase_8_Capstone/` — one directory per phase. Most are currently scaffolds (`.gitkeep` only). As phases are completed, notebooks, scripts, and documentation land here.
- `prices-predictor-system/` — the fully-implemented Phase 5 reference project (ZenML + MLflow + design patterns on Ames Housing dataset). This is the core hands-on project.
- `notebooks/` — shared Jupyter notebooks.
- Transcript `.txt` files at root — YouTube video transcripts used as learning references.

## Current Progress

- ⬜ Phase 1 (ML System Design Thinking) — plan exists, not started
- ⬜ Phase 2 (Data Strategy & Engineering) — plan exists, not started
- ⬜ Phase 3 (Feature Engineering & Pipeline) — plan exists, not started
- ⬜ Phase 4 (Baseline First) — plan exists, not started
- ✅ Phase 5 (House Prices Predictor System) — **reference project exists** in `prices-predictor-system/` (needs local setup/execution)
- ⬜ Phase 6 (Enterprise Training Data Pipeline) — plan exists, not started
- ⬜ Phase 7 (Monitoring & Production Ops) — plan exists, not started
- ⬜ Phase 8 (Capstone) — plan exists, not started

## Recommended Learning Path

Follow the **Project-First Approach** from the plan:
1. Jump into Phase 5 (Prices Predictor) — learn Phases 1-4 concepts IN CONTEXT as they naturally arise
2. Phase 5 alone gives you the portfolio project
3. Phase 6 and 8 are stretch goals

## Key Libraries & Tools

| Category | Tools |
|----------|-------|
| ML Pipeline Orchestration | ZenML |
| Experiment Tracking | MLflow |
| Data Versioning | DVC |
| Model Serving | MLflow Serving, FastAPI |
| Monitoring | Evidently AI, Great Expectations |
| Feature Store | Feast (optional) |
| Dashboard | Streamlit |
| CLI | Click |
| ML | scikit-learn, pandas, numpy, seaborn, matplotlib |
| AI/LLM (Phase 6) | OpenAI API, Anthropic API |
| Async (Phase 6) | asyncio, httpx |
| Data Validation | Pydantic, Great Expectations |

## Critical Design Patterns

This project teaches software design patterns through ML pipeline code:

| Pattern | Where Used | Why |
|---------|-----------|-----|
| **Strategy Pattern** | Data cleaning, missing value handling, feature engineering, outlier detection, data splitting, model building, model evaluation | Swap algorithms without changing calling code |
| **Factory Pattern** | Data ingestion (`DataIngestorFactory`), Unified Loader (Phase 6) | Create objects without specifying exact class |
| **Template Pattern** | Missing values analysis, multivariate analysis | Define skeleton, let subclasses fill steps |
| **Pipeline Pattern** | ZenML steps chained together | Reproducible, cacheable, trackable workflows |
| **Decorator Pattern** | ZenML `@step`, `@pipeline` | Add behavior without modifying function |

## Phase 5 Project Conventions

When working on the `prices-predictor-system/`:

- All data processing uses **Strategy Pattern**: abstract base class → concrete implementations → context class
- ZenML steps are in `steps/`, pipelines in `pipelines/`, core logic in `src/`
- EDA analysis modules are in `analysis/analyze_src/`
- MLflow autolog is enabled in the model building step
- The data path in `training_pipeline.py` is hardcoded to the original author's path — **must be updated** for local execution
- Use `zenml init` before running any pipeline

### Standard QLoRA / BitsAndBytes config NOT used here
This is an MLOps project using scikit-learn, not a deep learning project. The patterns from the Fine-tuning project (LoRA, quantization) do not apply.

## Phase 6 Architecture Patterns (Future)

The Enterprise Training Data Pipeline follows a modular architecture:
- `core/` — models, config, logger, errors (Pydantic models, structured logging)
- `sources/` — document loaders with Factory pattern (TXT, PDF, URL, CSV)
- `processing/` — text preprocessing and smart chunking
- `tasks/` — AI generation (QA, classification, summarization)
- `ai/` — AI client abstraction (OpenAI/Anthropic)
- `evaluation/` — quality evaluation and filtering
- `export/` — multi-format dataset export
- `cli/` — Click-based CLI interface
- `dashboard/` — Streamlit app

## Transcript-to-Phase Mapping

| Transcript File | Phases Covered |
|----------------|----------------|
| `ML System Design & MLOps For Beginners.txt` | 1 (system design thinking), 2 (data strategy), 3 (features), 4 (baseline) |
| `Build ML Production Grade Projects For Free.txt` | 5 (ZenML + MLflow setup) |
| `First-Ever Production-Grade AI Project.txt` | 6 (enterprise pipeline architecture) |
| `This AI PROJECT Got My Student 50 LPA Job.txt` | 5 (prices predictor system) |
| `End To End Deep Learning Project Using MLOPS DVC Pipeline.txt` | 5, 7 (deployment, monitoring) |
