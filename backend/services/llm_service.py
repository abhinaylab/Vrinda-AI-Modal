import requests


class LLMService:

    def generate_response(self, messages):

        url = "http://localhost:11434/api/chat"

        payload = {
            "model": "llama3",
            "messages": messages,
            "stream": False
        }

        response = requests.post(
            url,
            json=payload
        )

        data = response.json()

        return {
            "response": data["message"]["content"]
        }