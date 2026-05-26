from services.memory_service import MemoryService


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

        messages = [
            {
                "role": "system",
                "content": ContextService.SYSTEM_PROMPT
            }
        ]

        messages.extend(recent_history)

        return messages