# MLOps & ML System Design — Hands-On Learning

An end-to-end MLOps and ML System Design learning project built from scratch following production-grade principles.

## What This Repo Covers

| Phase | Topic | Status |
|-------|-------|--------|
| Phase 1 | ML System Design Thinking (problem framing, metrics, constraints) | ✅ Theory complete |
| Phase 2 | Data Strategy & Engineering (sampling, labeling, versioning) | ✅ Theory complete |
| Phase 3 | Feature Engineering & Pipeline (scaling, encoding, leakage detection) | 📖 Plan ready |
| Phase 4 | Baseline First (rules → simple model → measure → iterate) | 📖 Plan ready |
| Phase 5 | **House Prices Predictor System** (ZenML + MLflow + Design Patterns) | ✅ Reference code |
| Phase 6 | Enterprise Training Data Pipeline (async, AI generation, quality eval) | 📖 Plan ready |
| Phase 7 | Monitoring & Production Ops (drift, retraining, A/B testing) | 📖 Plan ready |
| Phase 8 | Capstone Project (end-to-end from design to deployment) | 📖 Plan ready |

## Key Project: Prices Predictor System (Phase 5)

A house price prediction system that demonstrates:
- **Design Patterns**: Factory (data ingestion), Strategy (analysis, processing, models), Template (EDA)
- **Thorough EDA**: Not just plots — storyline-driven decisions for modeling
- **MLOps Pipeline**: ZenML orchestration with steps for ingest → clean → feature engineer → outlier detect → split → train → evaluate
- **Experiment Tracking**: MLflow autolog — compare runs, track metrics/params/artifacts
- **Continuous Deployment**: MLflow Model Deployer — auto-deploy if model improves
- **Inference**: Prediction service URL for real-time predictions

## Tech Stack

| Category | Tools |
|----------|-------|
| ML Pipeline | ZenML |
| Experiment Tracking | MLflow |
| Data Versioning | DVC |
| Model Serving | MLflow Serving |
| Dashboard | Streamlit |
| Design Patterns | Factory, Strategy, Template |
| ML | scikit-learn (LinearRegression, Pipeline, ColumnTransformer) |
| Data | pandas, numpy, seaborn, matplotlib |

## Project Structure

```
MLOPS_System_Design_Thinking/
├── MLOPS_SYSTEM_DESIGN_PLAN.md      # Full learning plan (22 sessions)
├── README.md                         # This file
├── CLAUDE.md                         # Guidance for Claude Code
├── HANDOFF.md                        # Session handoff document
├── .gitignore
├── LICENSE
├── Phase_1_System_Design/           # ML System Design Thinking
├── Phase_2_Data_Strategy/           # Data Strategy & Engineering
├── Phase_3_Feature_Engineering/     # Feature Engineering & Pipeline
├── Phase_4_Baseline_First/          # Baseline First
├── Phase_5_House_Prices_Predictor/  # House Prices Predictor (ZenML + MLflow)
├── Phase_6_Enterprise_Pipeline/     # Enterprise Training Data Pipeline
├── Phase_7_Monitoring_Ops/          # Monitoring & Production Ops
├── Phase_8_Capstone/                # Capstone Project
├── notebooks/                        # Shared Jupyter notebooks
├── prices-predictor-system/          # Phase 5 reference project
│   ├── analysis/                     # EDA with strategy pattern
│   ├── src/                          # Core logic (design patterns)
│   ├── steps/                        # ZenML steps
│   ├── pipelines/                    # Training + deployment pipelines
│   ├── run_pipeline.py
│   ├── run_deployment.py
│   └── sample_predict.py
└── Transcripts (learning reference)
    ├── ML System Design & MLOps For Beginners.txt
    ├── Build ML Production Grade Projects For Free.txt
    ├── First-Ever Production-Grade AI Project.txt
    ├── This AI PROJECT Got My Student 50 LPA Job.txt
    └── End To End Deep Learning Project Using MLOPS DVC Pipeline.txt
```

## How to Use This Repo

1. Read `MLOPS_SYSTEM_DESIGN_PLAN.md` — the full 22-session plan
2. Follow phases sequentially (Think → Build → Scale)
3. Phase 5 has a complete reference project in `prices-predictor-system/`
4. Each session produces a tangible deliverable
5. Total estimated time: ~75-90 hours

## Learning Sources

- [ML System Design & MLOps For Beginners](https://youtu.be/ruA_EYARCNg) — System design thinking
- [Build ML Production Grade Projects](https://www.youtube.com/watch?v=dPmH3G9NQtY) — ZenML + MLflow basics
- [First-Ever Production-Grade AI Project](https://www.youtube.com/watch?v=7Q1rkgYh6ms) — Enterprise architecture
- [This AI PROJECT Got My Student 50 LPA Job](https://www.youtube.com/watch?v=8UwhoPOO9I0) — Prices predictor system

## Setup

```bash
# Clone
git clone https://github.com/ashokmulchandani/MLOPS-End-End-Prediction-Pipeline-Ashok-1.git
cd MLOPS-End-End-Prediction-Pipeline-Ashok-1

# Virtual environment
python -m venv .venv
.venv\Scripts\activate  # Windows

# Install
pip install zenml[server] mlflow scikit-learn pandas numpy seaborn matplotlib streamlit dvc

# Initialize ZenML
zenml init
zenml integration install mlflow
zenml experiment-tracker register mlflow_tracker --flavor=mlflow
zenml model-deployer register mlflow_deployer --flavor=mlflow
zenml stack register mlops_stack -o default -a default -e mlflow_tracker -d mlflow_deployer --set
```

## License

Private — learning project.
