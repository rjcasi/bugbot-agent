import time

MAX_REQ = 5
WINDOW = 10

requests_log = []

def simulate():
    print('Simulating rate limiting...')
    for i in range(10):
        now = time.time()
        requests_log.append(now)
        requests_log[:] = [t for t in requests_log if now - t < WINDOW]
        if len(requests_log) > MAX_REQ:
            print(f'Request {i}: BLOCKED (rate limit exceeded)')
        else:
            print(f'Request {i}: ALLOWED')
        time.sleep(1)