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
    return {
        "answer": f"You asked: {req.question}",
        "confidence": 0.95
    }