# FULL MLOps & ML SYSTEM DESIGN PROJECT PLAN OF ACTION

> Based on: ML System Design & MLOps For Beginners, Build ML Production Grade Projects, First-Ever Production-Grade AI Project
> Philosophy: Think → Build → Scale (System Design thinking first, then hands-on MLOps, then enterprise-grade architecture)

## 📊 Progress: 5/9 Modules Complete (Phases 1-4, 6G)

| # | Phase | Interactive Module | Templates |
|---|-------|--------------------|-----------|
| ✅ 1 | ML System Design Thinking | [phase1_system_design.html](phase1_system_design.html) | [10 docs](Phase_1_System_Design/) |
| ✅ 2 | Data Strategy & Engineering | [phase2_data_strategy.html](phase2_data_strategy.html) | [10 docs](Phase_2_Data_Strategy/) |
| ✅ 3 | Feature Engineering & Pipeline | [phase3_feature_engineering.html](phase3_feature_engineering.html) | [10 docs](Phase_3_Feature_Engineering/) |
| ✅ 4 | Baseline First | [phase4_baseline_first.html](phase4_baseline_first.html) | [8 docs](Phase_4_Baseline_First/) |
| ⬜ 5 | House Prices Predictor System | — | — |
| ⬜ 6 | Enterprise Training Data Pipeline | — | — |
| ✅ 6G | AI/ML Testing & QA | [phase4b_ai_testing.html](phase4b_ai_testing.html) | [10 docs](Phase_4B_AI_Testing/) |
| ⬜ 7 | Monitoring & Production Ops | — | — |
| ⬜ 8 | Capstone Project | — | — |

🏠 **Dashboard:** [index.html](index.html)

### 🎨 Visual Explainers

| Topic | Link |
|-------|------|
| Class Imbalance (2.6) — 5 techniques compared live | [class_imbalance_visualizer.html](class_imbalance_visualizer.html) |
| Train/Test Split (2.7) — which method per data type | [train_test_split_visualizer.html](train_test_split_visualizer.html) |
| Data Quality Gates (2.8) — 4-layer inspection pipeline | [data_quality_visualizer.html](data_quality_visualizer.html) |
| Label Strategy (2.3) — 6 ways to get labels | [label_strategy_visualizer.html](label_strategy_visualizer.html) |
| Feature Profiling (3.1) — histograms, correlations, missing charts | [feature_profiling_visualizer.html](feature_profiling_visualizer.html) |
| Missing Values (3.2) — WHY before HOW, 5 scenarios | [missing_values_visualizer.html](missing_values_visualizer.html) |
| Feature Monitoring (3.10) — live drift dashboard | [feature_monitoring_visualizer.html](feature_monitoring_visualizer.html) |

---

## ✅ Phase 1: ML System Design Thinking (Before You Write Code) — COMPLETE

> "Most ML projects fail at the definition stage, not the modeling stage."
> **Status:** All 10 steps complete. Interactive module: [`phase1_system_design.html`](phase1_system_design.html)
> **Deliverables:** [`Phase_1_System_Design/`](Phase_1_System_Design/) — 10 template documents

| Step | Task | Deliverable | Status |
|------|------|-------------|--------|
| 1.1 | Pick a problem — decide if it even needs ML (6-word test: Learn, Complex, Patterns, Existing data, Predictions, Unseen data) | 1-page decision doc | ✅ |
| 1.2 | Compare 3 options: Rule/heuristic vs Simple ML model vs "Not Now" (collect data first) | Comparison table with cost/risk/value | ✅ |
| 1.3 | Frame the problem precisely: "Given input X, predict Y, for user Z, at decision time T, to optimize business outcome B" | Problem framing statement | ✅ |
| 1.4 | Build the metrics ladder: Business metric → Product metric → Model metric → Feature/data quality metric | Metrics ladder diagram | ✅ |
| 1.5 | Choose 1 North Star metric + 2-3 guardrail metrics | Documented metric choices with rationale | ✅ |
| 1.6 | Anticipate failures — list 5 ways the model could fail before writing code | Failure mode analysis doc | ✅ |
| 1.7 | Define the feedback loop: Prediction → User behavior → Logging → Labels → Training data → New model | Feedback loop diagram | ✅ |
| 1.8 | Identify operational constraints: latency budget, throughput, privacy/GDPR, interpretability, cost | Constraints checklist | ✅ |
| 1.9 | Design the rollback path — what happens if model misbehaves? | Rollback plan | ✅ |
| 1.10 | Write the 1-page ML proposal (problem, value, risk, baseline, metrics, constraints) | ML proposal document | ✅ |

---

## ✅ Phase 2: Data Strategy & Engineering (Data Beats Clever Models) — COMPLETE

> "If your labels are wrong, if your sampling is biased, even the cleverest model will behave badly."
> **Status:** All 10 steps complete. Interactive module: [`phase2_data_strategy.html`](phase2_data_strategy.html)
> **Deliverables:** [`Phase_2_Data_Strategy/`](Phase_2_Data_Strategy/) — 10 template documents

