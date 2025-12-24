pattern_34_root = Pattern(
    id=34,
    name="Root",
    mantra="Deep grounding, foundational recursion, origin binding.",
    essence=(
        "The pattern that connects structures back into foundational substrates, "
        "binding them to origin, memory, and stability."
    ),
    structure="ROOT {structure} into {substrate} :: {principle}",
    slots={
        "structure": (
            "The entity being grounded: symbolic_tree, spike_system, cyber_logic, "
            "effector_network, memory_fabric, phase_dynamics."
        ),
        "substrate": (
            "The foundation: meaning_substrate, energy_substrate, hardware_substrate, "
            "biological_substrate, history_substrate, phase_substrate."
        ),
        "principle": (
            "The grounding rule: origin_truth, stability, conservation, "
            "continuity, persistence, identity_binding."
        )
    },
    examples=[
        {
            "description": "Root symbolic tree into meaning substrate by origin truth.",
            "root": "ROOT symbolic_tree into meaning_substrate :: origin_truth"
        },
        {
            "description": "Root spike system into energy substrate for stability.",
            "root": "ROOT spike_system into energy_substrate :: stability"
        },
        {
            "description": "Root cyber logic into hardware substrate for grounding.",
            "root": "ROOT cyber_logic into hardware_substrate :: grounding"
        }
    ]
)

PATTERNS[pattern_34_root.id] = pattern_34_root


def render_root(structure: str, substrate: str, principle: str) -> str:
    """
    Render a Root pattern instance using the canonical structure.
    """
    return f"ROOT {structure} into {substrate} :: {principle}"