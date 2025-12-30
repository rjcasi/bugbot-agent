// cockpit.js — global cockpit panel loader

const BASE_URL = "http://127.0.0.1:8000";

function loadPanel(route) {
    const frame = document.getElementById("panelFrame");

    // Normalize route
    if (!route.startsWith("/")) {
        route = "/" + route;
    }

    const fullUrl = BASE_URL + route;

    console.log("Loading panel:", fullUrl);

    frame.src = fullUrl;
}

// --- Organ Status Polling ---
const organs = [
    "cyber_arena",
    "heatmap",
    "raster",
    "embedding_projector",
    "fuzz_generator",
    "token_visualizer",
    "model_card",
    "robotics",
    "causal_set",
    "embeddings",
    "fourier_surface",
    "robotics_panel",
    "physics_arena"
];

function updateOrganStatus() {
    organs.forEach(route => {
        const dot = document.getElementById(`status-${route}`);
        if (!dot) return;

        fetch(`${BASE_URL}/${route}`, { method: "GET" })
            .then(() => {
                dot.className = "status-dot status-online";
            })
            .catch(() => {
                dot.className = "status-dot status-offline";
            });
    });
}

// Poll every 3 seconds
setInterval(updateOrganStatus, 3000);
updateOrganStatus();


// --- Telemetry Stream ---
function startTelemetry() {
    console.log("Connecting to telemetry...");

    const ws = new WebSocket("ws://127.0.0.1:8000/ws/telemetry");

    ws.onopen = () => {
        console.log("Telemetry connected");
    };

    ws.onmessage = (event) => {
        const data = JSON.parse(event.data);
        console.log("Telemetry:", data);

        // If you add a telemetry panel later:
        // document.getElementById("telemetry-cpu").innerText = data.cpu;
        // document.getElementById("telemetry-spikes").innerText = data.spikes;
        // document.getElementById("telemetry-energy").innerText = data.energy;
    };

    ws.onclose = () => {
        console.log("Telemetry disconnected, retrying...");
        setTimeout(startTelemetry, 2000);
    };

    ws.onerror = () => {
        console.log("Telemetry error, reconnecting...");
        ws.close();
    };
}

startTelemetry();