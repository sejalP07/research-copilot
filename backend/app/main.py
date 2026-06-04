from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from app.services.ai_service import generate_answer
from app.routers.document import router as document_router

app = FastAPI(title="Research Copilot")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(document_router)

class ResearchRequest(BaseModel):
    question: str

@app.get("/")
async def root():
    return {"message": "Research Copilot API Running"}

@app.post("/research")
async def research(req: ResearchRequest):
    result = generate_answer(req.question)

    return {
        "answer": result["answer"],
        "sources": result["sources"],
        "confidence": 0.95,
    }