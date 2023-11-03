#!/usr/bin/env python3

import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

socket.bind(("localhost", 9471))
socket.listen()

conn, addr = socket.accept()

while True:
    data = conn.recv(1024)

    if not data:
        break
    print(f"Nova mensagem de {addr[0]}: {data.decode()}")

conn.close()
