# backend/core/security.py

def verify_api_key(api_key: str):
    return api_key == "secure_key"