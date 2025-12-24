const pattern24Shell = new Pattern({
  id: 24,
  name: "Shell",
  mantra: "Protective enclosure, boundary architecture, structural containment.",
  essence:
    "The pattern that encloses and protects sensitive cores, establishing " +
    "boundaries and maintaining integrity under stress.",
  structure: "SHELL {core} with {boundary} :: {policy}",
  slots: {
    core:
      "The protected element: symbolic_core, spike_generator, cyber_kernel, effector_brain, memory_seed, phase_anchor.",
    boundary:
      "The protective layer: hard_shell, soft_shell, adaptive_shell, energy_barrier, symbolic_membrane, cyber_firewall.",
    policy:
      "The boundary rule: allow_internal_only, block_entropy>0.5, preserve_integrity, non_destructive, read_only, anomaly_block."
  },
  examples: [
    {
      description: "Protect symbolic core with adaptive shell.",
      shell: "SHELL symbolic_core with adaptive_shell :: preserve_integrity"
    },
    {
      description: "Shield spike generator with energy barrier.",
      shell: "SHELL spike_generator with energy_barrier :: block_entropy>0.5"
    },
    {
      description: "Guard cyber kernel with firewall.",
      shell: "SHELL cyber_kernel with cyber_firewall :: anomaly_block"
    }
  ]
});

PATTERNS[pattern24Shell.id] = pattern24Shell;


function renderShell(core, boundary, policy) {
  return `SHELL ${core} with ${boundary} :: ${policy}`;
}