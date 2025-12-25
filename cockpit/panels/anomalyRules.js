// anomalyRules.js

export const anomalyRules = [
  {
    pattern: "Fracture",
    match: event => event.type === "divergence" || event.branches > 1,
    explanation: "System behavior diverged along multiple axes."
  },
  {
    pattern: "Flux",
    match: event => event.entropy_delta > 0.3,
    explanation: "High entropy shift detected — continuous instability."
  },
  {
    pattern: "Veil",
    match: event => event.hidden_fields?.length > 0,
    explanation: "Obscured or masked fields detected."
  },
  {
    pattern: "Pulsegate",
    match: event => event.timing_jitter > 50,
    explanation: "Timing irregularity — gating instability."
  },
  {
    pattern: "Anchorfield",
    match: event => event.anchor_loss === true,
    explanation: "Loss of stabilizing attractor detected."
  }
];