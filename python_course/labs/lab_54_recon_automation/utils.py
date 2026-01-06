import requests

def run_recon():
    print('Running recon automation...')
    r = requests.get('https://example.com')
    print('Status:', r.status_code)