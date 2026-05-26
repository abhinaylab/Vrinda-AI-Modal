import json
import os

from schemas.memory_schema import ConversationMemory

BASE_DIR = "storage/conversations"


class MemoryService:

    @staticmethod
    def get_memory_path(session_id: str) -> str:
        return f"{BASE_DIR}/{session_id}.json"

    @staticmethod
    def load_conversation(session_id: str):

        path = MemoryService.get_memory_path(session_id)

        if not os.path.exists(path):
            return ConversationMemory(
                session_id=session_id,
                messages=[]
            )

        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)

        return ConversationMemory(**data)

    @staticmethod
    def save_conversation(conversation: ConversationMemory):

        path = MemoryService.get_memory_path(
            conversation.session_id
        )

        with open(path, "w", encoding="utf-8") as file:
            json.dump(
                conversation.model_dump(),
                file,
                indent=4,
                ensure_ascii=False
            )

    @staticmethod
    def add_message(
        session_id: str,
        role: str,
        content: str
    ):

        conversation = MemoryService.load_conversation(
            session_id
        )

        conversation.messages.append({
            "role": role,
            "content": content
        })

        MemoryService.save_conversation(conversation)

    @staticmethod
    def get_formatted_history(session_id: str):

        conversation = MemoryService.load_conversation(
            session_id
        )

        history = []

        for msg in conversation.messages:
            history.append({
                "role": msg.role,
                "content": msg.content
            })

        return history