import requests

def fuzz_chain():
    print('Running fuzz chain...')
    payloads = [None, '', {'key':'A'*500}]
    for p in payloads:
        try:
            r = requests.post('http://localhost:5000/api/test', json=p)
            print(f'Payload {p} -> {r.status_code}')
        except:
            print('Error sending payload')