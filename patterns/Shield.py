pattern_8_shield = Pattern(
    id=8,
    name="Shield",
    mantra="Protection, containment, controlled isolation.",
    essence=(
        "The pattern that establishes boundaries, prevents corruption, and "
        "maintains system integrity under stress or intrusion."
    ),
    structure="{mode} :: {region} @ {policy}",
    slots={
        "mode": (
            "Type of shielding: isolate, dampen, quarantine, filter, "
            "rate_limit, sanitize, preserve."
        ),
        "region": (
            "What is being protected: tensor block, organ, memory vector, "
            "cyber panel, effector, phase-space region."
        ),
        "policy": (
            "Rules governing the shield: non_destructive, preserve_energy, "
            "entropy<=0.4, read_only, time<=200ms, symbolic_integrity."
        )
    },
    examples=[
        {
            "description": "Quarantine a corrupted memory vector.",
            "shield": "QUARANTINE :: MEMORY_VEC_12 @ read_only"
        },
        {
            "description": "Dampen spikes in layer 3 to prevent runaway firing.",
            "shield": "DAMPEN :: LAYER_3 @ entropy<=0.4"
        },
        {
            "description": "Isolate a suspicious fuzzing pattern.",
            "shield": "ISOLATE :: CYBER_ORGAN_2 @ non_destructive"
        }
    ]
)

PATTERNS[pattern_8_shield.id] = pattern_8_shield


def render_shield(mode: str, region: str, policy: str) -> str:
    """
    Render a Shield pattern instance using the canonical structure.
    """
    return f"{mode} :: {region} @ {policy}"