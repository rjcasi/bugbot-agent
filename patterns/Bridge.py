pattern_17_bridge = Pattern(
    id=17,
    name="Bridge",
    mantra="Translation, connection, cross-domain mapping.",
    essence=(
        "The pattern that connects domains, translating signals and meaning "
        "across organs, modalities, and representational spaces."
    ),
    structure="BRIDGE {source_domain} -> {target_domain} via {mapping}",
    slots={
        "source_domain": (
            "Where the signal originates: symbolic_layer, cyber_panel, spike_tensor, "
            "effector_system, phase_space, memory_core."
        ),
        "target_domain": (
            "Where the signal is mapped: robotics_layer, meaning_core, anomaly_detector, "
            "embedding_space, cyber_defense, phase_orbit."
        ),
        "mapping": (
            "How translation occurs: projection, alignment, normalization, "
            "symbolic_translation, cross_modal_mapping, energy_preserving_transform."
        )
    },
    examples=[
        {
            "description": "Bridge symbolic meaning into cyber defense.",
            "bridge": "BRIDGE symbolic_layer -> cyber_panel via projection"
        },
        {
            "description": "Bridge spikes into embedding space.",
            "bridge": "BRIDGE spike_tensor -> embedding_space via normalization"
        },
        {
            "description": "Bridge cyber logs into symbolic meaning.",
            "bridge": "BRIDGE cyber_logs -> meaning_core via symbolic_translation"
        }
    ]
)

PATTERNS[pattern_17_bridge.id] = pattern_17_bridge


def render_bridge(source_domain: str, target_domain: str, mapping: str) -> str:
    """
    Render a Bridge pattern instance using the canonical structure.
    """
    return f"BRIDGE {source_domain} -> {target_domain} via {mapping}"