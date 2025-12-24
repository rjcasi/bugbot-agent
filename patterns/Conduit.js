const pattern21Conduit = new Pattern({
  id: 21,
  name: "Conduit",
  mantra: "Directed transmission, channeling, purposeful flow.",
  essence:
    "The pattern that routes signals, energy, and meaning through " +
    "intentional pathways toward specific destinations.",
  structure: "CONDUIT {source} via {pathway} -> {destination}",
  slots: {
    source:
      "Where the signal originates: spike_origin, symbolic_core, cyber_detector, effector_sensor, memory_node, phase_cell.",
    pathway:
      "The channel: direct_line, filtered_channel, shielded_route, energy_path, symbolic_pipe, cyber_tunnel.",
    destination:
      "Where the signal is delivered: effector_motor, meaning_core, anomaly_resolver, embedding_space, cyber_defense, phase_orbit."
  },
  examples: [
    {
      description: "Direct spike origin to effector motor.",
      conduit: "CONDUIT spike_origin via direct_line -> effector_motor"
    },
    {
      description: "Route symbolic meaning through a filter.",
      conduit: "CONDUIT symbolic_core via filtered_channel -> meaning_core"
    },
    {
      description: "Send cyber detection through a shielded route.",
      conduit: "CONDUIT cyber_detector via shielded_route -> anomaly_resolver"
    }
  ]
});

PATTERNS[pattern21Conduit.id] = pattern21Conduit;


function renderConduit(source, pathway, destination) {
  return `CONDUIT ${source} via ${pathway} -> ${destination}`;
}