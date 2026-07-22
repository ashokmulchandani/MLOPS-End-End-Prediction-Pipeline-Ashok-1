# 4B.9 — The AI Testing Pyramid (10 Layers)

| # | Layer | Framework |
|---|-------|-----------|
| 10 | Production Monitoring | Evidently AI, WhyLabs |
| 9 | Human Evaluation / A-B | Manual + statistical |
| 8 | End-to-End AI Workflow | pytest + Docker |
| 7 | Prompt + Model Eval | DeepEval, Promptfoo |
| 6 | RAG / Retrieval | Ragas, TruLens |
| 5 | Embedding Regression | Custom benchmarks |
| 4 | Model Regression | MLflow, W&B |
| 3 | Prompt Regression | Promptfoo, LangSmith |
| 2 | Data Validation | Great Expectations, Pandera |
| 1 | Unit + Integration | pytest, unittest |

## Key Frameworks

- **Prompt Testing:** Promptfoo, LangSmith, Braintrust
- **LLM Evaluation:** DeepEval, Ragas, OpenAI Evals
- **RAG Testing:** Ragas, TruLens
- **Data Validation:** Great Expectations, Soda, Pandera
- **CI/CD:** GitHub Actions, GitLab CI, Jenkins
