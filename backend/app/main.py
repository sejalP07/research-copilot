from fastapi import FastAPI

app = FastAPI(
    title="Research Copilot API"
)

@app.get("/")
def home():
    return {
        "status": "running"
    }