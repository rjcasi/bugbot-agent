import requests

def call_ping(base_url: str):
    """Call the RB-App /ping endpoint."""
    url = f"{base_url}/ping"
    resp = requests.get(url, timeout=5)
    resp.raise_for_status()
    return resp.json()

def call_action(base_url: str, action: str):
    """Call a generic RB-App action endpoint."""
    url = f"{base_url}/action"
    payload = {"action": action}
    resp = requests.post(url, json=payload, timeout=5)
    resp.raise_for_status()
    return resp.json()
