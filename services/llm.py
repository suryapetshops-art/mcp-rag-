"""Minimal LLM client interface for this repo.

Purpose
- Provide a single place to integrate an external LLM provider (OpenAI, Anthropic, etc.).
- Keep provider-specific code out of `app.py` so the UI stays lightweight and testable.

Usage
- Read `API_KEY` from environment or pass the key directly to `LLMClient`.
- Replace the `generate` stub with a real provider request.
"""

from typing import Optional
import os


class LLMClient:
    def __init__(self, api_key: Optional[str] = None):
        """Create a client using an API key (or read from env var `API_KEY`).

        Raises:
            ValueError: if no API key is found.
        """
        self.api_key = api_key or os.getenv("API_KEY")
        if not self.api_key:
            raise ValueError("API key not found. Set API_KEY env var or pass it to LLMClient.")

    def generate(self, prompt: str, max_tokens: int = 256) -> str:
        """Return a text response for `prompt`.

        This is currently a stub. Replace the implementation with an HTTP request
        to your LLM provider (use `requests` or a provider SDK).
        """
        # TODO: implement provider call (example: OpenAI, Anthropic)
        # For now return a lightweight mock response so callers can be tested.
        return f"(mock response) Prompt received: {prompt[:120]}"


# Example usage (do not run in production):
# client = LLMClient()
# resp = client.generate("Hello world")
# print(resp)