| Step | Task | Deliverable | Status |
|------|------|-------------|--------|
| 2.1 | Identify data sources — where does data come from? APIs, logs, databases, scraping? | Data source inventory | ✅ |
| 2.2 | Sampling strategy — simple random vs stratified vs weighted vs reservoir | Sampling plan document | ✅ |
| 2.3 | Label strategy — hand labels vs natural labels (clicks, completions) vs weak supervision vs active learning | Labeling plan | ✅ |
| 2.4 | Define implicit negatives — "no click within X seconds = negative" (choose window length) | Implicit negative rules | ✅ |
| 2.5 | Data lineage — track source, annotator, injection date, label version for every sample | Lineage schema design | ✅ |
| 2.6 | Handle class imbalance — oversampling, undersampling, SMOTE, class weights, focal loss | Imbalance strategy + code | ✅ |
| 2.7 | Train/validation/test split — time-based, stratified, entity-based (no leakage) | Split strategy document | ✅ |
| 2.8 | Data quality checks — schema validation, range checks, null rate monitoring, drift detection | Data validation pipeline | ✅ |
| 2.9 | Build a data versioning system with DVC — track data changes like code | DVC setup + `dvc.yaml` | ✅ |
| 2.10 | Create a data changelog — "changed sampling on this date, fixed labels on that date" | Changelog file | ✅ |

---

## Phase 3: Feature Engineering & Pipeline (Features Matter More Than Algorithms)

> "Whatever transformation you apply in training MUST be applied identically in serving."

| Step | Task | Deliverable |
|------|------|-------------|
| 3.1 | Observe features — ranges, missing rates, drift over time | Feature profiling report |
| 3.2 | Handle missing values — drop, mean/median impute, constant, model-based | Imputation strategy + code |
| 3.3 | Scaling — MinMax vs StandardScaler vs RobustScaler (freeze stats from training set only) | Scaling pipeline |
| 3.4 | Binning — convert continuous to categorical (quantile bins, domain bins) | Binning logic |
| 3.5 | Categorical encoding — one-hot (small cardinality) vs top-K + unknown bucket vs hashing (high cardinality) | Encoding strategy |
| 3.6 | Feature crosses — multiply features for interactions (watch for explosion/overfitting) | Feature cross experiments |
| 3.7 | Leakage detection — ablation test (drop each feature, check if performance drops suspiciously) | Ablation test results |
| 3.8 | Build transformation pipeline — same code path for training AND serving | `sklearn.Pipeline` or custom |
| 3.9 | Version the pipeline — save scaler stats, bin edges, encoder mappings | Versioned artifacts |
| 3.10 | Monitor feature health in production — distribution shifts, null spikes, prediction distribution stability | Monitoring dashboard |

---

## Phase 4: Baseline First (Win With Simple Steps)

> "Start with something super simple. Ship it. Measure. Then add complexity only when needed."

| Step | Task | Deliverable |
|------|------|-------------|
| 4.1 | Build the simplest possible baseline — rule-based or single-feature heuristic | Baseline v0 (rules) |
| 4.2 | Measure baseline on your metrics ladder — does it move the business metric at all? | Baseline evaluation report |
| 4.3 | Build a simple ML model — logistic regression or decision tree | Baseline v1 (simple model) |
| 4.4 | Compare baseline v0 vs v1 — how much lift does ML give over rules? | Comparison table |
| 4.5 | Instrument logging from day 1 — log every prediction, input features, actual outcome | Logging infrastructure |
| 4.6 | Ship baseline to small group — A/B test or shadow mode | Deployment of baseline |
| 4.7 | Collect real-world feedback — does offline metric improvement translate to business value? | Post-launch analysis |
| 4.8 | Document: "Baseline gives X% of value. To get remaining Y%, we need Z (more data/complex model)" | Business case for next iteration |

## Phase 5: House Prices Predictor System (ZenML + MLflow — Real Project)

> "Even the simplest project idea can be in the top 1% with the right implementation."
> Reference project: `prices-predictor-system/` (Ames Housing dataset)
> This is the EXACT project that got students 50 LPA jobs.

### 5A: Project Setup & Design Patterns

| Step | Task | Deliverable |
|------|------|-------------|
| 5A.1 | Create project structure: `src/`, `steps/`, `pipelines/`, `analysis/`, `data/`, `explanations/` | Project scaffold |
| 5A.2 | Set up virtual environment + `requirements.txt` (zenml, mlflow, scikit-learn, pandas, seaborn) | Environment ready |
| 5A.3 | Initialize ZenML (`zenml init`) + register stack with MLflow tracker + MLflow deployer | Stack: `zenml stack describe` shows mlflow_tracker + mlflow_deployer |
| 5A.4 | Study & implement Factory Design Pattern — coffee machine analogy (see `explanations/factory_design_pattern.py`) | Understand: interface → concrete products → factory class |
| 5A.5 | Study & implement Strategy Design Pattern — payment gateway analogy (see `explanations/strategy_design_pattern.py`) | Understand: interface → strategies → context class |
| 5A.6 | Study & implement Template Design Pattern — restaurant cuisine analogy (see `explanations/template_design_pattern.py`) | Understand: skeleton method → abstract steps → concrete implementations |

### 5B: Data Ingestion (Factory Pattern)

| Step | Task | Deliverable |
|------|------|-------------|
| 5B.1 | Create `DataIngestor` abstract class — interface with `ingest(file_path) → DataFrame` | `src/ingest_data.py` |
| 5B.2 | Implement `ZipDataIngestor` — verify zip, extract, find CSV, return DataFrame | Concrete product |
| 5B.3 | Create `DataIngestorFactory` — static method `get_data_ingestor(file_extension)` routes to correct ingestor | Factory class |
| 5B.4 | Create ZenML step `data_ingestion_step` — uses factory, returns DataFrame | `steps/data_ingestion_step.py` |
| 5B.5 | Key learnings: type hints, docstrings, error handling (verify file type before processing), auto-detect extension | Professional code habits |

