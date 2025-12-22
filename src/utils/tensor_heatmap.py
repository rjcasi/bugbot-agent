import numpy as np
import matplotlib.pyplot as plt
import io
from PIL import Image

def generate_heatmap_png(tensor, cmap="viridis"):
    """
    Generate a heatmap PNG from a 2D tensor (NumPy array).
    Returns a PIL Image object.
    """

    if tensor is None:
        raise ValueError("generate_heatmap_png: tensor cannot be None")

    # Convert to numpy array if needed
    tensor = np.array(tensor)

    # Create the heatmap figure
    fig, ax = plt.subplots(figsize=(4, 4))
    heatmap = ax.imshow(tensor, cmap=cmap)
    ax.axis("off")

    # Save to in-memory PNG
    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight", pad_inches=0)
    plt.close(fig)
    buf.seek(0)

    return Image.open(buf)
