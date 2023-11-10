#!/usr/bin/env python3
import socket

def main():
    serverHost = 'localhost'
    serverPort = 9471

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((serverHost, serverPort))

    # Servidor está pronto para receber conexões
    server_socket.listen()
    print("Servidor está escutando ...")

    # Recebe o pedido de conexão e aceita
    conn, addr = server_socket.accept()
    print("Servidor conectado por:", addr)

    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"Nova mensagem de {addr[0]}: {data.decode()}")
        data = input(' -> ')
        conn.send(data.encode())

    conn.close()

if __name__ == "__main__":
    main()
