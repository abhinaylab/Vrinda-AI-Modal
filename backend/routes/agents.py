# backend/routes/agents.py

from fastapi import APIRouter

router = APIRouter()


@router.get("/agents")
async def agents_status():
    return {
        "agents": "running"
    }