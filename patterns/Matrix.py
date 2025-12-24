pattern_26_matrix = Pattern(
    id=26,
    name="Matrix",
    mantra="Multi-dimensional structuring, cross-axis meaning, coordinated interaction.",
    essence=(
        "The pattern that organizes meaning across multiple axes, forming "
        "structured, coherent, multi-dimensional relationships."
    ),
    structure="MATRIX {axes} via {mapping} -> {cell}",
    slots={
        "axes": (
            "The dimensions: time_axis, meaning_axis, energy_axis, cyber_axis, "
            "spatial_axis, phase_axis."
        ),
        "mapping": (
            "The interaction rule: orthogonal, aligned, weighted, cross_product, "
            "tensor_map, symbolic_projection."
        ),
        "cell": (
            "The resulting unit: meaning_cell, spike_cell, cyber_cell, effector_cell, "
            "memory_cell, phase_cell."
        )
    },
    examples=[
        {
            "description": "Create a meaning cell from time and meaning axes.",
            "matrix": "MATRIX time_axis+meaning_axis via tensor_map -> meaning_cell"
        },
        {
            "description": "Form a cyber cell from cyber and energy axes.",
            "matrix": "MATRIX cyber_axis+energy_axis via weighted -> cyber_cell"
        },
        {
            "description": "Generate a phase cell from spatial and phase axes.",
            "matrix": "MATRIX spatial_axis+phase_axis via orthogonal -> phase_cell"
        }
    ]
)

PATTERNS[pattern_26_matrix.id] = pattern_26_matrix


def render_matrix(axes: str, mapping: str, cell: str) -> str:
    """
    Render a Matrix pattern instance using the canonical structure.
    """
    return f"MATRIX {axes} via {mapping} -> {cell}"