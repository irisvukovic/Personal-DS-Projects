# Personal Projects
This repository contains projects I've worked on beyond academic coursework to explore different machine learning algorithms and approaches to data science using topics that interest me.
The goal of this repository is to experiment, learn, and apply data science and machine learning techniques in a more open, self-directed way.
Projects are listed in chronological order (newest → oldest).

| Project | Description | Tools |
|--------|------------|------|
| **Barcelona Airbnb Analysis** | Housing market analysis examining Airbnb's impact on Barcelona's housing crisis through commercial operator detection and neighborhood-level housing pressure indexing | Python, Pandas |
| **LLM-Based Medical Coding** *(In progress)* | RAG pipeline that converts unstructured clinical notes into ICD-10 codes | Python, ThauraAI API |
| **2025 US Open Predictor** | First personal project exploring XGBoost on historical ATP tennis data | Python, XGBoost |

Below are the **detailed descriptions and reflections** for each project listed above.

---
### Barcelona Airbnb Analysis

This project investigates how Airbnb activity in Barcelona may be contributing to housing displacement and pressure on the residential housing market. Using data from [Inside Airbnb](https://insideairbnb.com/get-the-data/), I analyzed listing-level and neighborhood-level patterns to identify signs of commercialization and areas of concentrated short-term rental activity.

**Findings:** Comparing total listings to unique hosts (19,410 vs. 6,620), it is clear that a few multi-property owners and companies are dominating the Airbnb market in the city. Only 17.2% of listings are actually casual, with the rest being commercial. Out of 49 neighborhoods analyzed, Poblenou area (80.9/100) is in the highest scoring HPI neighborhoods, with the average HPI being 60.5. 

**Tools:** Python, Pandas, NumPy, Scikit-learn, K-means clustering

➡️ View project: [barcelona_airbnb.ipynb](./barcelona_airbnb.ipynb)

**To do:** Extend exploration to compare Barcelona to other cities with housing displacement issues caused by Airbnb commercialization.

---

### LLM-Based Medical Coding Pipeline *(In Progress)*

Medical coding, or converting physician notes into standardized ICD-10 codes, is expensive, slow, and prone to errors when done manually. This project builds an automated pipeline to suggest ICD-10 codes from raw clinical notes using a retrieval-augmented generation (RAG) architecture.

**How it works:** Clinical notes and ICD-10 guidelines are embedded using **Bio-ClinicalBERT** and stored in **ChromaDB**. When a new note is submitted, the pipeline retrieves the 20 most semantically similar documents, reranks them to the top 10 using a cross-encoder model (ms-marco-MiniLM-L-6-v2), and passes them as context to **Thaura** via the ThauraAI API. The model returns the top-3 ICD-10 code predictions. 

**Evaluation:** Top-1 and top-3 accuracy on held-out notes. Hallucination rate comparison between RAG and GPT-only baseline. Carbon footprint tracking via CodeCarbon for local compute.

**Findings:** RAG-based architecture improved accuracy (+44%) and reduced hallucinations (-2) compared to GPT-only.

**Tools:** Python, ThauraAI API, Bio-ClinicalBERT, ChromaDB, cross-encoder reranking, CodeCarbon

➡️ View project: [med_coding_single_code.ipynb](./med_coding_single_code.ipynb)

**To do:** Power BI visual analysis.

---

### 2025 US Open Predictor

My **first personal data science project**, created to experiment with **XGBoost**, an algorithm I hadn't used before. Using historical ATP data, I built a model to predict outcomes for the 2025 US Open Men's Singles. I chose tennis because I was actively following the tournament and found an expansive, publicly available dataset on Kaggle.

**Tools:** Python, Pandas, NumPy, Scikit-learn, XGBoost  

**Results & Reflection:** My predictions were fairly accurate compared to the real outcomes. However, I realized that XGBoost may not have been the most suitable model for this task, despite its strong performance. In the future, I'd like to repeat this experiment using women's tennis data, a different modeling approach, and a dashboard-style visualization.

➡️ View project: [mensprediction.ipynb](./mensprediction.ipynb)
