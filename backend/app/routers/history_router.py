from fastapi import APIRouter

from app.services.history_service import (
    get_research_history
)

router = APIRouter()


@router.get("/history")
def history():

    return get_research_history()