### 5C: Exploratory Data Analysis (Strategy Pattern)

| Step | Task | Deliverable |
|------|------|-------------|
| 5C.1 | Create `DataInspectionStrategy` abstract class + `DataTypesInspectionStrategy` + `SummaryStatisticsStrategy` | `analysis/analyze_src/basic_data_inspection.py` |
| 5C.2 | Create `DataInspector` context class — set_strategy() + execute_inspection() | Context class |
| 5C.3 | Run inspection — identify: 82 columns, skewed SalePrice (std dev $79K), potential outliers in LotArea | Insights documented in EDA notebook |
| 5C.4 | Create `MissingValueAnalysisTemplate` (Template Pattern) — identify + visualize missing values with heatmap | `analysis/analyze_src/missing_values_analysis.py` |
| 5C.5 | Interpret heatmap — identify columns with significant missing (Alley, PoolQC, Fence) vs moderate vs single | Missing value strategy decisions |
| 5C.6 | Create `UnivariateAnalysisStrategy` — histogram + KDE for numerical, count plot for categorical | `analysis/analyze_src/univariate_analysis.py` |
| 5C.7 | Analyze SalePrice distribution — confirm positive skew → decision: apply log transformation | Distribution insight |
| 5C.8 | Create `BivariateAnalysisStrategy` — scatter plot (numerical vs numerical), box plot (categorical vs numerical) | `analysis/analyze_src/bivariate_analysis.py` |
| 5C.9 | Analyze GrLivArea vs SalePrice — confirm linear relationship + outliers | Linearity validation |
| 5C.10 | Analyze OverallQual vs SalePrice — confirm strong positive correlation via box plot | Feature importance insight |
| 5C.11 | Create `MultivariateAnalysis` (Template Pattern) — correlation heatmap + pair plot | `analysis/analyze_src/multivariate_analysis.py` |
| 5C.12 | Interpret correlations — OverallQual (0.80), GrLivArea (0.71), TotalBsmtSF (0.63) are strongest predictors | Final EDA conclusions |
| 5C.13 | Document decisions: need log transform (skewness), need outlier handling, need encoding, multicollinearity check | Decision document |

### 5D: Processing Steps (Strategy Pattern)

| Step | Task | Deliverable |
|------|------|-------------|
| 5D.1 | Create `MissingValueHandlingStrategy` abstract + `DropMissingValues` (axis, threshold) + `FillMissingValues` (mean/median/mode/constant) | `src/handle_missing_values.py` |
| 5D.2 | Create `MissingValueHandler` context class — set_strategy() + handle_missing_values() | Context class |
| 5D.3 | Create ZenML step `handle_missing_values_step` — takes DataFrame + strategy param, returns cleaned DataFrame | `steps/handle_missing_values_step.py` |
| 5D.4 | Create `FeatureEngineeringStrategy` abstract + `LogTransformation` + `StandardScaling` + `MinMaxScaling` + `OneHotEncoding` | `src/feature_engineering.py` |
| 5D.5 | Create ZenML step `feature_engineering_step` — apply log transform to SalePrice + GrLivArea | `steps/feature_engineering_step.py` |
| 5D.6 | Create `OutlierDetectionStrategy` abstract + `ZScoreDetection` (threshold=3) + `IQRDetection` | `src/outlier_detection.py` |
| 5D.7 | Create `OutlierDetector` context — detect_outliers() + handle_outliers(method='remove'|'cap') | Context class with capping logic |
| 5D.8 | Create ZenML step `outlier_detection_step` — detect + handle outliers on SalePrice column | `steps/outlier_detection_step.py` |
| 5D.9 | Create `DataSplittingStrategy` abstract + `SimpleTrainTestSplit` (test_size=0.2) | `src/data_splitter.py` |
| 5D.10 | Create ZenML step `data_splitter_step` — returns X_train, X_test, y_train, y_test | `steps/data_splitter_step.py` |

### 5E: Model Building + MLflow Tracking

| Step | Task | Deliverable |
|------|------|-------------|
| 5E.1 | Create `ModelBuildingStrategy` abstract + `LinearRegressionStrategy` | `src/model_building.py` |
| 5E.2 | Key insight: Pipeline = StandardScaler + LinearRegression (same scaler for train AND predict) | Understand train/serve parity |
| 5E.3 | Create `model_building_step` with MLflow integration — `mlflow.sklearn.autolog()` | `steps/model_building_step.py` |
| 5E.4 | Include ColumnTransformer: numerical (SimpleImputer mean) + categorical (SimpleImputer mode + OneHotEncoder) | Preprocessing pipeline |
| 5E.5 | Register model as ZenML Model artifact (`ArtifactConfig(name="prices_predictor")`) | Model artifact tracked |
| 5E.6 | Create `ModelEvaluationStrategy` abstract + `RegressionModelEvaluationStrategy` (MSE, R2) | `src/model_evaluator.py` |
| 5E.7 | Create `model_evaluator_step` — preprocess X_test with same pipeline, then evaluate | `steps/model_evaluator_step.py` |
| 5E.8 | Run full training pipeline — verify in ZenML dashboard: ingest → missing → feature → outlier → split → train → evaluate | Pipeline DAG screenshot |
| 5E.9 | View MLflow UI (`mlflow ui`) — check logged params, metrics (MSE, R2), artifacts (model.pkl) | MLflow experiment view |
| 5E.10 | Experiment: change imputation strategy (mean → median), compare runs in MLflow | Experiment comparison |

