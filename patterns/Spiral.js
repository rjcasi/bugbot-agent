const pattern25Spiral = new Pattern({
  id: 25,
  name: "Spiral",
  mantra: "Recursive ascent, layered evolution, upward return.",
  essence:
    "The pattern that evolves structures through recursive cycles, " +
    "each iteration rising to a higher level of meaning or complexity.",
  structure: "SPIRAL {origin} via {recursion} toward {ascent}",
  slots: {
    origin:
      "The starting point: symbolic_seed, spike_origin, cyber_root, effector_base, memory_anchor, phase_source.",
    recursion:
      "The transformation rule: amplify, refine, expand, rotate, elevate, compress.",
    ascent:
      "The upward dimension: meaning_depth, energy_level, phase_height, symbolic_layer, cyber_complexity, spatial_scale."
  },
  examples: [
    {
      description: "Spiral a symbolic seed upward in meaning.",
      spiral: "SPIRAL symbolic_seed via refine toward meaning_depth"
    },
    {
      description: "Spiral spike origin upward in energy.",
      spiral: "SPIRAL spike_origin via amplify toward energy_level"
    },
    {
      description: "Spiral cyber root upward in complexity.",
      spiral: "SPIRAL cyber_root via elevate toward cyber_complexity"
    }
  ]
});

PATTERNS[pattern25Spiral.id] = pattern25Spiral;


function renderSpiral(origin, recursion, ascent) {
  return `SPIRAL ${origin} via ${recursion} toward ${ascent}`;
}