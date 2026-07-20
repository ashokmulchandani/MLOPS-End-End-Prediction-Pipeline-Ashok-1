# Handoff Document — MLOps & ML System Design Learning

## Session Summary

The user (Ashok) is working through their **MLOps & ML System Design Master Plan** interactively. They have a comprehensive 8-phase plan documented in `MLOPS_SYSTEM_DESIGN_PLAN.md`. The project follows a **Project-First Approach** — jumping into Phase 5 (Prices Predictor System) and learning Phases 1-4 concepts in context.

The reference project (`prices-predictor-system/`) is a fully-implemented MLOps pipeline from ayushsingh's tutorial, featuring ZenML orchestration, MLflow tracking, and design patterns (Factory, Strategy, Template).

## Key Files

All files are in: `C:\Users\ashok\OneDrive\NOblox\MLOPS_System_Design_Thinking\`

| File/Dir | Purpose |
|-----------|---------|
| `MLOPS_SYSTEM_DESIGN_PLAN.md` | Master plan — 8 phases, 22 sessions, all steps and deliverables |
| `CLAUDE.md` | Guidance for Claude Code when working in this repo |
| `README.md` | Project overview with phase status and setup instructions |
| `phase1_system_design.html` | Phase 1 interactive learning module — 10 slides, 10 quizzes |
| `Phase_1_System_Design/` | 10 template documents (decision doc, framing, metrics ladder, etc.) |
| `prices-predictor-system/` | Phase 5 reference project — complete ZenML + MLflow pipeline |
| `Phase_2_Data_Strategy/` through `Phase_8_Capstone/` | Phase directories (currently scaffolds) |
| `notebooks/` | Shared Jupyter notebooks |
| Transcript `.txt` files | YouTube learning references (5 transcripts) |

## Current State

- **Phase 1 (ML System Design Thinking)**: ✅ Complete — `phase1_system_design.html` interactive module built (10 slides, 10 quizzes) + 10 template documents in `Phase_1_System_Design/` covering all 10 design steps applied to the House Prices Predictor.
- **Phase 2-4**: Plans exist in `MLOPS_SYSTEM_DESIGN_PLAN.md` but no implementations yet.
- **Phase 5 (Prices Predictor)**: Reference project exists in `prices-predictor-system/` with full code (ZenML steps, MLflow tracking, design patterns). The code still has hardcoded paths from the original author (`ayushsingh`) that need updating for local execution.
- **Phases 6-8**: Architecture plans exist but not implemented. These are stretch goals.

## What Needs to Happen Next

1. **Phase 2 (Data Strategy)** — Build interactive HTML + template documents for data strategy & engineering
2. **Set up and run Phase 5 locally** — Update hardcoded paths, set up ZenML/MLflow, run the training pipeline end-to-end
3. **Phases 3-4** — Feature engineering and baseline first modules
4. **Phase 6 (Enterprise Pipeline)** — Stretch goal after Phase 5 is mastered

## User Preferences (From Fine-Tuning Project)

These preferences were established in the Fine-tuning project and likely carry over:

- Prefers **interactive HTML** over static explanations for learning complex concepts
- Likes **quizzes** at the end of each topic to check understanding
- Wants **concrete examples** (small numbers, real data) rather than abstract theory
- Prefers **analogies** to explain technical concepts
- Prefers **light/white background** for learning materials
- Uses **arrow keys** for navigation (keyboard-friendly)
- Wants the **"why"** before the "how" — intuition first, details second
- Asks follow-up questions when concepts don't fully land

## Design Patterns for Interactive HTMLs

When building Phase HTMLs, follow these patterns from the Fine-tuning project:

- **Single-file HTML** with embedded CSS and JS (no dependencies except Google Fonts)
- **Orbitron** for headings, **JetBrains Mono** for code, **DM Sans** for body
- **Slide-based navigation** with step dots and arrow key support
- **Quiz at bottom** of each slide with correct/wrong feedback and green highlighting
- **Fun fact box** (💡) that changes per slide
- **Equation/code boxes** with `border-left: 3px solid` accent
- **Comparison grids** (1fr 1fr) for A-vs-B topics
- **Diagrams and visualizations** for architecture concepts (pipeline DAGs, pattern diagrams)

## Suggested Skills

- `frontend-design` — For building interactive Phase HTMLs
- `senior-architect` — For system design discussions and architecture decisions
- `clean-code` — For refactoring pipeline code
- `senior-backend` — For Phase 6 enterprise pipeline work

## Repo URLs

- **Project repo:** `https://github.com/ashokmulchandani/MLOPS-End-End-Prediction-Pipeline-Ashok-1.git`
- **Plan file:** `MLOPS_SYSTEM_DESIGN_PLAN.md` (root of repo)

## Related Projects

- **Fine-Tuning Project:** `C:\Users\ashok\OneDrive\NOblox\Fine_tuning-ML-Pipleine--Synthetic_Data-Ashok-1\` — LLM fine-tuning curriculum (10 phases)
- **DevOps Projects:** `C:\Users\ashok\OneDrive\NOblox\Ashok_DEVOPS_Projects\` — Docker, K8s, CI/CD
- **CUDA Projects:** `C:\Users\ashok\OneDrive\NOblox\CUDA_Projects-Ashok\` — GPU optimization
