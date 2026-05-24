# backend/services/memory_service.py

class MemoryService:

    def store_memory(self, data: str):
        return {
            "stored": data
        }