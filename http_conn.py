import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect(("www.google.com", 80))
sock.send(b'GET /\r\n')
response = sock.recv(2048)

sock.close()

print(response.decode('utf-8'))
