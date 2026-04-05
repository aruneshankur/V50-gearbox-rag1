# Multimodal RAG System for V50 Gearbox Assembly

## 1. Problem Statement
### Domain Identification
I work as a Senior Manager at **Tata Motors, Pantnagar plant**, specifically leading the **V50 gearbox assembly shop**. My domain is automotive manufacturing and precision engineering.

### Problem Description
On the shop floor, technicians often need to access the **Intra V30/V50 Service Manuals** to find critical data like tightening torques, clearance limits, or assembly sequences. [cite_start]These documents are heavy PDFs (like the one uploaded: *OSB-INTRA V30_V50*) filled with complex engineering diagrams and multi-page tables[cite: 21]. Currently, finding a specific value requires manual scrolling, which causes delays in the assembly line.

### Why This Problem Is Unique
Generic search engines cannot "read" an exploded-view diagram of a gearbox to explain how a snap ring should be seated[cite: 22]. The data is often trapped in **fine-print footnotes** or **technical diagrams** that standard keyword searches ignore[cite: 23].

### Why RAG Is the Right Approach
Retrieval-Augmented Generation (RAG) is better than fine-tuning because the technical specs in manufacturing manuals change with new RDE (Real Driving Emissions) norms[cite: 24]. RAG ensures the AI provides a **grounded answer** with a direct reference to the specific page of the Tata Motors manual, preventing dangerous "hallucinations" of torque values[cite: 25].

### Expected Outcomes
The system will allow a user to ask: *"What is the main shaft tightening torque for the V50?"* and receive the exact value along with the relevant table and image reference[cite: 26].

---

## 2. Architecture Overview
The system follows a standard Multimodal RAG pipeline[cite: 34]:
1. **Ingestion:** Uses **Docling** to split the PDF into Text, Tables, and Images[cite: 35].
2. **Processing:** Images are sent to a **Vision Language Model (VLM)** to create text summaries[cite: 35].
3. **Storage:** All data is converted into vectors and stored in a **FAISS** vector store[cite: 35].
4. **Retrieval:** When a user queries, the system finds the most relevant chunks and generates an answer using an **LLM**[cite: 35].

---

## 3. Technology Choices
* [cite_start]**Document Parser:** **Docling** - Selected for its superior ability to handle complex PDF layouts and extract tables accurately[cite: 35, 51].
* [cite_start]**Vector Store:** **FAISS** - Chosen for its high speed and efficiency in similarity search for small to medium-sized technical manuals[cite: 35, 53].
* [cite_start]**API Framework:** **FastAPI** - Used to create high-performance, asynchronous endpoints as required by the assignment[cite: 35, 38].
* [cite_start]**Vision Model:** **Gemini/GPT-4o** - To interpret assembly diagrams and convert them into searchable text[cite: 55].

---

## 4. Setup Instructions
1. Clone the repo: `git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Set up your `.env` file with your API keys.
4. Run the server: `uvicorn main:app --reload`

---

## 5. API Documentation
* [cite_start]`GET /health`: Returns system readiness[cite: 38].
* [cite_start]`POST /ingest`: Upload a PDF for processing[cite: 38].
* [cite_start]`POST /query`: Submit a natural language question[cite: 38].
* [cite_start]`GET /docs`: Interactive Swagger UI[cite: 38].

---

## 6. Limitations & Future Work
* [cite_start]**Current Limitation:** The system may struggle with very low-resolution hand-drawn diagrams[cite: 83].
* [cite_start]**Future Work:** Integrate OCR for handwritten maintenance logs on the shop floor[cite: 83].
