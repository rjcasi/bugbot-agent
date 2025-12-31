from dataclasses import dataclass, field
from typing import Any, Callable, Dict, List, Optional, Set
from .report import TopologyReport
from .structures import OpenCover
from . import detectors

@dataclass
class TopologicalSpace:
    points: Set[Any]
    open_sets: List[Set[Any]]
    neighbors: Dict[Any, Set[Any]] = field(default_factory=dict)
    metric: Optional[Callable[[Any, Any], float]] = None

    is_product_space: bool = False
    is_quotient_space: bool = False
    locally_euclidean: Optional[bool] = None

    def analyze(self, covers: Optional[List[OpenCover]] = None) -> TopologyReport:
        report = TopologyReport()

        report.is_connected = detectors.is_connected(self.points, self.open_sets)
        report.is_path_connected = detectors.is_path_connected(self.points, self.neighbors)
        report.is_hausdorff = detectors.is_hausdorff(self.points, self.open_sets)
        report.is_compact = detectors.is_compact(self.points, covers)

        report.is_first_countable = True if self.metric else None
        report.is_second_countable = True if len(self.points) < float("inf") else None
        report.is_metrizable = self.metric is not None

        report.is_product_space = self.is_product_space
        report.is_quotient_space = self.is_quotient_space

        if self.locally_euclidean is not None:
            if report.is_hausdorff and report.is_second_countable and self.locally_euclidean:
                report.is_manifold_candidate = True
            else:
                report.is_manifold_candidate = False

        return report