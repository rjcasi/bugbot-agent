"""
LLM Adapter Base Interface
--------------------------

Defines a common interface for all LLM backends:
- local transformers
- cloud LLMs (ChatGPT, Grok, etc.)
- embeddings
"""

from typing import List, Any, Dict


class BaseLLMAdapter:
    """Abstract base class for all LLM adapters."""

    def generate(self, prompt: str) -> str:
        """Single-turn text generation."""
        raise NotImplementedError

    def chat(self, messages: List[Dict[str, str]]) -> str:
        """
        Multi-turn chat.

        messages: [{"role": "user"|"assistant"|"system", "content": "..."}]
        """
        raise NotImplementedError

    def embed(self, text: str) -> Any:
        """Return an embedding representation for the given text."""
        raise NotImplementedError