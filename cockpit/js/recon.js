async function runRecon() {
    const res = await fetch("/recon");
    const data = await res.json();
    document.getElementById("recon-output").textContent =
        JSON.stringify(data.results, null, 2);
}