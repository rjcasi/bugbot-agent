pattern_12_echo = Pattern(
    id=12,
    name="Echo",
    mantra="Resonance, recurrence, temporal memory.",
    essence=(
        "The pattern that repeats or returns signals across time, creating "
        "temporal structure, memory, and rhythmic reinforcement."
    ),
    structure="ECHO {signal} @ {delay} -> {transform}",
    slots={
        "signal": (
            "What is being echoed: spikes, intentions, anomalies, embeddings, "
            "effector trajectories, phase-space oscillations."
        ),
        "delay": (
            "Temporal offset: 50ms, 1_cycle, 3_iterations, 200ms, next_frame."
        ),
        "transform": (
            "How the returning signal is modified: attenuate, amplify, filter, "
            "invert, normalize, phase_shift."
        )
    },
    examples=[
        {
            "description": "Echo spike activity with attenuation.",
            "echo": "ECHO spikes @ 50ms -> attenuate"
        },
        {
            "description": "Echo symbolic intention across cycles.",
            "echo": "ECHO intention @ 1_cycle -> normalize"
        },
        {
            "description": "Echo cyber anomaly with amplification.",
            "echo": "ECHO cyber_anomaly @ 200ms -> amplify"
        }
    ]
)

PATTERNS[pattern_12_echo.id] = pattern_12_echo


def render_echo(signal: str, delay: str, transform: str) -> str:
    """
    Render an Echo pattern instance using the canonical structure.
    """
    return f"ECHO {signal} @ {delay} -> {transform}"