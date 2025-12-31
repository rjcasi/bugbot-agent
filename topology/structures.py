from dataclasses import dataclass
from typing import Any, List, Optional, Set

@dataclass
class Basis:
    basic_sets: List[Set[Any]]

    def as_open_sets(self) -> List[Set[Any]]:
        return self.basic_sets


@dataclass
class OpenCover:
    sets: List[Set[Any]]
    target_subset: Optional[Set[Any]] = None