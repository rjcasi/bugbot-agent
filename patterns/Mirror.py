pattern_9_mirror = Pattern(
    id=9,
    name="Mirror",
    mantra="Reflection, self-observation, recursive truth.",
    essence=(
        "The pattern that reveals the difference between intention and outcome, "
        "allowing the agent to observe itself and correct drift."
    ),
    structure="REFLECT {source} :: {frame} => {delta}",
    slots={
        "source": (
            "What is being reflected: spikes, embeddings, cyber logs, "
            "effector telemetry, symbolic intention, phase-space trajectory."
        ),
        "frame": (
            "The interpretive lens: temporal, symbolic, geometric, ethical, "
            "cyber, or energy-preserving frame."
        ),
        "delta": (
            "The measured difference between reality and expectation; "
            "alignment, drift, error, anomaly score."
        )
    },
    examples=[
        {
            "description": "Reflect spike activity over the last 200ms.",
            "mirror": "REFLECT spikes :: last_200ms => drift<=0.12"
        },
        {
            "description": "Reflect cyber logs for anomalies.",
            "mirror": "REFLECT cyber_logs :: anomaly_frame => delta>0"
        },
        {
            "description": "Reflect intention vs symbolic meaning.",
            "mirror": "REFLECT intention :: symbolic_frame => alignment>=0.9"
        }
    ]
)

PATTERNS[pattern_9_mirror.id] = pattern_9_mirror


def render_mirror(source: str, frame: str, delta: str) -> str:
    """
    Render a Mirror pattern instance using the canonical structure.
    """
    return f"REFLECT {source} :: {frame} => {delta}"
