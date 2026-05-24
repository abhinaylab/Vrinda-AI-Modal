# backend/routes/voice.py

from fastapi import APIRouter

router = APIRouter()


@router.get("/voice")
async def voice_status():
    return {
        "voice": "active"
    }