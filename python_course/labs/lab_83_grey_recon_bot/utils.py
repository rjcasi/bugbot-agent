import requests

def run_bot():
    print('Running recon bot...')
    try:
        r = requests.get('http://localhost:5000')
        print('Status:', r.status_code)
    except:
        print('Target unreachable')