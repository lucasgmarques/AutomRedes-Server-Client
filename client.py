#!/usr/bin/env python3

import socket

def main():
    serverHost = 'localhost'
    serverPort = 9471

    socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    socketClient.connect((serverHost, serverPort))
    
    msg= input("Digite aqui a sua mensagem: ")

    while True:
        socketClient.send(msg.encode('utf-8'))
        data = socketClient.recv(1024).decode()

        print("Recebido do servidor: " + data)

        msg = input(" --> ")
    

    socketClient.close()

if __name__ == "__main__":
    main()
