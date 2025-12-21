"""
BugBotAgent — Core Agent Class
------------------------------

This class represents the "organism-level" controller for your system.
Each subsystem (symbolic attention, STDP spikes, cyber defense, robotics)
is treated as an organ with its own internal logic.

The agent orchestrates:
- compression of experience
- prediction of next state
- symbolic meaning extraction
- cyber fuzz pattern defense
- robotics embodiment
"""

from typing import Dict, Any, Optional


class BugBotAgent:
    """
    The central nervous system of the BugBot organism.
    """

    def __init__(
        self,
        attention_module=None,
        spiking_module=None,
        cyber_defense_module=None,
        robotics_module=None,
        llm_module=None,
        config: Optional[Dict[str, Any]] = None,
    ):
        """
        Initialize the agent with optional organs.
        """
        self.attention = attention_module
        self.spikes = spiking_module
        self.cyber = cyber_defense_module
        self.robotics = robotics_module
        self.llm = llm_module
        self.config = config or {}

    # ---------------------------------------------------------
    # Core Loop
    # ---------------------------------------------------------

    def perceive(self, input_data: Any) -> Dict[str, Any]:
        if self.attention:
            return self.attention.encode(input_data)
        return {"raw": input_data}

    def adapt(self, encoded_state: Dict[str, Any]) -> Dict[str, Any]:
        if self.spikes:
            return self.spikes.update(encoded_state)
        return encoded_state

    def defend(self, encoded_state: Dict[str, Any]) -> Dict[str, Any]:
        if self.cyber:
            return self.cyber.evaluate(encoded_state)
        return {"defense": "no_cyber_module"}

    def embody(self, encoded_state: Dict[str, Any]) -> Dict[str, Any]:
        if self.robotics:
            return self.robotics.act(encoded_state)
        return {"robotics": "no_robotics_module"}

    def think(self, encoded_state: Dict[str, Any]) -> Dict[str, Any]:
        """
        Use the LLM organ to reflect on the current state.
        """
        if not self.llm:
            return {"llm": "no_llm_module"}

        summary_prompt = f"""
You are BugBotAgent, a modular organism.

Current state:
{encoded_state}

Briefly describe:
- what you perceive
- whether it looks anomalous
- what you would do next
"""
        response = self.llm.generate(summary_prompt.strip())
        return {"llm_response": response}

    # ---------------------------------------------------------
    # Full Agent Step
    # ---------------------------------------------------------

    def step(self, input_data: Any) -> Dict[str, Any]:
        encoded = self.perceive(input_data)
        adapted = self.adapt(encoded)
        defended = self.defend(adapted)
        embodied = self.embody(defended)
        reflection = self.think(defended)

        return {
            "perceived": encoded,
            "adapted": adapted,
            "defended": defended,
            "embodied": embodied,
            "reflection": reflection,
        }

    # ---------------------------------------------------------
    # Utility
    # ---------------------------------------------------------

    def load_config(self, config: Dict[str, Any]):
        self.config.update(config)

    def summary(self) -> Dict[str, Any]:
        return {
            "attention_module": str(type(self.attention)),
            "spiking_module": str(type(self.spikes)),
            "cyber_defense_module": str(type(self.cyber)),
            "robotics_module": str(type(self.robotics)),
            "llm_module": str(type(self.llm)),
            "config_keys": list(self.config.keys()),
        }