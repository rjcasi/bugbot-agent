from dataclasses import dataclass
import numpy as np
from typing import Dict, Any

from bugbot_agent.geometry.structures import RiemannianStructure


@dataclass
class CurvaturePanelOutput:
    point: np.ndarray
    christoffel: np.ndarray
    riemann: np.ndarray
    ricci: np.ndarray
    scalar: float
    meta: Dict[str, Any]


class CurvaturePanel:
    """
    Curvature Organ for BugBot-Agent.
    Computes:
      - Christoffel symbols
      - Riemann curvature tensor
      - Ricci tensor
      - Scalar curvature
    """

    def __init__(self, structure: RiemannianStructure):
        self.structure = structure

    def evaluate_at(self, x: np.ndarray) -> CurvaturePanelOutput:
        g = self.structure.metric(x)
        g_inv = np.linalg.inv(g)
        partials = self._metric_partials(x)

        gamma = self._christoffel(g, g_inv, partials)
        riemann = self._riemann(gamma)
        ricci = np.einsum("likj->ij", riemann)
        scalar = float(np.einsum("ij,ij->", g_inv, ricci))

        return CurvaturePanelOutput(
            point=x,
            christoffel=gamma,
            riemann=riemann,
            ricci=ricci,
            scalar=scalar,
            meta={"note": "numerical approximation"},
        )

    def _metric_partials(self, x, eps=1e-4):
        dim = len(x)
        g0 = self.structure.metric(x)
        out = np.zeros((dim, dim, dim))
        for k in range(dim):
            x2 = x.copy()
            x2[k] += eps
            out[k] = (self.structure.metric(x2) - g0) / eps
        return out

    def _christoffel(self, g, g_inv, partials):
        n = g.shape[0]
        gamma = np.zeros((n, n, n))
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    s = 0.0
                    for l in range(n):
                        s += g_inv[k, l] * (
                            partials[i, j, l]
                            + partials[j, i, l]
                            - partials[l, i, j]
                        )
                    gamma[k, i, j] = 0.5 * s
        return gamma

    def _riemann(self, gamma):
        n = gamma.shape[0]
        R = np.zeros((n, n, n, n))
        for l in range(n):
            for i in range(n):
                for j in range(n):
                    for k in range(n):
                        s = 0.0
                        for m in range(n):
                            s += (
                                gamma[l, j, m] * gamma[m, i, k]
                                - gamma[l, i, m] * gamma[m, j, k]
                            )
                        R[l, i, j, k] = s
        return R