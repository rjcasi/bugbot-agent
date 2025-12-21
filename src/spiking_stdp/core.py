"""
STDP Spiking Neuron Module
--------------------------

Implements a simple Spike-Timing-Dependent Plasticity (STDP) layer.
This is the "adaptive learning organ" of the BugBotAgent.

Key ideas:
- Spikes occur when activation crosses a threshold.
- STDP strengthens or weakens connections based on timing.
- This module is intentionally lightweight and interpretable.
"""

import numpy as np
from typing import Dict, Any


class STDPSpikingLayer:
    def __init__(self, dim: int = 32, threshold: float = 0.5, lr: float = 0.01):
        self.dim = dim
        self.threshold = threshold
        self.lr = lr

        # Synaptic weights
        self.weights = np.random.randn(dim, dim) * 0.01

        # Last spike times
        self.last_spike = np.zeros(dim)

        # Internal time counter
        self.t = 0

    def _spike(self, vector: np.ndarray) -> np.ndarray:
        """Generate spikes based on threshold."""
        return (vector > self.threshold).astype(float)

    def update(self, encoded: Dict[str, Any]) -> Dict[str, Any]:
        """Apply STDP learning rule."""
        vec = encoded["vector"]
        spikes = self._spike(vec)

        for i in range(self.dim):
            for j in range(self.dim):
                if spikes[i] and spikes[j]:
                    dt = self.last_spike[j] - self.last_spike[i]

                    if dt > 0:
                        self.weights[i, j] += self.lr * np.exp(-dt)
                    else:
                        self.weights[i, j] -= self.lr * np.exp(dt)

        # Update spike times
        for i in range(self.dim):
            if spikes[i]:
                self.last_spike[i] = self.t

        self.t += 1

        return {
            "spikes": spikes,
            "weights": self.weights,
            "time": self.t,
        }