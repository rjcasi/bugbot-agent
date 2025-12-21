"""
Grok Adapter
------------

Wraps a Grok-style client.
"""

from typing import List, Dict, Any
from .base import BaseLLMAdapter


class GrokAdapter(BaseLLMAdapter):
    def __init__(self, client: Any, model: str = "grok-2"):
        self.client = client
        self.model = model

    def generate(self, prompt: str) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
        )
        return response.choices[0].message["content"]

    def chat(self, messages: List[Dict[str, str]]) -> str:
        response = self.client.chat.completions.create(
            model=self.model,
            messages=messages,
        )
        return response.choices[0].message["content"]

    def embed(self, text: str) -> Any:
        # Placeholder — depends on Grok's API
        return {"embedding": None, "note": "Embedding not implemented yet."}