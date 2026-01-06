import requests

def run_chain():
    print('Running recon chain...')
    urls = ['http://localhost:5000', 'http://localhost:5000/api']
    for u in urls:
        try:
            r = requests.get(u)
            print(f'{u} -> {r.status_code}')
        except:
            print(f'{u} unreachable')