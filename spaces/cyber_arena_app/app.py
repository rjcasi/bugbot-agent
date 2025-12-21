"""
Cyber Arena — Hugging Face Space App
------------------------------------

This Space lets you:
- Input text or fuzz patterns
- Switch between LLM organs (Transformers / ChatGPT / Grok)
- Observe the full BugBotAgent internal cycle:
    perception → adaptation → defense → embodiment → reflection
"""

import gradio as gr

# Import your organism organs
from bugbot_agent import BugBotAgent
from symbolic_attention.tensor import SymbolicAttentionTensor
from spiking_stdp.core import STDPSpikingLayer
from cyber_arena.fuzz_engine import CyberFuzzEngine
from robotics.telemetry import RoboticsEmbodiment

# Unified LLM cortex
from llm_adapter import create_llm_adapter


# ---------------------------------------------------------
# Build a BugBotAgent with a chosen LLM backend
# ---------------------------------------------------------

def build_agent(backend: str):
    """
    Construct a BugBotAgent with the selected LLM organ.
    """

    # Core organs
    attention = SymbolicAttentionTensor(dim=32)
    spikes = STDPSpikingLayer(dim=32)
    cyber = CyberFuzzEngine()
    robotics = RoboticsEmbodiment()

    # Dummy client placeholder for cloud LLMs
    dummy_client = object()

    # Cortex organ selection
    if backend == "transformers":
        llm = create_llm_adapter("transformers", model_name="gpt2")

    elif backend == "chatgpt":
        llm = create_llm_adapter("chatgpt", client=dummy_client)

    elif backend == "grok":
        llm = create_llm_adapter("grok", client=dummy_client)

    else:
        llm = None

    # Build the organism
    agent = BugBotAgent(
        attention_module=attention,
        spiking_module=spikes,
        cyber_defense_module=cyber,
        robotics_module=robotics,
        llm_module=llm,
    )

    return agent


# ---------------------------------------------------------
# Main function executed by the UI
# ---------------------------------------------------------

def run_cycle(input_text: str, backend: str):
    """
    Build a fresh agent with the chosen LLM backend,
    run one full organism cycle, and return the internal state.
    """
    agent = build_agent(backend)
    return agent.step(input_text)


# ---------------------------------------------------------
# Gradio UI
# ---------------------------------------------------------

ui = gr.Interface(
    fn=run_cycle,
    inputs=[
        gr.Textbox(
            label="Input or fuzz pattern",
            placeholder="Type text, commands, or fuzz patterns like <script> or AAAAA"
        ),
        gr.Radio(
            ["transformers", "chatgpt", "grok"],
            value="transformers",
            label="LLM Cortex Organ",
            info="Choose the brain powering BugBot's reflection organ."
        ),
    ],
    outputs=gr.JSON(label="BugBotAgent Internal State"),
    title="🐞 BugBot Cyber Arena — LLM Cortex Switcher",
    description=(
        "A living AI organism with symbolic attention, STDP learning, "
        "cyber defense, robotics embodiment, and a pluggable LLM cortex. "
        "Switch the LLM organ live and watch the organism respond."
    ),
)

# Local dev mode
if __name__ == "__main__":
    ui.launch()