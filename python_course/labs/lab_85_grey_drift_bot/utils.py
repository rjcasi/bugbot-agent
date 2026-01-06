import time, os

def monitor():
    print('Monitoring entropy drift...')
    for _ in range(5):
        print('Entropy:', os.urandom(4).hex())
        time.sleep(1)