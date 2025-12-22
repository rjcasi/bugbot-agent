import gradio as gr
import numpy as np
import matplotlib.pyplot as plt
import io
from PIL import Image

def generate_heatmap(matrix_size=32):
    # Create a random matrix
    data = np.random.rand(matrix_size, matrix_size)

    # Plot heatmap
    fig, ax = plt.subplots(figsize=(4, 4))
    ax.imshow(data, cmap="viridis")
    ax.set_title("Random Tensor Heatmap")
    ax.axis("off")

    # Save to PNG in memory
    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight", pad_inches=0)
    plt.close(fig)
    buf.seek(0)

    return Image.open(buf)

with gr.Blocks() as demo:
    gr.Markdown("# 🔥 Tensor Heatmap Panel")
    gr.Markdown("Generate random tensor heatmaps for visualization.")

    size = gr.Slider(8, 128, value=32, label="Matrix Size")
    output = gr.Image(type="pil")

    btn = gr.Button("Generate Heatmap")
    btn.click(fn=generate_heatmap, inputs=size, outputs=output)

demo.launch()
