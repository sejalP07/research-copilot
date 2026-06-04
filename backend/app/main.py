from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Research Copilot")

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ResearchRequest(BaseModel):
    question: str

@app.get("/")
async def root():
    return {"message": "Research Copilot API Running"}

@app.post("/research")
async def research(req: ResearchRequest):
    from app.services.ai_service import generate_answer

    answer = generate_answer(req.question)

    return {
        "answer": answer,
        "confidence": 0.95
    }