import numpy as np
import matplotlib.pyplot as plt
import io
from PIL import Image

def generate_raster_png(spike_times, spike_ids, figsize=(6, 4)):
    """
    Generate a spike raster plot as a PNG.
    spike_times: list or array of spike timestamps
    spike_ids: list or array of neuron IDs corresponding to each spike
    """

    if spike_times is None or spike_ids is None:
        raise ValueError("generate_raster_png: spike_times and spike_ids cannot be None")

    spike_times = np.array(spike_times)
    spike_ids = np.array(spike_ids)

    fig, ax = plt.subplots(figsize=figsize)
    ax.scatter(spike_times, spike_ids, s=2, color="black")
    ax.set_xlabel("Time")
    ax.set_ylabel("Neuron ID")
    ax.set_title("Spike Raster")
    ax.grid(False)

    # Save to in-memory PNG
    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight", pad_inches=0.1)
    plt.close(fig)
    buf.seek(0)

    return Image.open(buf)
