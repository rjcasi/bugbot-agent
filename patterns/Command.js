class Pattern {
  constructor({ id, name, mantra, essence, structure, slots, examples = [] }) {
    this.id = id;
    this.name = name;
    this.mantra = mantra;
    this.essence = essence;
    this.structure = structure;
    this.slots = slots;
    this.examples = examples;
  }
}

const pattern7Command = new Pattern({
  id: 7,
  name: "Command",
  mantra: "Decisive action, directional force, unambiguous intent.",
  essence:
    "The moment an agent stops perceiving and starts shaping; " +
    "transitions awareness into actuation through clear directives.",
  structure: "{directive} :: {target} @ {constraint}",
  slots: {
    directive:
      "Compressed intention; an atomic verb-like action (e.g., SCAN_PORTS, FIRE_SPIKE).",
    target:
      "Locus of change; organ, panel, tensor region, effector, memory segment.",
    constraint:
      "Guardrail on time, space, energy, ethics, or symbolic invariants."
  },
  examples: [
    {
      description: "Fire a spike in layer 2 for 50ms.",
      command: "FIRE_SPIKE :: LAYER_2 @ 50ms"
    },
    {
      description: "Rotate phase space while preserving energy.",
      command: "ROTATE_FIELD :: PHASE_SPACE @ preserve_energy"
    },
    {
      description: "Deploy non-destructive cyber shield.",
      command: "DEPLOY_SHIELD :: CYBER_ORGAN_3 @ non_destructive"
    }
  ]
});


const PATTERNS = {
  [pattern7Command.id]: pattern7Command
  // Add other patterns here (1–6, 8, …)
};


function renderCommand(directive, target, constraint) {
  return `${directive} :: ${target} @ ${constraint}`;
}


// Example usage
const cmd = renderCommand("GENERATE_FUZZ", "RED_TEAM_PANEL", "entropy<=0.7");
console.log(cmd);
// -> GENERATE_FUZZ :: RED_TEAM_PANEL @ entropy<=0.7