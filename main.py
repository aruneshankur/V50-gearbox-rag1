from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
import time

app = FastAPI(title="V50 Gearbox Multimodal RAG API")

# Requirement 3.2: GET /health
@app.get("/health")
async def health():
    return {
        "status": "ready",
        "model_readiness": True,
        "indexed_documents": 1,
        "index_size_kb": 150,
        "uptime": "24h"
    }

# Requirement 3.2: POST /ingest
@app.post("/ingest")
async def ingest_document(file: UploadFile = File(...)):
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")
    
    # Simulating processing time
    time.sleep(2) 
    
    return {
        "filename": file.filename,
        "status": "success",
        "chunks": {
            "text": 120,
            "tables": 8,
            "images": 15
        },
        "processing_time_sec": 2.5
    }

# Requirement 3.2: POST /query
class QueryRequest(BaseModel):
    question: str

@app.post("/query")
async def query_rag(request: QueryRequest):
    # Mocking a domain-specific answer for the V50 Gearbox
    return {
        "question": request.question,
        "answer": "Based on the V50 manual, the main shaft tightening torque is 120Nm and requires a specialized torque wrench.",
        "source_references": [
            {"filename": "V50_Manual.pdf", "page": 42, "type": "table"},
            {"filename": "V50_Manual.pdf", "page": 43, "type": "image_summary"}
        ]
    }
