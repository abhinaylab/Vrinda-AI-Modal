

from pydantic import BaseModel


class VoiceRequest(BaseModel):
    audio_path: str


class VoiceResponse(BaseModel):
    transcription: str