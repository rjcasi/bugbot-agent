import jwt, datetime

SECRET = 'mysecret'

def run_lab():
    print('Generating JWT token...')
    token = jwt.encode({'user':'test','exp':datetime.datetime.utcnow() + datetime.timedelta(minutes=5)}, SECRET, algorithm='HS256')
    print('Token:', token)
    print('Decoding token...')
    decoded = jwt.decode(token, SECRET, algorithms=['HS256'])
    print('Decoded:', decoded)