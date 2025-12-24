pattern_15_spark = Pattern(
    id=15,
    name="Spark",
    mantra="Ignition, emergence, spontaneous activation.",
    essence=(
        "The pattern that transforms triggers into emergent behavior, "
        "activating new pathways and generating novel responses."
    ),
    structure="SPARK {trigger} via {catalyst} => {emergence}",
    slots={
        "trigger": (
            "What initiates ignition: anomaly spike, symbolic tension, "
            "threshold crossing, energy surplus, phase compression."
        ),
        "catalyst": (
            "The mechanism of amplification: resonance, positive feedback, "
            "symbolic amplification, energy release, cross-modal excitation."
        ),
        "emergence": (
            "The new behavior or structure: new_pathway, emergent_action, "
            "spontaneous_defense, novel_embedding, new_attractor."
        )
    },
    examples=[
        {
            "description": "Spark a defense from an anomaly spike.",
            "spark": "SPARK anomaly_spike via resonance => emergent_defense"
        },
        {
            "description": "Spark a new pathway from symbolic tension.",
            "spark": "SPARK symbolic_tension via amplification => new_pathway"
        },
        {
            "description": "Spark spontaneous action from energy surplus.",
            "spark": "SPARK energy_surplus via phase_release => spontaneous_action"
        }
    ]
)

PATTERNS[pattern_15_spark.id] = pattern_15_spark


def render_spark(trigger: str, catalyst: str, emergence: str) -> str:
    """
    Render a Spark pattern instance using the canonical structure.
    """
    return f"SPARK {trigger} via {catalyst} => {emergence}"