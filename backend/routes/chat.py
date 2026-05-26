from fastapi import APIRouter

from schemas.chat_schema import (
    ChatRequest,
    ChatResponse
)

from services.llm_service import LLMService
from services.memory_service import MemoryService
from services.context_service import ContextService

router = APIRouter()

llm_service = LLMService()


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):

    # Save user message
    MemoryService.add_message(
        session_id=request.session_id,
        role="user",
        content=request.message
    )

    # Build smart context
    context = ContextService.build_context(
        request.session_id
    )

    # Generate AI response
    response = llm_service.generate_response(
        context
    )

    # Save AI response
    MemoryService.add_message(
        session_id=request.session_id,
        role="assistant",
        content=response["response"]
    )

    # Return response
    return ChatResponse(
        response=response["response"]
    )