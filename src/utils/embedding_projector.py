import numpy as np
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

# Try to import UMAP if installed
try:
    import umap
    UMAP_AVAILABLE = True
except ImportError:
    UMAP_AVAILABLE = False


def project_embeddings_pca(embeddings, n_components=2):
    """
    Project embeddings using PCA.
    embeddings: list or numpy array of vectors
    """
    embeddings = np.array(embeddings)
    pca = PCA(n_components=n_components)
    return pca.fit_transform(embeddings)


def project_embeddings_tsne(embeddings, n_components=2, perplexity=30):
    """
    Project embeddings using t-SNE.
    """
    embeddings = np.array(embeddings)
    tsne = TSNE(n_components=n_components, perplexity=perplexity)
    return tsne.fit_transform(embeddings)


def project_embeddings_umap(embeddings, n_components=2):
    """
    Project embeddings using UMAP if available.
    """
    if not UMAP_AVAILABLE:
        raise ImportError("UMAP is not installed. Install with: pip install umap-learn")

    embeddings = np.array(embeddings)
    reducer = umap.UMAP(n_components=n_components)
    return reducer.fit_transform(embeddings)
import numpy as np
import matplotlib.pyplot as plt
import io
from PIL import Image

def make_3d_scatter(points, labels=None, figsize=(6, 6)):
    """
    Create a 3D scatter plot from 3D points.
    Returns a PNG image (PIL Image object).
    points: Nx3 array of 3D coordinates
    labels: optional list of labels for coloring
    """

    points = np.array(points)

    if points.shape[1] != 3:
        raise ValueError("make_3d_scatter: points must be Nx3 for 3D scatter")

    fig = plt.figure(figsize=figsize)
    ax = fig.add_subplot(111, projection='3d')

    if labels is None:
        ax.scatter(points[:, 0], points[:, 1], points[:, 2], s=10, c='blue')
    else:
        labels = np.array(labels)
        ax.scatter(points[:, 0], points[:, 1], points[:, 2], s=10, c=labels, cmap='viridis')

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("3D Embedding Scatter")

    buf = io.BytesIO()
    plt.savefig(buf, format="png", bbox_inches="tight", pad_inches=0.1)
    plt.close(fig)
    buf.seek(0)

    return Image.open(buf)
