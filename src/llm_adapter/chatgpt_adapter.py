"""
ChatGPT Adapter
---------------

Wraps an OpenAI-style client for ChatGPT-like models.
"""

from typing import List, Dict, Any
from .base import BaseLLMAdapter


class ChatGPTAdapter(BaseLLMAdapter):
    def __init__(self, client: Any, model: str = "gpt-5"):
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
        response = self.client.embeddings.create(
            model="text-embedding-3-large",
            input=text,
        )
        return response.data[0].embedding