### 5F: Deployment Pipeline + Inference

| Step | Task | Deliverable |
|------|------|-------------|
| 5F.1 | Create `continuous_deployment_pipeline` — runs training pipeline + MLflow Model Deployer step (workers=3) | `pipelines/deployment_pipeline.py` |
| 5F.2 | Create `inference_pipeline` — dynamic_importer (sample data) → prediction_service_loader → predictor | Inference pipeline |
| 5F.3 | Create `dynamic_importer` step — sample input data as JSON (columns model expects) | `steps/dynamic_importer.py` |
| 5F.4 | Create `prediction_service_loader` step — find existing MLflow deployment service by pipeline/step name | `steps/prediction_service_loader.py` |
| 5F.5 | Create `predictor` step — load model service, call `service.predict(numpy_array)` | `steps/predictor.py` |
| 5F.6 | Create `run_deployment.py` — orchestrate deploy + inference with Click CLI (--stop-service flag) | CLI deployment script |
| 5F.7 | Run deployment: `python run_deployment.py` — get prediction URL (localhost) | Model serving locally |
| 5F.8 | Create `sample_predict.py` — send POST request to prediction URL, get house price prediction | Working prediction ($280K) |
| 5F.9 | (Assignment) Create Streamlit app — input form → POST to prediction URL → display price | `app.py` |
| 5F.10 | (Assignment) Try other algorithms: Ridge, Lasso, RandomForest — compare in MLflow | Extended experiments |

---

## Phase 6: Enterprise-Grade Training Data Pipeline (Production Architecture)

> "Companies don't care what model you trained. They care if you can build a pipeline that ships training data at scale."

### 6A: Project Architecture & Init

| Step | Task | Deliverable |
|------|------|-------------|
| 6A.1 | Design project structure — `__init__.py` as reception desk (public API), `bot.py` as factory manager | Project scaffold |
| 6A.2 | Create Pydantic data models — Document, TextChunk, TrainingExample, Dataset, QualityReport, TaskTemplate | `models.py` |
| 6A.3 | Define enums — DocumentType (PDF/TXT/URL/CSV), TaskType (QA/Classification/Summarization), QualityMetric | Enums in models |
| 6A.4 | Create base entity class — UUID, created_at, updated_at, metadata | BaseEntity model |
| 6A.5 | Set up logging system — custom logger with structured output | `logger.py` |
| 6A.6 | Set up error handling — custom `TrainingDataBotError` exception hierarchy | `errors.py` |
| 6A.7 | Create settings/config — API keys, chunk sizes, quality thresholds from `.env` | `config.py` + `.env.example` |

### 6B: Document Loading Highway (Unified Loader)

| Step | Task | Deliverable |
|------|------|-------------|
| 6B.1 | Create abstract `BaseLoader` — `load_single()`, `load_multiple()`, `load_stream()` | `base.py` |
| 6B.2 | Implement `DocumentLoader` — handles TXT, MD, JSON, CSV, HTML | `documents.py` |
| 6B.3 | Implement `PDFLoader` — extract text from PDFs (PyPDF2/pdfplumber) | `pdf.py` |
| 6B.4 | Implement `WebLoader` — scrape URLs with Decodo API + fallback to BeautifulSoup | `web.py` |
| 6B.5 | Implement `UnifiedLoader` — auto-detect file type, route to correct specialist loader | `unified.py` |
| 6B.6 | Add parallel loading — `asyncio.gather()` for multiple documents simultaneously | Async loading |
| 6B.7 | Test: load PDF + TXT + URL in one call — verify all return Document objects | Integration test |

### 6C: Text Processing Pipeline

| Step | Task | Deliverable |
|------|------|-------------|
| 6C.1 | Text cleaning — remove excessive whitespace, short lines, special characters | `preprocessor.py` |
| 6C.2 | Smart chunking — split documents into chunks with configurable size (default 1000 tokens) | Chunking algorithm |
| 6C.3 | Overlap strategy — 200-token overlap between chunks for context preservation | Overlap implementation |
| 6C.4 | Token counting — track token count per chunk for cost estimation | Token counter |
| 6C.5 | Output as TextChunk objects — document_id, content, chunk_index, start/end index, context | Structured chunks |

### 6D: Task Management & AI Generation

| Step | Task | Deliverable |
|------|------|-------------|
| 6D.1 | Create `TaskManager` — routes tasks to correct generator based on TaskType | `manager.py` |
| 6D.2 | Create task templates — prompt + description + parameters for each task type | Default templates |
| 6D.3 | Implement `QAGenerator` — takes chunk → generates Q&A pairs via AI | `qa_generator.py` |
| 6D.4 | Implement `ClassificationGenerator` — takes chunk → generates labeled examples | `classification_generator.py` |
| 6D.5 | Implement `SummarizationGenerator` — takes chunk → generates summary pairs | `summarization_generator.py` |
| 6D.6 | Create `AIClient` — connects to OpenAI/Anthropic, manages prompts, tracks costs | `client.py` |
| 6D.7 | Add cost tracking — tokens used, cost per example, total spend | Cost monitoring |
| 6D.8 | Add retry logic + rate limiting — handle API failures gracefully | Resilient API calls |

