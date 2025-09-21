"""
Small helpers, left intentionally minimal so Copilot can extend as needed.
"""
from pathlib import Path

def safe_name(name: str) -> str:
    # sanitize small things (placeholder for future sanitization)
    return name.strip()
