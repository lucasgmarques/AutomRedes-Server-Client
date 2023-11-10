#!/usr/bin/env python3
import socket

SERVERHOST = 'localhost'
SERVERPORT = 9472

def create_socket(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    return client_socket

def main():
    msg= input("Digite aqui a sua mensagem: ")

    client_socket = create_socket(SERVERHOST, SERVERPORT)

    while msg.lower() != 'tchau':
        client_socket.send(msg.encode('utf-8'))
        data = client_socket.recv(1024).decode()

        print(f"[Servidor]: {data}")

        msg = input(" --> ")
    
    print("Finalizando a conexão!")
    client_socket.close()

if __name__ == "__main__":
    main()
