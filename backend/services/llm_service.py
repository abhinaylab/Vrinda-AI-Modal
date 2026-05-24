# backend/services/llm_service.py

class LLMService:

    def generate_response(self, prompt: str):

        return {
            "response": f"VRINDA AI received: {prompt}"
        }