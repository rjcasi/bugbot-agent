pattern_23_refine = Pattern(
    id=23,
    name="Refine",
    mantra="Sharpening, precision, iterative improvement.",
    essence=(
        "The pattern that sharpens signals, structures, and behaviors through "
        "iterative correction, convergence, and precision."
    ),
    structure="REFINE {input} by {criterion} via {iteration}",
    slots={
        "input": (
            "What is being improved: spike_sequence, symbolic_structure, cyber_trace, "
            "effector_motion, embedding_vector, phase_path."
        ),
        "criterion": (
            "The improvement metric: minimize_error, maximize_alignment, reduce_entropy, "
            "increase_precision, stabilize_phase, sharpen_signal."
        ),
        "iteration": (
            "The refinement method: gradient_step, recursive_pass, smoothing, filtering, "
            "correction_loop, alignment_pass."
        )
    },
    examples=[
        {
            "description": "Refine spike sequence by reducing entropy.",
            "refine": "REFINE spike_sequence by reduce_entropy via smoothing"
        },
        {
            "description": "Refine symbolic structure by maximizing alignment.",
            "refine": "REFINE symbolic_structure by maximize_alignment via recursive_pass"
        },
        {
            "description": "Refine cyber trace by minimizing error.",
            "refine": "REFINE cyber_trace by minimize_error via correction_loop"
        }
    ]
)

PATTERNS[pattern_23_refine.id] = pattern_23_refine


def render_refine(input_: str, criterion: str, iteration: str) -> str:
    """
    Render a Refine pattern instance using the canonical structure.
    """
    return f"REFINE {input_} by {criterion} via {iteration}"