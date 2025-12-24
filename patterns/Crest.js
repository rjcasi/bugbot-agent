const pattern33Crest = new Pattern({
  id: 33,
  name: "Crest",
  mantra: "Peak activation, maximal expression, apex moment.",
  essence:
    "The pattern that captures the moment of maximum intensity, energy, " +
    "or clarity in a wave or process.",
  structure: "CREST {wave} at {peak} :: {expression}",
  slots: {
    wave:
      "The evolving process: spike_wave, symbolic_wave, cyber_wave, effector_wave, memory_wave, phase_wave.",
    peak:
      "The apex: max_amplitude, clarity_peak, load_peak, meaning_peak, energy_peak, resonance_peak.",
    expression:
      "The resulting manifestation: full_fire, revelation, full_alert, maximum_precision, critical_transition, threshold_cross."
  },
  examples: [
    {
      description: "Crest spike wave at maximum amplitude.",
      crest: "CREST spike_wave at max_amplitude :: full_fire"
    },
    {
      description: "Crest symbolic wave at clarity peak.",
      crest: "CREST symbolic_wave at clarity_peak :: revelation"
    },
    {
      description: "Crest cyber wave at load peak.",
      crest: "CREST cyber_wave at load_peak :: full_alert"
    }
  ]
});

PATTERNS[pattern33Crest.id] = pattern33Crest;

function renderCrest(wave, peak, expression) {
  return `CREST ${wave} at ${peak} :: ${expression}`;
}