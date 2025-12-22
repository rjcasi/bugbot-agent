import os
import sys
from pathlib import Path
from typing import List

import gradio as gr
import numpy as np

# --- Ensure project root is on sys.path ---
ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.append(str(ROOT))

from src.utils.shared_state import shared_state
from src.utils.tensor_heatmap import generate_heatmap_png
from src.utils.spike_raster import generate_raster_png
from src.utils.embedding_projector import (
    project_embeddings_pca,
    make_3d_scatter,
)
from src.utils.fuzz_patterns import generate_and_record_fuzz


# ----- Simple token/embedding mock -----
def mock_tokenize(text: str) -> List[str]:
    return text.strip().split()


def mock_embed(tokens: List[str]) -> np.ndarray:
    rng = np.random.default_rng(len(tokens))
    return rng.normal(size=(len(tokens), 32))


# ----- Cyber arena panel -----
def cyber_arena_step(prompt: str) -> str:
    if not prompt.strip():
        return "Provide a prompt to stimulate the arena."
    tokens = mock_tokenize(prompt)
    embedding = mock_embed(tokens)
    shared_state.add_embedding(tokens, embedding)
    return f"Arena received {len(tokens)} tokens and registered an embedding."


# ----- Tensor heatmap panel -----
def tensor_heatmap_panel(rows: int, cols: int, cmap: str) -> tuple[bytes, str]:
    img = generate_heatmap_png(rows=rows, cols=cols, cmap=cmap)
    summary = f"Generated {rows}x{cols} tensor heatmap using cmap='{cmap}'."
    return img, summary


# ----- Spike raster panel -----
def spike_raster_panel(
    neurons: int,
    timesteps: int,
    firing_prob: float,
) -> tuple[bytes, str]:
    img = generate_raster_png(
        neurons=neurons,
        timesteps=timesteps,
        firing_prob=firing_prob,
    )
    summary = (
        f"Spike raster with {neurons} neurons, {timesteps} timesteps, "
        f"firing_prob={firing_prob:.2f}."
    )
    return img, summary


# ----- Embedding projector panel -----
def embedding_projector_panel() -> tuple:
    last = shared_state.get_last_embedding()
    if last is None:
        return None, "No embeddings yet – send a prompt in Cyber Arena first."
    proj = project_embeddings_pca(last, n_components=3)
    fig = make_3d_scatter(
        proj,
        labels=[f"t{i}" for i in range(proj.shape[0])],
        title="Last embedding (PCA)",
    )
    return fig, "Projected last embedding using PCA into 3D space."


# ----- Fuzz generator panel -----
def fuzz_panel(n: int):
    events = generate_and_record_fuzz(n)
    text_lines = [f"[{i}] score={e['score']:.2f} :: {e['pattern']}" for i, e in enumerate(events)]
    return "\n".join(text_lines)


# ----- Robotics panel (placeholder) -----
def robotics_step(command: str) -> str:
    if not command.strip():
        return "Send a movement or task command to see a simulated response."
    return f"Robotics module received command: '{command}'. (Simulation placeholder.)"


# ----- Model card loader -----
MODEL_CARD_PATH = ROOT / "model_card.md"


def load_model_card() -> str:
    if MODEL_CARD_PATH.exists():
        return MODEL_CARD_PATH.read_text(encoding="utf-8")
    return "# Model Card\n\nNo model_card.md found at project root."


# ----- Build Gradio UI -----
with gr.Blocks(title="BugBotAgent Cockpit") as demo:
    gr.Markdown(
        "# BugBotAgent Cockpit\n"
        "A unified organism visualizing **perception, spikes, fuzz, and embodiment**."
    )

    with gr.Tab("Cyber Arena"):
        arena_in = gr.Textbox(label="Prompt", lines=3)
        arena_out = gr.Textbox(label="Arena Response", lines=2)
        arena_btn = gr.Button("Send to Arena")

        arena_btn.click(
            cyber_arena_step,
            inputs=arena_in,
            outputs=arena_out,
        )

    with gr.Tab("Tensor Heatmap"):
        with gr.Row():
            rows = gr.Slider(4, 64, value=16, step=1, label="Rows")
            cols = gr.Slider(4, 64, value=16, step=1, label="Cols")
            cmap = gr.Dropdown(
                ["viridis", "magma", "plasma", "inferno"],
                value="viridis",
                label="Colormap",
            )
        heatmap_img = gr.Image(label="Heatmap", type="numpy")
        heatmap_txt = gr.Textbox(label="Summary", lines=2)
        heatmap_btn = gr.Button("Generate Heatmap")

        heatmap_btn.click(
            tensor_heatmap_panel,
            inputs=[rows, cols, cmap],
            outputs=[heatmap_img, heatmap_txt],
        )

    with gr.Tab("Spike Raster"):
        with gr.Row():
            neurons = gr.Slider(8, 128, value=32, step=1, label="Neurons")
            timesteps = gr.Slider(20, 300, value=100, step=5, label="Timesteps")
            firing_prob = gr.Slider(0.01, 0.3, value=0.05, step=0.01, label="Firing Prob")
        raster_img = gr.Image(label="Spike Raster", type="numpy")
        raster_txt = gr.Textbox(label="Summary", lines=2)
        raster_btn = gr.Button("Generate Raster")

        raster_btn.click(
            spike_raster_panel,
            inputs=[neurons, timesteps, firing_prob],
            outputs=[raster_img, raster_txt],
        )

    with gr.Tab("Embedding Projector 3D"):
        proj_fig = gr.Plot(label="Embedding 3D")
        proj_txt = gr.Textbox(label="Status", lines=2)
        proj_btn = gr.Button("Project Last Embedding")

        proj_btn.click(
            embedding_projector_panel,
            inputs=None,
            outputs=[proj_fig, proj_txt],
        )

    with gr.Tab("Fuzz Generator"):
        fuzz_n = gr.Slider(1, 20, value=5, step=1, label="Number of Patterns")
        fuzz_out = gr.Textbox(label="Generated Fuzz Patterns", lines=10)
        fuzz_btn = gr.Button("Generate Fuzz")

        fuzz_btn.click(
            fuzz_panel,
            inputs=fuzz_n,
            outputs=fuzz_out,
        )

    with gr.Tab("Robotics Arena"):
        robot_cmd = gr.Textbox(label="Command", lines=2)
        robot_out = gr.Textbox(label="Simulation", lines=3)
        robot_btn = gr.Button("Send Command")

        robot_btn.click(
            robotics_step,
            inputs=robot_cmd,
            outputs=robot_out,
        )

    with gr.Tab("Model Card"):
        model_card_md = gr.Markdown(load_model_card())

if __name__ == "__main__":
    demo.launch()