# Personal Projects
This repository contains projects I've worked on beyond academic coursework to explore different machine learning algorithms and approaches to data science using topics that interest me.
The goal of this repository is to experiment, learn, and apply data science and machine learning techniques in a more open, self-directed way.
Projects are listed in chronological order (newest → oldest).

| Project | Description | Tools |
|--------|------------|------|
| **LLM-Based Medical Coding** *(In progress)* | RAG pipeline that converts unstructured clinical notes into ICD-10 codes using GPT-3.5 Turbo and Bio-ClinicalBERT | Python, OpenAI API |
| **2025 US Open Predictor** | First personal project exploring XGBoost on historical ATP tennis data | Python, XGBoost |

Below are the **detailed descriptions and reflections** for each project listed above.

---

### LLM-Based Medical Coding Pipeline *(In Progress)*

Medical coding, or converting physician notes into standardized ICD-10 codes, is expensive, slow, and prone to errors when done manually. This project builds an automated pipeline to suggest ICD-10 codes from raw clinical notes using a retrieval-augmented generation (RAG) architecture.

**How it works:** Clinical notes and ICD-10 guidelines are embedded using **Bio-ClinicalBERT** and stored in **ChromaDB**. When a new note is submitted, the pipeline retrieves the 20 most semantically similar documents, reranks them to the top 10 using a cross-encoder model (ms-marco-MiniLM-L-6-v2), and passes them as context to **GPT-3.5 Turbo** via the OpenAI API. The model returns the top-5 ICD-10 code predictions. A rule-based fallback (KNN-style) handles cases where LLM output cannot be parsed.

**Knowledge base:** Synthetically generated clinical notes were used instead of real MIMIC-IV records to avoid potential data-use agreement violations with third-party APIs. 25 ICD-10 codes × 30 synthetic notes each.

**Evaluation:** Top-1 and top-5 accuracy on held-out notes. Hallucination rate comparison between RAG and GPT-only baseline. Carbon footprint tracking via CodeCarbon for local compute.

**Current findings:** RAG currently shows higher hallucination rates than the GPT-only baseline, which is an unexpected result I'm actively investigating. My working hypothesis is that retrieval noise from semantically overlapping synthetic notes is introducing misleading context. 

**Tools:** Python, OpenAI API (GPT-3.5 Turbo), Bio-ClinicalBERT, ChromaDB, cross-encoder reranking, CodeCarbon

➡️ View project: [mensprediction.ipynb](./mensprediction.ipynb)

**Next steps:**
- Diagnose and resolve elevated hallucination rate
- Expand to multi-code prediction (primary + secondary diagnoses)
- Build a Power BI visualization for evaluation metrics

---

### 2025 US Open Predictor

My **first personal data science project**, created to experiment with **XGBoost**, an algorithm I hadn't used before. Using historical ATP data, I built a model to predict outcomes for the 2025 US Open Men's Singles. I chose tennis because I was actively following the tournament and found an expansive, publicly available dataset on Kaggle.

**Tools:** Python, Pandas, NumPy, Scikit-learn, XGBoost  

**Results & Reflection:** My predictions were fairly accurate compared to the real outcomes. However, I realized that XGBoost may not have been the most suitable model for this task, despite its strong performance. In the future, I'd like to repeat this experiment using women's tennis data, a different modeling approach, and a dashboard-style visualization.

➡️ View project: [mensprediction.ipynb](./mensprediction.ipynb)
