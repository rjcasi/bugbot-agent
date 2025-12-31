from dataclasses import dataclass, field
from typing import List, Optional

@dataclass
class TopologyReport:
    is_connected: Optional[bool] = None
    is_path_connected: Optional[bool] = None
    is_compact: Optional[bool] = None
    is_hausdorff: Optional[bool] = None
    is_first_countable: Optional[bool] = None
    is_second_countable: Optional[bool] = None
    is_metrizable: Optional[bool] = None

    is_product_space: Optional[bool] = None
    is_quotient_space: Optional[bool] = None
    is_manifold_candidate: Optional[bool] = None

    warnings: List[str] = field(default_factory=list)
    notes: List[str] = field(default_factory=list)

    def summary(self) -> str:
        lines = [
            "Topology Report:",
            f"  Connected:        {self.is_connected}",
            f"  Path connected:   {self.is_path_connected}",
            f"  Compact:          {self.is_compact}",
            f"  Hausdorff:        {self.is_hausdorff}",
            f"  1st countable:    {self.is_first_countable}",
            f"  2nd countable:    {self.is_second_countable}",
            f"  Metrizable:       {self.is_metrizable}",
            f"  Product space:    {self.is_product_space}",
            f"  Quotient space:   {self.is_quotient_space}",
            f"  Manifold cand.:   {self.is_manifold_candidate}",
        ]
        if self.warnings:
            lines.append("Warnings:")
            lines += [f"  - {w}" for w in self.warnings]
        if self.notes:
            lines.append("Notes:")
            lines += [f"  - {n}" for n in self.notes]
        return "\n".join(lines)