pattern_31_veil = Pattern(
    id=31,
    name="Veil",
    mantra="Obscuration, hidden layers, protected meaning.",
    essence=(
        "The pattern that hides content behind layers, enabling privacy, "
        "mystery, and controlled revelation."
    ),
    structure="VEIL {content} behind {layer} :: {rule}",
    slots={
        "content": (
            "The hidden element: symbolic_truth, cyber_signal, memory_trace, "
            "phase_pattern, effector_intent, anomaly_signature."
        ),
        "layer": (
            "The obscuring layer: soft_layer, obfuscation_layer, shadow_layer, "
            "encryption_layer, symbolic_fog, cyber_shroud."
        ),
        "rule": (
            "The reveal policy: partial_reveal, anomaly_mask, selective_access, "
            "reveal_on_trust, reveal_on_resonance, never_reveal."
        )
    },
    examples=[
        {
            "description": "Veil symbolic truth behind a soft layer, partially revealed.",
            "veil": "VEIL symbolic_truth behind soft_layer :: partial_reveal"
        },
        {
            "description": "Veil a cyber signal behind an obfuscation layer to mask anomalies.",
            "veil": "VEIL cyber_signal behind obfuscation_layer :: anomaly_mask"
        },
        {
            "description": "Veil a memory trace behind a shadow layer with selective access.",
            "veil": "VEIL memory_trace behind shadow_layer :: selective_access"
        }
    ]
)

PATTERNS[pattern_31_veil.id] = pattern_31_veil


def render_veil(content: str, layer: str, rule: str) -> str:
    """
    Render a Veil pattern instance using the canonical structure.
    """
    return f"VEIL {content} behind {layer} :: {rule}"