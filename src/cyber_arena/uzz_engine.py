"""
Cyber Arena Fuzz Engine
-----------------------

This module simulates fuzzing patterns and evaluates how the agent
responds to anomalies. It acts as the "immune system organ."
"""

import random
from typing import Dict, Any


class CyberFuzzEngine:
    def __init__(self):
        self.patterns = [
            "AAAAA",
            "%%%%%",
            "<script>",
            "../",
            "' OR 1=1 --",
            "🧨 fuzz spike",
        ]

    def generate(self) -> str:
        """Generate a random fuzz pattern."""
        return random.choice(self.patterns)

    def evaluate(self, encoded: Dict[str, Any]) -> Dict[str, Any]:
        """Detect anomalies based on symbolic tokens."""
        tokens = encoded.get("tokens", [])
        anomaly = any(t in self.patterns for t in tokens)

        return {
            "anomaly_detected": anomaly,
            "tokens": tokens,
            "response": "blocked" if anomaly else "clean",
        }