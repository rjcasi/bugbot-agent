import requests, os

def pipeline():
    print('Running automation pipeline...')
    try:
        r = requests.get('http://localhost:5000')
        print('Recon:', r.status_code)
    except:
        print('Recon failed')
    print('Entropy:', os.urandom(4).hex())