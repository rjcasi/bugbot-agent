import requests

if __name__ == '__main__':
    url = 'http://localhost:5000/search'
    params = [{'q': ''}, {'q': 'A'*1000}, {'q': '<script>'}]
    for p in params:
        r = requests.get(url, params=p)
        print(f'{p} -> {r.status_code}')