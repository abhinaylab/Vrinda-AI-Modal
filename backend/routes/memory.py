# backend/routes/memory.py

from fastapi import APIRouter

router = APIRouter()


@router.get("/memory")
async def memory_status():
    return {
        "memory": "online"
    }