### 6E: Quality Evaluation & Export

| Step | Task | Deliverable |
|------|------|-------------|
| 6E.1 | Create `QualityEvaluator` — check toxicity, bias, diversity, coherence, relevance | `evaluator.py` |
| 6E.2 | Quality scoring — overall score from weighted sub-metrics | Scoring algorithm |
| 6E.3 | Quality gate — auto-reject examples below threshold | Filter logic |
| 6E.4 | Generate quality report — per-example and aggregate statistics | QualityReport objects |
| 6E.5 | Create `DatasetExporter` — export to JSON, CSV, Parquet formats | `exporter.py` |
| 6E.6 | Add metadata to exports — source, quality scores, generation params | Rich metadata |
| 6E.7 | HuggingFace format export — ready for `datasets.load_dataset()` | HF-compatible output |

### 6F: CLI + Dashboard + Orchestration

| Step | Task | Deliverable |
|------|------|-------------|
| 6F.1 | Create CLI interface — `tdb process --source ./docs --task qa --format json` | `cli.py` (Click) |
| 6F.2 | Create Streamlit dashboard — 4 tabs: Dashboard, Documents, Generate, Analytics | `app.py` |
| 6F.3 | Dashboard: real-time stats — documents loaded, examples generated, quality scores, costs | Live metrics |
| 6F.4 | Create the "one-click magic" method — `bot.quick_process(sources, tasks, output)` | Convenience method |
| 6F.5 | Add async context manager — auto-cleanup on exit (`async with bot:`) | Resource management |
| 6F.6 | End-to-end test: URL → load → chunk → generate QA → evaluate → export JSON | Full pipeline test |

---

## ✅ Phase 6G: AI/ML Testing & Quality Assurance — COMPLETE

> "I review like I'm the person getting paged at 3am when this breaks."
> **Status:** All 10 steps complete. Interactive module: [`phase4b_ai_testing.html`](phase4b_ai_testing.html)
> **Deliverables:** [`Phase_4B_AI_Testing/`](Phase_4B_AI_Testing/) — 10 template documents + [runnable practice tests](Phase_4B_AI_Testing/test_practice/)

| Step | Task | Deliverable | Status |
|------|------|-------------|--------|
| 6G.1 | Why testing AI is different — non-deterministic, data-as-code, degrades over time | 3 differences document | ✅ |
| 6G.2 | 3-Pass PR Review — Works? → Readable? → Safe? | PR review checklist | ✅ |
| 6G.3 | Test Cases: Happy Path, Edge Cases, Failure Modes | Test template with examples | ✅ |
| 6G.4 | AI Testing 4 Layers: Data → Model → Pipeline → Production | Layer overview document | ✅ |
| 6G.5 | Layer 1: Data Testing — schema validation, ranges, nulls | Pandera/Pydantic code | ✅ |
| 6G.6 | Layer 2: Model Testing — behavioral, invariance, directional | pytest model tests | ✅ |
| 6G.7 | Layer 3: Pipeline Testing — E2E, error paths, retries | Pipeline test code | ✅ |
| 6G.8 | Layer 4: Production Monitoring — drift, nulls, predictions | Evidently AI code | ✅ |
| 6G.9 | AI Testing Pyramid — 10 layers from unit to production | Pyramid reference | ✅ |
| 6G.10 | MLOps CI/CD Pipeline + Framework Cheat Sheet | CI/CD flow + tools table | ✅ |

> 🧪 **Practice code:** 5 runnable test files in [`Phase_4B_AI_Testing/test_practice/`](Phase_4B_AI_Testing/test_practice/):
> - `test_data_quality.py` — schema, ranges, leakage (Layer 1)
> - `test_model_behavior.py` — shape, NaN, directional, stability (Layer 2)
> - `test_pipeline_e2e.py` — E2E flow, error paths, retry (Layer 3)
> - `monitor_drift.py` — PSI drift detection (Layer 4)
> - `test_enterprise_pipeline.py` — Unit tests for Phase 6 loaders, chunkers, generators, evaluators, exporters

---

## Phase 7: Monitoring, Retraining & Production Operations

> "Shipping the model is the middle, not the end. The real game is how you maintain and refresh."

| Step | Task | Deliverable |
|------|------|-------------|
| 7.1 | Set up model monitoring — track prediction distribution, feature drift, null rates | Monitoring pipeline |
| 7.2 | Define alert thresholds — if drift score > X, or recall drops below Y, or business KPI drops Z% | Alert rules |
| 7.3 | Implement drift detection — statistical tests (KS test, PSI) on input features | Drift detector |
| 7.4 | Build retraining trigger — automatic retrain when drift detected or performance degrades | Retrain pipeline |
| 7.5 | Shadow deployment — run new model alongside old, compare predictions before switching | Shadow mode |
| 7.6 | Canary deployment — route 5% traffic to new model, monitor, then gradually increase | Canary strategy |
| 7.7 | A/B testing framework — hypothesis, primary metric, duration, sample size calculation | A/B test plan |
| 7.8 | Build model registry — version models, track lineage (which data + code produced which model) | Model registry |
| 7.9 | Dead letter queue — failed predictions logged for investigation | DLQ implementation |
| 7.10 | Incident response playbook — "model accuracy dropped 10%, here's what to do" | Runbook document |

