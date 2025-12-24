
from dataclasses import dataclass, field
from typing import List, Dict, Any

@dataclass
class Pattern:
    id: int
    name: str
    mantra: str
    essence: str
    structure: str
    slots: Dict[str, str]
    examples: List[Dict[str, Any]] = field(default_factory=list)


pattern_7_command = Pattern(
    id=7,
    name="Command",
    mantra="Decisive action, directional force, unambiguous intent.",
    essence=(
        "The moment an agent stops perceiving and starts shaping; "
        "transitions awareness into actuation through clear directives."
    ),
    structure="{directive} :: {target} @ {constraint}",
    slots={
        "directive": "Compressed intention; an atomic verb-like action (e.g., SCAN_PORTS, FIRE_SPIKE).",
        "target": "Locus of change; organ, panel, tensor region, effector, memory segment.",
        "constraint": "Guardrail on time, space, energy, ethics, or symbolic invariants."
    },
    examples=[
        {
            "description": "Fire a spike in layer 2 for 50ms.",
            "command": "FIRE_SPIKE :: LAYER_2 @ 50ms"
        },
        {
            "description": "Rotate phase space while preserving energy.",
            "command": "ROTATE_FIELD :: PHASE_SPACE @ preserve_energy"
        },
        {
            "description": "Deploy non-destructive cyber shield.",
            "command": "DEPLOY_SHIELD :: CYBER_ORGAN_3 @ non_destructive"
        }
    ]
)


# Optional: registry for all patterns

PATTERNS: Dict[int, Pattern] = {
    pattern_7_command.id: pattern_7_command,
    # pattern_1, pattern_2, ... can be added here
}


def render_command(
    directive: str,
    target: str,
    constraint: str
) -> str:
    """
    Render a Command pattern instance using the canonical structure.
    """
    return f"{directive} :: {target} @ {constraint}"


# Example usage:
if __name__ == "__main__":
    cmd = render_command("GENERATE_FUZZ", "RED_TEAM_PANEL", "entropy<=0.7")
    print(cmd)
    # -> GENERATE_FUZZ :: RED_TEAM_PANEL @ entropy<=0.7