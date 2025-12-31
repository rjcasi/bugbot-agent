from typing import Any, Dict, List, Optional, Set
from .structures import OpenCover

# -------------------------------
# Connectedness
# -------------------------------
def is_connected(points: Set[Any], open_sets: List[Set[Any]]) -> bool:
    closed_sets = [points - U for U in open_sets]
    clopen = [U for U in open_sets if U in closed_sets]
    return len(clopen) <= 2 and set() in clopen and points in clopen


# -------------------------------
# Path connectedness (graph-based)
# -------------------------------
def is_path_connected(points: Set[Any], neighbors: Dict[Any, Set[Any]]) -> Optional[bool]:
    if not neighbors:
        return None
    if not points:
        return True

    start = next(iter(points))
    visited = dfs(start, neighbors)
    return visited == points


def dfs(start: Any, neighbors: Dict[Any, Set[Any]]) -> Set[Any]:
    stack = [start]
    visited = set()
    while stack:
        p = stack.pop()
        if p in visited:
            continue
        visited.add(p)
        for q in neighbors.get(p, set()):
            if q not in visited:
                stack.append(q)
    return visited


# -------------------------------
# Hausdorff
# -------------------------------
def is_hausdorff(points: Set[Any], open_sets: List[Set[Any]]) -> bool:
    pts = list(points)
    n = len(pts)
    for i in range(n):
        for j in range(i + 1, n):
            if not separable(pts[i], pts[j], open_sets):
                return False
    return True


def separable(x: Any, y: Any, open_sets: List[Set[Any]]) -> bool:
    containing_x = [U for U in open_sets if x in U]
    containing_y = [V for V in open_sets if y in V]
    for U in containing_x:
        for V in containing_y:
            if U.isdisjoint(V):
                return True
    return False


# -------------------------------
# Compactness
# -------------------------------
def is_compact(points: Set[Any], covers: Optional[List[OpenCover]]) -> Optional[bool]:
    if covers is None:
        return True  # finite-space heuristic
    for cover in covers:
        if not has_finite_subcover(points, cover):
            return False
    return True


def has_finite_subcover(points: Set[Any], cover: OpenCover) -> bool:
    target = cover.target_subset or points
    remaining = set(target)
    open_sets = cover.sets
    while remaining:
        best = max(open_sets, key=lambda U: len(remaining & U), default=None)
        if not best or not (remaining & best):
            return False
        remaining -= best
    return True