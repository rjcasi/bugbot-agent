// bridgeModel.js

export const bridgeModel = [
  {
    physics: "Energy",
    cyber: "packet_rate",
    pattern: "Crest",
    rule: v => v > 0.8
  },
  {
    physics: "Phase",
    cyber: "timing_jitter",
    pattern: "Pulsegate",
    rule: v => v > 50
  },
  {
    physics: "Flow",
    cyber: "throughput_variance",
    pattern: "Flux",
    rule: v => v > 0.4
  },
  {
    physics: "Density",
    cyber: "entropy",
    pattern: "Fracture",
    rule: v => v > 0.6
  }
];