---

## Phase 8: Full End-to-End Project (Capstone — Combine Everything)

> Pick ONE real problem and apply all phases end-to-end.

### Suggested Project: Customer Churn Prediction System

| Step | Task | Deliverable |
|------|------|-------------|
| 8.1 | System Design doc — problem framing, metrics ladder, constraints, failure modes | Design document |
| 8.2 | Data pipeline — ingest from SQL, sample, label, version with DVC | Data pipeline |
| 8.3 | Feature engineering — build transformation pipeline (train + serve parity) | Feature pipeline |
| 8.4 | Baseline — rule-based (no login > 30 days = high risk) + logistic regression | Baseline models |
| 8.5 | Advanced model — XGBoost/LightGBM with hyperparameter tuning | Tuned model |
| 8.6 | ZenML pipeline — ingest → clean → feature → train → evaluate → deploy | Full MLOps pipeline |
| 8.7 | MLflow tracking — all experiments logged, best model registered | Experiment history |
| 8.8 | Deployment — MLflow serving + Streamlit app for business users | Deployed system |
| 8.9 | Monitoring — drift detection, performance alerts, retraining triggers | Monitoring dashboard |
| 8.10 | Documentation — README, architecture diagram, runbook, metrics report | Production-ready docs |

---

## ⚡ RECOMMENDED PATH: Project-First Approach (Phase 5 as the Vehicle)

> **Jump straight into Phase 5 (Prices Predictor)** — learn Phase 1-4 concepts
> IN CONTEXT as they naturally arise during the project.
> Come back to Phase 6 later as a stretch goal.
> **Phase 5 alone gives you the "50 LPA job" project ready.**
>
> ### Why Project-First?
> - Phase 1-4 are thinking/documents — you learn them BETTER when applied to a real problem
> - Every EDA decision in Phase 5 IS Phase 1-4 in action
> - You'll understand the INTUITION because you're seeing it work on real data
> - You can VISUALISE each concept (plots, dashboards, pipeline DAGs) instead of just reading about it
>
> ### How Phase 1-4 Concepts Are Married Into Phase 5:
>
> | Phase 5 Step | Phase 1-4 Concept You're Learning | Intuition / Visualisation |
> |---|---|---|
> | 5C.3: Inspect data (82 cols, skewed SalePrice) | **Phase 1.1**: Does this need ML? Yes — complex patterns, 82 features, can't write rules | You SEE the complexity in the data shape |
> | 5C.7: SalePrice histogram shows positive skew | **Phase 1.4**: Metrics ladder — offline metric (MSE) must connect to business (accurate pricing) | You SEE the skew in the histogram, understand WHY log transform is needed |
> | 5C.12: Correlation heatmap (OverallQual=0.80) | **Phase 1.5**: North Star metric — R2 score + guardrails (no overfitting) | You SEE which features matter in the heatmap colors |
> | 5C.13: "Need outlier handling, log transform" | **Phase 1.6**: Anticipate failures — model will fail on outliers if not handled | You SEE outliers as dots outside the scatter plot cluster |
> | 5D.1-5D.3: Handle missing values (drop/fill) | **Phase 2.1-2.5**: Data strategy — where is data missing? Random or structured? | You SEE yellow bands in the missing value heatmap |
> | 5D.4-5D.5: Log transformation on SalePrice | **Phase 3.3-3.4**: Feature engineering — scaling, transformation for algorithm assumptions | You SEE the distribution change from skewed → normal after transform |
> | 5D.6-5D.8: Z-score outlier detection | **Phase 3.7**: Leakage detection / ablation — remove suspicious data points | You SEE outliers disappear from scatter plot after handling |
> | 5D.9-5D.10: Train/test split (80/20) | **Phase 2.7**: Splits — no leakage, stratified, representative | You SEE the split in ZenML dashboard as separate artifacts |
> | 5E.1-5E.2: LinearRegression (simplest model) | **Phase 4.1-4.3**: Baseline first — start simple, measure, then add complexity | You SEE the baseline MSE/R2 in MLflow as your benchmark |
> | 5E.9-5E.10: Compare runs in MLflow | **Phase 4.4-4.7**: Compare baseline vs iterations — does complexity help? | You SEE side-by-side metrics in MLflow UI |
> | 5F.1-5F.7: Deploy model, get prediction URL | **Phase 1.8-1.9**: Operational constraints + rollback path | You SEE the model serving at localhost, can stop/restart |
> | Phase 7: Add drift detection | **Phase 1.7**: Feedback loop — monitor, detect drift, retrain | You SEE alerts when input distribution changes |
>
> ### The Rule:
> **At every step in Phase 5, PAUSE and ask: "Which Phase 1-4 concept am I applying here? WHY am I doing this? What would go WRONG if I skipped it?"**
> Document these answers in your EDA notebook as markdown cells — this becomes your interview talking points.
>
> ---
>
> - **Project-first path = 7-8 sessions, ~25-30 hours**
> - At 3 sessions/week → **~3 weeks** to have a complete MLOps portfolio deployed
> - Phase 6 (Enterprise Pipeline) = stretch goal, add 6 more sessions later
> - Phase 7 (Monitoring) = add 1 more session after project is deployed
>
> **Note:** Deployment infrastructure (Docker/K8s/CI-CD) and system design patterns
> (cache, queue, circuit breaker) are already covered in the DevOps Hackathon Plan.
> Model optimization/serving (TensorRT/Triton) is already in the CUDA Plan.
> This MLOps plan focuses on what's UNIQUE: ML thinking, data strategy, feature pipelines,
> experiment tracking, and design patterns in Python code.

