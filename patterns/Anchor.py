pattern_13_anchor = Pattern(
    id=13,
    name="Anchor",
    mantra="Grounding, stability, fixed points.",
    essence=(
        "The pattern that maintains invariants, stabilizes identity, and "
        "prevents drift across cycles and transformations."
    ),
    structure="ANCHOR {reference} in {domain} :: {constraint}",
    slots={
        "reference": (
            "The stable point: baseline embedding, spike homeostasis, "
            "symbolic invariant, cyber integrity baseline, neutral pose."
        ),
        "domain": (
            "Where the anchor applies: memory, cyber panel, tensor region, "
            "effector system, symbolic layer, phase-space manifold."
        ),
        "constraint": (
            "The rule that must remain true: drift<=0.05, alignment>=0.9, "
            "entropy<=0.4, preserve_energy, maintain_integrity."
        )
    },
    examples=[
        {
            "description": "Anchor baseline embedding to prevent drift.",
            "anchor": "ANCHOR baseline_embedding in memory :: drift<=0.05"
        },
        {
            "description": "Anchor spike homeostasis in layer 2.",
            "anchor": "ANCHOR spike_rate_homeostasis in layer_2 :: entropy<=0.4"
        },
        {
            "description": "Anchor symbolic invariant in meaning core.",
            "anchor": "ANCHOR symbolic_invariant in meaning_core :: alignment>=0.9"
        }
    ]
)

PATTERNS[pattern_13_anchor.id] = pattern_13_anchor


def render_anchor(reference: str, domain: str, constraint: str) -> str:
    """
    Render an Anchor pattern instance using the canonical structure.
    """
    return f"ANCHOR {reference} in {domain} :: {constraint}"