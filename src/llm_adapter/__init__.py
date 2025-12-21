"""
LLM Adapter Unified Hub
-----------------------

Provides a single entrypoint to construct different LLM backends
by name. This is the "cortex organ" selector for BugBotAgent.
"""

from typing import Optional, Any

from .base import BaseLLMAdapter
from .transformers_adapter import TransformersAdapter
from .chatgpt_adapter import ChatGPTAdapter
from .grok_adapter import GrokAdapter


def create_llm_adapter(
    backend: str,
    client: Optional[Any] = None,
    model_name: Optional[str] = None,
) -> BaseLLMAdapter:
    """
    Construct an LLM adapter by backend name.

    backend: "transformers" | "chatgpt" | "grok"
    client:  API client for cloud backends (ChatGPT/Grok)
    model_name: optional model identifier
    """
    backend = backend.lower()

    if backend == "transformers":
        return TransformersAdapter(model_name=model_name or "gpt2")

    if backend == "chatgpt":
        if client is None:
            raise ValueError("ChatGPT backend requires a client.")
        return ChatGPTAdapter(client=client, model=model_name or "gpt-5")

    if backend == "grok":
        if client is None:
            raise ValueError("Grok backend requires a client.")
        return GrokAdapter(client=client, model=model_name or "grok-2")

    raise ValueError(f"Unknown LLM backend: {backend}")