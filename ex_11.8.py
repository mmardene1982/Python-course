
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('google.com', 80))
cmd = 'GET http://www.google.com HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(100000)
    if len(data) < 1:
        break
    print(data.decode(), end='')
    print('finisg')

    mysock.close()
