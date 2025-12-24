pattern_22_bloom = Pattern(
    id=22,
    name="Bloom",
    mantra="Expansion, proliferation, generative growth.",
    essence=(
        "The pattern that expands seeds into proliferating structures, enabling "
        "growth, generativity, and controlled complexity."
    ),
    structure="BLOOM {seed} via {growth_rule} into {field}",
    slots={
        "seed": (
            "The initial element: symbolic_seed, spike_pattern, cyber_signature, "
            "effector_idea, memory_fragment, phase_kernel."
        ),
        "growth_rule": (
            "The expansion logic: recursive, branching, harmonic, exponential, "
            "fractal, diffusion."
        ),
        "field": (
            "The domain of proliferation: meaning_field, spike_field, cyber_field, "
            "effector_field, memory_field, phase_field."
        )
    },
    examples=[
        {
            "description": "Bloom a symbolic seed into the meaning field.",
            "bloom": "BLOOM symbolic_seed via recursive into meaning_field"
        },
        {
            "description": "Bloom a spike pattern harmonically.",
            "bloom": "BLOOM spike_pattern via harmonic into spike_field"
        },
        {
            "description": "Bloom a cyber signature into the cyber field.",
            "bloom": "BLOOM cyber_signature via branching into cyber_field"
        }
    ]
)

PATTERNS[pattern_22_bloom.id] = pattern_22_bloom


def render_bloom(seed: str, growth_rule: str, field: str) -> str:
    """
    Render a Bloom pattern instance using the canonical structure.
    """
    return f"BLOOM {seed} via {growth_rule} into {field}"