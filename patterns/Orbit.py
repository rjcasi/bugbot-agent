pattern_16_orbit = Pattern(
    id=16,
    name="Orbit",
    mantra="Cyclical stability, attractors, looping identity.",
    essence=(
        "The pattern that stabilizes behavior into meaningful cycles, forming "
        "attractors and rhythmic loops that preserve identity."
    ),
    structure="ORBIT {center} via {path} @ {period}",
    slots={
        "center": (
            "The attractor: symbolic invariant, spike homeostasis, cyber integrity "
            "baseline, phase-space attractor, effector neutral pose."
        ),
        "path": (
            "The trajectory: stable_cycle, oscillation, closed_loop, periodic_orbit, "
            "rhythmic_path, attractor_loop."
        ),
        "period": (
            "The timing: 50ms, 1_cycle, 3_iterations, 200ms, harmonic_period."
        )
    },
    examples=[
        {
            "description": "Orbit around the meaning core.",
            "orbit": "ORBIT meaning_core via stable_cycle @ 1_cycle"
        },
        {
            "description": "Orbit spike homeostasis in rhythmic oscillation.",
            "orbit": "ORBIT spike_homeostasis via oscillation @ 50ms"
        },
        {
            "description": "Orbit cyber integrity in a closed loop.",
            "orbit": "ORBIT cyber_integrity via closed_loop @ 200ms"
        }
    ]
)

PATTERNS[pattern_16_orbit.id] = pattern_16_orbit


def render_orbit(center: str, path: str, period: str) -> str:
    """
    Render an Orbit pattern instance using the canonical structure.
    """
    return f"ORBIT {center} via {path} @ {period}"