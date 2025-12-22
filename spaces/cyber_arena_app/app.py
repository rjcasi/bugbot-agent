"""
BugBotAgent — Multi-Panel Hugging Face Space
--------------------------------------------

Tabs:
1. Cyber Arena (LLM cortex switching)
2. Token Visualizer (tokens, embeddings, attention, spikes, fuzz)
3. Robotics Arena (XY movement visualization)
"""

import json
import numpy as np
import gradio as gr

# Organs
from bugbot_agent import BugBotAgent
from symbolic_attention.tensor import SymbolicAttentionTensor
from spiking_stdp.core import STDPSpikingLayer
from cyber_arena.fuzz_engine import CyberFuzzEngine
from robotics.telemetry import RoboticsEmbodiment
from llm_adapter import create_llm_adapter


# ---------------------------------------------------------
# Shared organs for Token Visualizer + Robotics Arena
# ---------------------------------------------------------

attention = SymbolicAttentionTensor(dim=32)
spikes = STDPSpikingLayer(dim=32)
cyber = CyberFuzzEngine()
robotics = RoboticsEmbodiment()


def np_to_list(x):
    return x.tolist() if isinstance(x, np.ndarray) else x


# ---------------------------------------------------------
# Cyber Arena Agent Builder
# ---------------------------------------------------------

def build_agent(backend: str):
    dummy_client = object()

    if backend == "transformers":
        llm = create_llm_adapter("transformers", model_name="gpt2")
    elif backend == "chatgpt":
        llm = create_llm_adapter("chatgpt", client=dummy_client)
    elif backend == "grok":
        llm = create_llm_adapter("grok", client=dummy_client)
    else:
        llm = None

    return BugBotAgent(
        attention_module=SymbolicAttentionTensor(dim=32),
        spiking_module=STDPSpikingLayer(dim=32),
        cyber_defense_module=CyberFuzzEngine(),
        robotics_module=RoboticsEmbodiment(),
        llm_module=llm,
    )


def cyber_arena_run(input_text, backend):
    agent = build_agent(backend)
    return agent.step(input_text)


# ---------------------------------------------------------
# Token Visualizer
# ---------------------------------------------------------

def visualize_tokens(input_text: str):
    encoded = attention.encode(input_text)
    tokens = encoded.get("tokens", [])
    vector = np_to_list(encoded.get("vector", []))
    attn = np_to_list(encoded.get("attention", []))

    spike_state = spikes.update(encoded)
    spike_vec = np_to_list(spike_state.get("spikes", []))
    weights = np_to_list(spike_state.get("weights", []))
    t = spike_state.get("time", 0)

    fuzz_state = cyber.evaluate(encoded)

    return (
        json.dumps(tokens, indent=2, ensure_ascii=False),
        json.dumps(vector, indent=2),
        json.dumps(attn, indent=2),
        json.dumps(spike_vec, indent=2),
        json.dumps(fuzz_state, indent=2),
        t,
    )


# ---------------------------------------------------------
# Robotics Arena
# ---------------------------------------------------------

def robotics_step(input_text: str):
    encoded = attention.encode(input_text)
    state = robotics.act(encoded)
    return json.dumps(state, indent=2), state["robot_state"]["x"], state["robot_state"]["y"]


# ---------------------------------------------------------
# Gradio UI (Tabbed)
# ---------------------------------------------------------

with gr.Blocks() as demo:
    gr.Markdown("# 🐞 BugBotAgent — Multi-Panel Organism Cockpit")

    with gr.Tabs():

        # -------------------------
        # Cyber Arena
        # -------------------------
        with gr.Tab("Cyber Arena"):
            gr.Markdown("### LLM Cortex Switching + Full Agent Cycle")

            input_box = gr.Textbox(label="Input or fuzz pattern")
            backend = gr.Radio(
                ["transformers", "chatgpt", "grok"],
                value="transformers",
                label="LLM Cortex Organ",
            )
            run_btn = gr.Button("Run Cycle")

            output_json = gr.JSON(label="Agent State")

            run_btn.click(
                fn=cyber_arena_run,
                inputs=[input_box, backend],
                outputs=[output_json],
            )

        # -------------------------
        # Token Visualizer
        # -------------------------
        with gr.Tab("Token Visualizer"):
            gr.Markdown("### Tokens → Embeddings → Attention → Spikes → Fuzz")

            tv_input = gr.Textbox(label="Input text")
            tv_btn = gr.Button("Visualize")

            tokens_out = gr.Code(label="Tokens")
            embed_out = gr.Code(label="Embedding Vector")
            attn_out = gr.Code(label="Attention Weights")
            spikes_out = gr.Code(label="STDP Spikes")
            fuzz_out = gr.Code(label="Fuzz Detection")
            t_out = gr.Number(label="STDP Time Step", precision=0)

            tv_btn.click(
                fn=visualize_tokens,
                inputs=[tv_input],
                outputs=[tokens_out, embed_out, attn_out, spikes_out, fuzz_out, t_out],
            )

        # -------------------------
        # Robotics Arena
        # -------------------------
        with gr.Tab("Robotics Arena"):
            gr.Markdown("### Symbolic → Motor Embodiment")

            rb_input = gr.Textbox(label="Movement commands (left/right/up/down)")
            rb_btn = gr.Button("Move")

            rb_json = gr.Code(label="Robotics State")
            rb_x = gr.Number(label="X Position")
            rb_y = gr.Number(label="Y Position")

            rb_btn.click(
                fn=robotics_step,
                inputs=[rb_input],
                outputs=[rb_json, rb_x, rb_y],
            )


if __name__ == "__main__":
    demo.launch()