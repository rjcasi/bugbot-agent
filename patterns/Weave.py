pattern_14_weave = Pattern(
    id=14,
    name="Weave",
    mantra="Integration, synthesis, multi-stream coherence.",
    essence=(
        "The pattern that fuses multiple signals, modalities, or organs into "
        "a unified, coherent structure or behavior."
    ),
    structure="WEAVE {threads} via {loom} -> {pattern}",
    slots={
        "threads": (
            "The streams being combined: spikes+embeddings, cyber_logs+intention, "
            "effector_pose+phase_space, fuzz+defense."
        ),
        "loom": (
            "The integration method: weighted_sum, attention_map, symbolic_binding, "
            "phase_alignment, cross_entropy_fusion, temporal_sync."
        ),
        "pattern": (
            "The resulting unified structure: fused_embedding, coherent_action, "
            "unified_signal, stabilized_behavior."
        )
    },
    examples=[
        {
            "description": "Fuse spikes and embeddings via attention.",
            "weave": "WEAVE spikes+embeddings via attention_map -> fused_embedding"
        },
        {
            "description": "Integrate cyber logs with intention.",
            "weave": "WEAVE cyber_logs+intention via symbolic_binding -> coherent_action"
        },
        {
            "description": "Unify effector pose with phase-space.",
            "weave": "WEAVE effector_pose+phase_space via phase_alignment -> unified_signal"
        }
    ]
)

PATTERNS[pattern_14_weave.id] = pattern_14_weave


def render_weave(threads: str, loom: str, pattern: str) -> str:
    """
    Render a Weave pattern instance using the canonical structure.
    """
    return f"WEAVE {threads} via {loom} -> {pattern}"