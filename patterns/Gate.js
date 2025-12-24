const pattern11Gate = new Pattern({
  id: 11,
  name: "Gate",
  mantra: "Thresholds, transitions, conditional passage.",
  essence:
    "The pattern that regulates what may pass, when, and under what " +
    "conditions, ensuring controlled transformation.",
  structure: "GATE {input} ? {condition} -> {outcome}",
  slots: {
    input:
      "What is attempting to pass: spikes, cyber packets, symbolic intentions, effector commands, memory updates.",
    condition:
      "The rule determining passage: entropy<=0.5, alignment>=0.8, anomaly==0, energy_preserved, drift<=0.1.",
    outcome:
      "What happens: pass, block, reroute, dampen, quarantine, escalate."
  },
  examples: [
    {
      description: "Gate spike bursts based on entropy.",
      gate: "GATE spikes ? entropy<=0.5 -> pass"
    },
    {
      description: "Gate cyber packets based on anomaly score.",
      gate: "GATE cyber_packet ? anomaly==0 -> pass"
    },
    {
      description: "Gate symbolic intention based on alignment.",
      gate: "GATE intention ? alignment>=0.8 -> execute"
    }
  ]
});

PATTERNS[pattern11Gate.id] = pattern11Gate;


function renderGate(input, condition, outcome) {
  return `GATE ${input} ? ${condition} -> ${outcome}`;
}