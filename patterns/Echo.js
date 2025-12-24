const pattern12Echo = new Pattern({
  id: 12,
  name: "Echo",
  mantra: "Resonance, recurrence, temporal memory.",
  essence:
    "The pattern that repeats or returns signals across time, creating " +
    "temporal structure, memory, and rhythmic reinforcement.",
  structure: "ECHO {signal} @ {delay} -> {transform}",
  slots: {
    signal:
      "What is being echoed: spikes, intentions, anomalies, embeddings, effector trajectories, phase-space oscillations.",
    delay:
      "Temporal offset: 50ms, 1_cycle, 3_iterations, 200ms, next_frame.",
    transform:
      "How the returning signal is modified: attenuate, amplify, filter, invert, normalize, phase_shift."
  },
  examples: [
    {
      description: "Echo spike activity with attenuation.",
      echo: "ECHO spikes @ 50ms -> attenuate"
    },
    {
      description: "Echo symbolic intention across cycles.",
      echo: "ECHO intention @ 1_cycle -> normalize"
    },
    {
      description: "Echo cyber anomaly with amplification.",
      echo: "ECHO cyber_anomaly @ 200ms -> amplify"
    }
  ]
});

PATTERNS[pattern12Echo.id] = pattern12Echo;


function renderEcho(signal, delay, transform) {
  return `ECHO ${signal} @ ${delay} -> ${transform}`;
}