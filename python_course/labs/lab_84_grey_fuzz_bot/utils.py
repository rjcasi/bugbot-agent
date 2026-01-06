import requests

def run_bot():
    print('Running fuzz bot...')
    payloads = ['', None]
    for p in payloads:
        try:
            r = requests.post('http://localhost:5000/api/test', json=p)
            print('Payload sent ->', r.status_code)
        except:
            print('Error sending payload')