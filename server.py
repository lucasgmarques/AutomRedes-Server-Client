#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import socket

SERVERHOST = '0.0.0.0'
SERVERPORT = 9472

def create_socket(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))

    return server_socket


def accept_conn(server_socket):
    server_socket.listen()
    print("Servidor está escutando...")
    conn, addr = server_socket.accept()
    print("Servidor conectado por:", addr)

    return conn, addr


def receive_msg(conn, addr):
    while True:
        data = conn.recv(1024)
        if not data:
            break
        print(f"[Cliente] {addr}: {data.decode()}")
        data = input(' -> ')
        conn.send(data.encode())


def main():
    connections = 0
    server_socket = create_socket(SERVERHOST, SERVERPORT)
    while True:
        conn, addr = accept_conn(server_socket)
        connections += 1
        receive_msg(conn, addr)
        conn.close()
        print(f"Número de conexões atendidas: {connections}")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Você interrompeu o programa.")
