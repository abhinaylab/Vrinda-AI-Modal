# backend/main.py

from fastapi import FastAPI
from routes.health import router as health_router
from routes.chat import router as chat_router
from routes.voice import router as voice_router
from routes.memory import router as memory_router
from routes.agents import router as agents_router

app = FastAPI(
    title="VRINDA AI",
    description="Futuristic AI Operating System",
    version="1.0.0"
)

# Register Routes
app.include_router(health_router)
app.include_router(chat_router)
app.include_router(voice_router)
app.include_router(memory_router)
app.include_router(agents_router)


@app.get("/")
async def root():
    return {
        "message": "VRINDA AI Backend Online"
    }