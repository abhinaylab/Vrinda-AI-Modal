from services.memory_service import MemoryService
from services.summary_service import SummaryService


class ContextService:

    MAX_HISTORY = 10

    SYSTEM_PROMPT = """
    You are VRINDA AI,
    a futuristic advanced AI assistant inspired by JARVIS.

    Your personality traits:
    - intelligent
    - helpful
    - futuristic
    - concise
    - professional

    Always provide clear and smart responses.
    """

    @staticmethod
    def build_context(session_id: str):

        history = MemoryService.get_formatted_history(
            session_id
        )

        recent_history = history[-ContextService.MAX_HISTORY:]

        summary = SummaryService.load_summary(
            session_id
        )

        messages = [
            {
                "role": "system",
                "content": ContextService.SYSTEM_PROMPT
            }
        ]

        # Inject long-term summary memory
        if summary:
            messages.append(
                {
                    "role": "system",
                    "content": f"""
                    Previous conversation summary:

                    {summary}
                    """
                }
            )

        # Add recent conversation history
        messages.extend(recent_history)

        return messages