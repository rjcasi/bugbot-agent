pattern_30_anchorfield = Pattern(
    id=30,
    name="Anchorfield",
    mantra="Global stabilizing attractor grids.",
    essence=(
        "The pattern that establishes distributed attractors across the system, "
        "creating global coherence and stabilizing identity."
    ),
    structure="ANCHORFIELD {anchors} via {field_rule} over {region}",
    slots={
        "anchors": (
            "The stabilizing points: meaning_anchors, spike_anchors, cyber_anchors, "
            "effector_anchors, memory_anchors, phase_anchors."
        ),
        "field_rule": (
            "The influence principle: inverse_distance, harmonic_pull, symbolic_gravity, "
            "energy_gradient, phase_alignment, coherence_force."
        ),
        "region": (
            "The domain: meaning_region, spike_region, cyber_region, effector_region, "
            "memory_region, phase_region."
        )
    },
    examples=[
        {
            "description": "Stabilize meaning with symbolic gravity.",
            "anchorfield": "ANCHORFIELD meaning_anchors via symbolic_gravity over meaning_region"
        },
        {
            "description": "Stabilize spikes with harmonic pull.",
            "anchorfield": "ANCHORFIELD spike_anchors via harmonic_pull over spike_region"
        },
        {
            "description": "Stabilize cyber behavior with coherence force.",
            "anchorfield": "ANCHORFIELD cyber_anchors via coherence_force over cyber_region"
        }
    ]
)

PATTERNS[pattern_30_anchorfield.id] = pattern_30_anchorfield


def render_anchorfield(anchors: str, field_rule: str, region: str) -> str:
    """
    Render an Anchorfield pattern instance using the canonical structure.
    """
    return f"ANCHORFIELD {anchors} via {field_rule} over {region}"