import requests

def fuzz_form():
    url = 'http://localhost:5000/login'
    usernames = ['admin', 'test', '', 'A'*500]
    passwords = ['password', '', 'B'*500]
    for u in usernames:
        for p in passwords:
            r = requests.post(url, data={'username': u, 'password': p})
            print(f'{u}:{p} -> {r.status_code}')