---

## Execution Order (Project-First Approach)

> Phase 1-4 concepts are learned IN CONTEXT during Phase 5 steps.
> At every step, you understand the intuition + visualise the result.

| Session | What to Complete | Phase 1-4 Concepts Covered | Time |
|---------|-----------------|---------------------------|------|
| Session 1 | Phase 5A: Setup + 3 Design Patterns (Factory, Strategy, Template) | — (coding foundations) | 2-3 hrs |
| Session 2 | Phase 5B: Data Ingestion (Factory Pattern) | Phase 1.1 (does it need ML?), Phase 2.1 (data sources) | 3-4 hrs |
| Session 3 | Phase 5C.1–5C.7: EDA Part 1 (inspection, missing values, univariate) | Phase 1.4-1.6 (metrics, failures), Phase 2.4-2.5 (lineage, quality) | 4-5 hrs |
| Session 4 | Phase 5C.8–5C.13: EDA Part 2 (bivariate, multivariate, conclusions) | Phase 1.7-1.8 (feedback loop, constraints), Phase 3.1 (feature profiling) | 3-4 hrs |
| Session 5 | Phase 5D: Processing Steps (missing values, features, outliers, split) | Phase 2.6-2.7 (imbalance, splits), Phase 3.2-3.7 (all feature engineering) | 4-5 hrs |
| Session 6 | Phase 5E: Model Building + MLflow Tracking | Phase 4.1-4.7 (baseline first, measure, compare) | 3-4 hrs |
| Session 7 | Phase 5F: Deployment + Inference + sample_predict | Phase 1.8-1.9 (constraints, rollback), Phase 4.8 (ship it) | 3-4 hrs |
| Session 8 | Phase 7: Monitoring, drift detection, retraining triggers | Phase 1.7 (feedback loop), Phase 2.8 (data validation) | 3-4 hrs |
| **✅ DONE** | **Full project deployed + all Phase 1-4 concepts understood in context** | **All of Phase 1-4 covered** | **~28-33 hrs** |
| --- | --- | --- | --- |
| *STRETCH* | *Phase 6A-6F (Enterprise Training Data Pipeline)* | *Advanced architecture* | *21-27 hrs* |
| *STRETCH* | *Phase 8 (Capstone — Churn Prediction end-to-end)* | *Apply independently* | *8-10 hrs* |
| Session 13 | Phase 5F: Steps 5F.1–5F.10 (deployment pipeline + inference + sample_predict) | 3-4 hrs | MLOps |
| Session 14 | Phase 7: Steps 7.1–7.5 (monitoring, drift, retraining) | 3-4 hrs | Production |
| **✅ DONE** | **Phase 1-5 + 7 complete — portfolio ready, project deployed** | **~50 hrs** | **✅** |

> ⚠️ **NOTE: The above 14-session table is the ORIGINAL sequential path (if you prefer theory-first).**
> **The RECOMMENDED project-first path above (8 sessions, ~28-33 hrs) covers the same content faster.**
> Choose whichever suits your learning style.

| --- | --- | --- | --- |
| *STRETCH* | *Phase 6A-6F (Enterprise Training Data Pipeline)* | *21-27 hrs* | *Later* |
| *STRETCH* | *Phase 8 (Capstone — Churn Prediction end-to-end)* | *8-10 hrs* | *Later* |

---

## Tools & Technologies

| Category | Tools |
|----------|-------|
| ML Pipeline Orchestration | ZenML, Airflow (optional) |
| Experiment Tracking | MLflow |
| Data Versioning | DVC |
| Model Serving | MLflow Serving, FastAPI |
| Monitoring | Evidently AI, Great Expectations, custom dashboards |
| Feature Store | Feast (optional) |
| Web Scraping | Decodo API, BeautifulSoup, httpx |
| AI/LLM | OpenAI API, Azure OpenAI |
| Data Validation | Pydantic, Great Expectations |
| Dashboard | Streamlit |
| CLI | Click |
| Async | asyncio, httpx (async) |
| Design Patterns | Strategy, Factory, Abstract Base Class |
| Deployment | Docker, AWS EC2, FastAPI |
| CI/CD | GitHub Actions |
| Database | PostgreSQL, SQLite (local) |
| Cloud Storage | AWS S3, GCS |
| Python | pandas, scikit-learn, numpy |

---

## Key Design Patterns Used Throughout

| Pattern | Where Used | Why |
|---------|-----------|-----|
| Strategy Pattern | Data cleaning (preprocess vs divide), Model selection, Evaluation metrics | Swap algorithms without changing calling code |
| Factory Pattern | Unified Loader (auto-detect file type → create correct loader) | Create objects without specifying exact class |
| Abstract Base Class | BaseLoader, BaseModel, BaseEvaluation | Enforce consistent interface across implementations |
| Pipeline Pattern | ZenML steps chained together | Reproducible, cacheable, trackable workflows |
| Observer Pattern | Monitoring alerts (drift detected → trigger retrain) | Decouple detection from action |
| Decorator Pattern | ZenML `@step`, `@pipeline` | Add behavior without modifying function |

