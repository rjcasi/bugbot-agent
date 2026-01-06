import requests, random, string

def randstr(n=20):
    return ''.join(random.choice(string.ascii_letters) for _ in range(n))

if __name__ == '__main__':
    url = 'http://localhost:5000'
    for _ in range(10):
        headers = {randstr(): randstr(), 'User-Agent': randstr()}
        r = requests.get(url, headers=headers)
        print('Status:', r.status_code)