from socket import *

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('127.0.0.1', 9000))
request = 'GET 127.0.0.1/some.txt HTTP 1.0\r\n\r\n'.encode()
sock.send(request)

while True:
    data = sock.recv(512).decode()
    if len(data) < 1:
        break
    print(data, end=' ')

sock.close()
