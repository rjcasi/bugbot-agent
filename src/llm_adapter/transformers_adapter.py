"""
Transformers Adapter
--------------------

Wraps a local Hugging Face Transformers causal LM.
"""

from typing import List, Dict, Any
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

from .base import BaseLLMAdapter


class TransformersAdapter(BaseLLMAdapter):
    def __init__(self, model_name: str = "gpt2", device: str = None):
        self.model_name = model_name
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForCausalLM.from_pretrained(model_name)

        if device is None:
            device = "cuda" if torch.cuda.is_available() else "cpu"

        self.device = device
        self.model.to(self.device)

    def generate(self, prompt: str) -> str:
        inputs = self.tokenizer(prompt, return_tensors="pt").to(self.device)
        with torch.no_grad():
            outputs = self.model.generate(
                **inputs,
                max_new_tokens=120,
                do_sample=True,
                temperature=0.8,
            )
        return self.tokenizer.decode(outputs[0], skip_special_tokens=True)

    def chat(self, messages: List[Dict[str, str]]) -> str:
        # Simple: flatten chat history into a single prompt
        prompt = ""
        for m in messages:
            role = m["role"]
            content = m["content"]
            prompt += f"{role.upper()}: {content}\n"
        prompt += "ASSISTANT:"

        return self.generate(prompt)

    def embed(self, text: str) -> Any:
        # Placeholder: you can later plug in a sentence-transformer model
        return {"embedding": None, "note": "Embedding not implemented yet."}