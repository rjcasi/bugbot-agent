const pattern27Horizon = new Pattern({
  id: 27,
  name: "Horizon",
  mantra: "Limit, boundary of perception, edge of growth.",
  essence:
    "The pattern that defines the frontier of perception and capability, " +
    "revealing what lies just beyond the organism's current limits.",
  structure: "HORIZON {domain} at {boundary} -> {beyond}",
  slots: {
    domain:
      "The space of perception: meaning_domain, cyber_domain, spike_domain, effector_domain, memory_domain, phase_domain.",
    boundary:
      "The limit condition: resolution_limit, entropy_limit, energy_limit, perception_limit, complexity_limit, stability_limit.",
    beyond:
      "The frontier: deeper_meaning, higher_energy, expanded_phase, emergent_behavior, new_complexity, unknown_field."
  },
  examples: [
    {
      description: "Perceive the edge of meaning.",
      horizon: "HORIZON meaning_domain at perception_limit -> deeper_meaning"
    },
    {
      description: "Sense the cyber frontier.",
      horizon: "HORIZON cyber_domain at entropy_limit -> emergent_behavior"
    },
    {
      description: "Reach the spike resolution boundary.",
      horizon: "HORIZON spike_domain at resolution_limit -> new_complexity"
    }
  ]
});

PATTERNS[pattern27Horizon.id] = pattern27Horizon;


function renderHorizon(domain, boundary, beyond) {
  return `HORIZON ${domain} at ${boundary} -> ${beyond}`;
}