from dataclasses import dataclass
from typing import Dict, Any

from bugbot_agent.topology.space import TopologicalSpace
from bugbot_agent.topology.detectors import (
    is_connected,
    connected_components,
    is_hausdorff,
)
from bugbot_agent.topology.structures import (
    is_second_countable,
    is_locally_euclidean,
)
from bugbot_agent.topology.report import TopologyReport


@dataclass
class TopologyPanelOutput:
    summary: Dict[str, Any]
    report: str


class TopologyPanel:
    """
    Cockpit UI wrapper around your existing topology logic.
    """

    def __init__(self, space: TopologicalSpace):
        self.space = space

    def analyze(self) -> TopologyPanelOutput:
        connected = is_connected(self.space)
        components = connected_components(self.space)
        hausdorff = is_hausdorff(self.space)
        second_countable = is_second_countable(self.space)
        locally_euclidean = is_locally_euclidean(self.space)

        manifold_candidate = (
            hausdorff and second_countable and locally_euclidean
        )

        summary = {
            "connected": connected,
            "components": components,
            "hausdorff": hausdorff,
            "second_countable": second_countable,
            "locally_euclidean": locally_euclidean,
            "manifold_candidate": manifold_candidate,
        }

        report = TopologyReport(summary).render()

        return TopologyPanelOutput(summary=summary, report=report)