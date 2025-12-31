from dataclasses import dataclass
from typing import Dict, Any
import numpy as np


@dataclass
class MetricPanelOutput:
    """
    Output container for the Metric Panel.
    """
    point: np.ndarray
    metric: np.ndarray
    inverse_metric: np.ndarray
    meta: Dict[str, Any]


class MetricPanel:
    """
    Metric Organ for BugBot-Agent.

    Responsibilities:
    - Evaluate the metric tensor g_ij(x)
    - Compute inverse metric g^{ij}(x)
    - Compute determinant, eigenvalues, signature
    - Validate positive-definiteness (if Riemannian)
    """

    def __init__(self, structure):
        """
        structure: an object with a .metric(x) -> g_ij(x) method
                   (your RiemannianStructure from structures.py)
        """
        self.structure = structure

    def evaluate_at(self, x: np.ndarray) -> MetricPanelOutput:
        """
        Evaluate the metric and diagnostics at point x.
        """
        g = self.structure.metric(x)
        g_inv = np.linalg.inv(g)

        det_g = float(np.linalg.det(g))
        eigenvalues = np.linalg.eigvalsh(g)

        meta = {
            "determinant": det_g,
            "eigenvalues": eigenvalues.tolist(),
            "positive_definite": bool((eigenvalues > 0).all()),
            "signature": self._signature(eigenvalues),
        }

        return MetricPanelOutput(
            point=x,
            metric=g,
            inverse_metric=g_inv,
            meta=meta,
        )

    @staticmethod
    def _signature(eigenvalues: np.ndarray) -> Dict[str, int]:
        """
        Count positive, negative, and zero eigenvalues.
        """
        pos = int((eigenvalues > 0).sum())
        neg = int((eigenvalues < 0).sum())
        zero = int((eigenvalues == 0).sum())
        return {"positive": pos, "negative": neg, "zero": zero}