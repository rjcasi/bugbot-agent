function generateManifold(k) {
    const xs = [];
    const ys = [];

    for (let t = -3; t <= 3; t += 0.05) {
        xs.push(t);
        ys.push(Math.exp(k * t) - 1);
    }

    return { xs, ys };
}

function updateManifold() {
    const k = parseFloat(document.getElementById("curvature").value);
    const theta = parseFloat(document.getElementById("theta").value);

    document.getElementById("kval").textContent = k.toFixed(2);
    document.getElementById("tval").textContent = theta + "°";

    const { xs, ys } = generateManifold(k);

    const tangentLength = 0.5;
    const rad = theta * Math.PI / 180;

    const tx = [0, tangentLength * Math.cos(rad)];
    const ty = [0, tangentLength * Math.sin(rad)];

    const data = [
        {
            x: xs,
            y: ys,
            mode: "lines",
            line: { color: "cyan", width: 3 },
            name: "Manifold Curve"
        },
        {
            x: tx,
            y: ty,
            mode: "lines+markers",
            line: { color: "magenta", width: 4 },
            marker: { size: 10 },
            name: "Tangent Vector"
        }
    ];

    const layout = {
        paper_bgcolor: "#050510",
        plot_bgcolor: "#050510",
        xaxis: { color: "#ccccff" },
        yaxis: { color: "#ccccff" },
        margin: { l: 40, r: 20, t: 20, b: 40 },
        title: { text: "Manifold Panel", font: { color: "#e0e0ff" } }
    };

    Plotly.newPlot("plot", data, layout);
}

document.addEventListener("DOMContentLoaded", () => {
    document.getElementById("curvature").addEventListener("input", updateManifold);
    document.getElementById("theta").addEventListener("input", updateManifold);
    updateManifold();
});