---

## Project Structure

```
MLOPS_System_Design_Thinking/
├── MLOPS_SYSTEM_DESIGN_PLAN.md          # This file
├── ML System Design & MLOps For Beginners.txt
├── Build ML Production Grade Projects.txt
├── First-Ever Production-Grade AI Project.txt
├── phase1_system_design/
│   ├── problem_framing_template.md
│   ├── metrics_ladder_template.md
│   ├── ml_proposal_template.md
│   └── failure_mode_analysis.md
├── phase2_data_strategy/
│   ├── sampling_experiments.ipynb
│   ├── labeling_strategy.md
│   ├── data_validation_pipeline.py
│   └── dvc.yaml
├── phase3_features/
│   ├── feature_profiling.ipynb
│   ├── transformation_pipeline.py
│   ├── leakage_detection.ipynb
│   └── feature_monitoring.py
├── phase4_baseline/
│   ├── rule_baseline.py
│   ├── simple_model_baseline.py
│   └── baseline_comparison.md
├── phase5_mlops_pipeline/
│   ├── src/
│   │   ├── data_cleaning.py
│   │   ├── model_dev.py
│   │   └── evaluation.py
│   ├── steps/
│   │   ├── ingest_data.py
│   │   ├── clean_data.py
│   │   ├── model_train.py
│   │   └── evaluation.py
│   ├── pipelines/
│   │   ├── training_pipeline.py
│   │   └── deployment_pipeline.py
│   ├── config.py
│   ├── run_pipeline.py
│   ├── run_deployment.py
│   └── app.py (Streamlit)
├── phase6_enterprise_pipeline/
│   ├── training_data_robot/
│   │   ├── __init__.py
│   │   ├── bot.py
│   │   ├── core/
│   │   │   ├── models.py
│   │   │   ├── config.py
│   │   │   ├── logger.py
│   │   │   └── errors.py
│   │   ├── sources/
│   │   │   ├── __init__.py
│   │   │   ├── base.py
│   │   │   ├── unified.py
│   │   │   ├── documents.py
│   │   │   ├── pdf.py
│   │   │   └── web.py
│   │   ├── processing/
│   │   │   └── preprocessor.py
│   │   ├── tasks/
│   │   │   ├── manager.py
│   │   │   ├── qa_generator.py
│   │   │   ├── classification_generator.py
│   │   │   └── summarization_generator.py
│   │   ├── ai/
│   │   │   ├── __init__.py
│   │   │   └── client.py
│   │   ├── evaluation/
│   │   │   └── evaluator.py
│   │   ├── export/
│   │   │   └── exporter.py
│   │   └── cli/
│   │       └── __init__.py
│   ├── dashboard/
│   │   └── app.py
│   ├── .env.example
│   └── README.md
├── phase7_monitoring/
│   ├── drift_detector.py
│   ├── alert_rules.yaml
│   ├── retrain_trigger.py
│   └── runbook.md
├── phase8_capstone/
│   ├── design_doc.md
│   ├── src/
│   ├── pipelines/
│   ├── monitoring/
│   └── README.md
└── requirements.txt
```

---

## Prerequisites

| Requirement | How to Check |
|-------------|--------------|
| Python 3.9+ | `python --version` |
| pip | `pip --version` |
| Git | `git --version` |
| Virtual environment | `python -m venv .venv` |
| ZenML | `pip install zenml[server]` → `zenml version` |
| MLflow | `pip install mlflow` → `mlflow --version` |
| DVC | `pip install dvc` → `dvc version` |
| Streamlit | `pip install streamlit` → `streamlit --version` |
| OpenAI API key (Phase 6) | Set in `.env` file |

---

## Key Principles (From All 3 Transcripts)

1. **Say NO to ML when it's not needed** — rules, database queries, simple processes can be better
2. **Data > Model** — fix data before trying fancier algorithms
3. **Start simple, ship fast** — baseline first, then iterate
4. **Same pipeline for training AND serving** — no train/serve skew
5. **Version everything** — data, features, models, configs
6. **Monitor everything** — drift, performance, cost, latency
7. **Design for failure** — rollback paths, fallbacks, graceful degradation
8. **Document decisions** — why you chose this metric, this threshold, this architecture
9. **Think in systems, not models** — the model is 20%, the system is 80%
10. **Feedback loops are gold** — prediction → behavior → label → retrain

---

## Estimated Total Time

| Path | Sessions | Hours | Timeline (3/week) |
|------|----------|-------|-------------------|
| **⚡ Project-First (RECOMMENDED)** | **8 sessions** | **~28-33 hrs** | **~3 weeks** |
| Sequential (Phase 1-5 + 7 separately) | 14 sessions | ~40-50 hrs | ~5 weeks |
| Full plan (+ Phase 6 + 8) | 22 sessions | ~75-90 hrs | ~8 weeks |

> **Project-first approach:** You learn Phase 1-4 concepts WHILE building the project.
> At every step you PAUSE, understand the intuition, and VISUALISE the result.
> By session 8, you have: the full MLOps pipeline deployed + all concepts understood in context — ready for interviews.
