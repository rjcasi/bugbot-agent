import requests, io

if __name__ == '__main__':
    url = 'http://localhost:5000/upload'
    files = [
        ('file', ('empty.txt', io.BytesIO(b''))),
        ('file', ('big.txt', io.BytesIO(b'A'*100000))),
        ('file', ('binary.bin', io.BytesIO(b'\x00\xFF\x00\xFF'))),
    ]
    for f in files:
        r = requests.post(url, files=[f])
        print(f'{f[1][0]} -> {r.status_code}')