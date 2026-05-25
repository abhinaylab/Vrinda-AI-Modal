
from pydantic import BaseModel


class AgentTaskRequest(BaseModel):
    task: str


class AgentTaskResponse(BaseModel):
    result: str