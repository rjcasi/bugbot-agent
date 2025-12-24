const pattern19Fracture = new Pattern({
  id: 19,
  name: "Fracture",
  mantra: "Controlled breaking, divergence, branching.",
  essence:
    "The pattern that splits unified structures into divergent branches, " +
    "enabling exploration, parallelism, and controlled breakdown.",
  structure: "FRACTURE {whole} along {axes} -> {branches}",
  slots: {
    whole:
      "The unified structure: spike_stream, symbolic_intention, cyber_signal, effector_plan, embedding_vector, phase_space_trajectory.",
    axes:
      "The criteria for splitting: entropy_axis, meaning_axis, anomaly_axis, energy_axis, temporal_axis, spatial_axis.",
    branches:
      "The resulting divergent paths: low_entropy+high_entropy, literal+metaphoric, normal+suspect, safe+aggressive."
  },
  examples: [
    {
      description: "Fracture spike stream by entropy.",
      fracture: "FRACTURE spike_stream along entropy_axis -> low_entropy+high_entropy"
    },
    {
      description: "Fracture symbolic intention by meaning.",
      fracture: "FRACTURE symbolic_intention along meaning_axis -> literal+metaphoric"
    },
    {
      description: "Fracture cyber signal by anomaly.",
      fracture: "FRACTURE cyber_signal along anomaly_axis -> normal+suspect"
    }
  ]
});

PATTERNS[pattern19Fracture.id] = pattern19Fracture;


function renderFracture(whole, axes, branches) {
  return `FRACTURE ${whole} along ${axes} -> ${branches}`;
}