import os
import json

from services.memory_service import MemoryService
from services.llm_service import LLMService


class SummaryService:

    SUMMARY_TRIGGER = 20


    llm_service = LLMService()

    @staticmethod
    def should_summarize(session_id: str):

        history = MemoryService.get_formatted_history(
            session_id
        )

        return len(history) >= SummaryService.SUMMARY_TRIGGER

    @staticmethod
    def generate_summary(session_id: str):

        history = MemoryService.get_formatted_history(
            session_id
        )

        summary_prompt = [
            {
                "role": "system",
                "content": """
                Summarize the following conversation.

                Focus on:
                - important user preferences
                - goals
                - personal information
                - ongoing tasks
                - important discussion topics

                Keep the summary concise and useful.
                """
            }
        ]

        summary_prompt.extend(history)

        response = SummaryService.llm_service.generate_response(
            summary_prompt
        )

        return response["response"]

    @staticmethod
    def save_summary(session_id: str, summary: str):

        path = f"storage/summaries/{session_id}.json"

        data = {
            "session_id": session_id,
            "summary": summary
        }

        with open(path, "w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False
            )

    @staticmethod
    def load_summary(session_id: str):

        path = f"storage/summaries/{session_id}.json"

        if not os.path.exists(path):
            return ""

        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)

        return data.get("summary", "")