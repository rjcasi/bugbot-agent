pattern_29_flux = Pattern(
    id=29,
    name="Flux",
    mantra="Continuous transformation, dynamic equilibrium, adaptive flow.",
    essence=(
        "The pattern that maintains continuous transformation and adaptive balance, "
        "allowing the organism to evolve moment by moment."
    ),
    structure="FLUX {state} under {force} -> {adjustment}",
    slots={
        "state": (
            "The current condition: spike_state, symbolic_state, cyber_state, "
            "effector_state, memory_state, phase_state."
        ),
        "force": (
            "The influence: drift, tension, energy_flow, entropy_shift, "
            "symbolic_pressure, cyber_load."
        ),
        "adjustment": (
            "The adaptive response: rebalancing, modulation, smoothing, "
            "redistribution, compensation, recalibration."
        )
    },
    examples=[
        {
            "description": "Flux spike state under drift.",
            "flux": "FLUX spike_state under drift -> modulation"
        },
        {
            "description": "Flux symbolic state under tension.",
            "flux": "FLUX symbolic_state under tension -> rebalancing"
        },
        {
            "description": "Flux cyber state under load.",
            "flux": "FLUX cyber_state under load -> redistribution"
        }
    ]
)

PATTERNS[pattern_29_flux.id] = pattern_29_flux


def render_flux(state: str, force: str, adjustment: str) -> str:
    """
    Render a Flux pattern instance using the canonical structure.
    """
    return f"FLUX {state} under {force} -> {adjustment}"