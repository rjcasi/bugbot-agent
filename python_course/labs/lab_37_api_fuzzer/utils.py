import requests

def fuzz():
    url = 'http://localhost:5000/api/test'
    payloads = [None, '', 123, [], {}, {'key': 'A' * 1000}]
    for p in payloads:
        try:
            r = requests.post(url, json=p)
            print(f'Payload: {p} -> {r.status_code}')
        except Exception as e:
            print('Error:', e)