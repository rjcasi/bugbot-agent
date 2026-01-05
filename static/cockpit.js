function loadPanel(name) {
    fetch(`/static/panels/${name}.html`)
        .then(res => res.text())
        .then(html => {
            document.getElementById("panel-container").innerHTML = html;
        });
}

function pingRBApp() {
    fetch("/rbapp/ping")
        .then(res => res.json())
        .then(data => {
            document.getElementById("rb-output").textContent =
                JSON.stringify(data, null, 2);
        });
}
