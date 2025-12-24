pattern_10_flow = Pattern(
    id=10,
    name="Flow",
    mantra="Continuity, motion, unbroken transformation.",
    essence=(
        "The pattern that carries state, meaning, and energy forward without "
        "breaking identity or coherence."
    ),
    structure="FLOW {stream} -> {path} :: {continuity}",
    slots={
        "stream": (
            "What is moving: spikes, embeddings, cyber signals, phase-space "
            "trajectories, symbolic meaning, effector motion."
        ),
        "path": (
            "The route or topology: gradient path, cyclic orbit, shortest path, "
            "energy-preserving path, anomaly-avoiding path."
        ),
        "continuity": (
            "The rule that must remain unbroken: preserve_energy, "
            "alignment>=0.8, avoid_entropy>0.6, maintain_phase."
        )
    },
    examples=[
        {
            "description": "Flow spike energy along a gradient path.",
            "flow": "FLOW spikes -> gradient_path :: preserve_energy"
        },
        {
            "description": "Flow embeddings through a cyclic orbit.",
            "flow": "FLOW embeddings -> cyclic_orbit :: alignment>=0.8"
        },
        {
            "description": "Flow cyber signals through a safe route.",
            "flow": "FLOW cyber_signal -> safe_route :: avoid_entropy>0.6"
        }
    ]
)

PATTERNS[pattern_10_flow.id] = pattern_10_flow


def render_flow(stream: str, path: str, continuity: str) -> str:
    """
    Render a Flow pattern instance using the canonical structure.
    """
    return f"FLOW {stream} -> {path} :: {continuity}"