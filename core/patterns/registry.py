# core/patterns/registry.py

class Pattern:
    def __init__(self, id, name, mantra="", essence="", structure="", slots=None, examples=None):
        self.id = id
        self.name = name
        self.mantra = mantra
        self.essence = essence
        self.structure = structure
        self.slots = slots or []
        self.examples = examples or []


# ---------------------------------------------------------
# Minimal pattern registry (you can expand later)
# ---------------------------------------------------------

pattern_registry = [
    Pattern(
        id=1,
        name="Identity",
        mantra="A is A",
        essence="Self-similarity",
        structure="X → X",
        slots=["X"],
        examples=["1 → 1", "self → self"]
    ),
    Pattern(
        id=2,
        name="Difference",
        mantra="A is not B",
        essence="Contrast",
        structure="X ≠ Y",
        slots=["X", "Y"],
        examples=["1 ≠ 2", "red ≠ blue"]
    )
]