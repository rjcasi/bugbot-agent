import socket, time

HOST='127.0.0.1'
PORT=9000
payloads=[b'', b'A'*10, b'A'*1000, b'\x00\xFF\x00\xFF']

if __name__ == '__main__':
    for p in payloads:
        s = socket.socket()
        s.connect((HOST, PORT))
        s.sendall(p)
        time.sleep(0.2)
        s.close()
        print('Sent:', p)