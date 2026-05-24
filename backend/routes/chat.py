# backend/routes/chat.py

from fastapi import APIRouter
from services.llm_service import LLMService

router = APIRouter()

llm_service = LLMService()


@router.post("/chat")
async def chat(message: str):
    response = llm_service.generate_response(message)

    return response