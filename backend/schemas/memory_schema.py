

from pydantic import BaseModel


class MemoryRequest(BaseModel):
    content: str


class MemoryResponse(BaseModel):
    status: str