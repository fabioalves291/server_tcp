#! /usr/bin/python3


import socket
import select
import time
from default import menu
import datetime
import threading
import concurrent.futures

def connn():
        print(addr,"enviu: ", (data).decode(utf8))
        dataD   =data.decode(utf8)
        
        if dataD       ==  "ext":
            print("finalizando conexão")
            sock.close()
            sockets_list.remove(sock) 
        elif dataD      ==  "e":
            print("fechando server...")
            time.sleep(2)
            exit()
        elif dataD      ==  "\h":
            conn.send((menu).encode(utf8))    
        elif dataD      ==  "f":
            pass
        elif dataD[:2]         ==  "d:":
            print(">> filename: "+dataD[2:])
            print(Di)
            
        else:
            conn.send("opção invalida".encode(utf8))


ipserver    =   "localhost"
port        =   2323
buffersize  =   512


utf8        =   "UTF-8"

srv         =   socket.socket(socket.AF_INET, socket.SOCK_STREAM)
localhost   =   (ipserver, port)


# Configurações do servidor
HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 2323        # Porta para conexão

# Criação do socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(5)  # O servidor irá aceitar até 5 conexões simultâneas

# Lista de sockets para leitura
sockets_list = [server_socket]

print('Aguardando conexões...')

while True:
    # Obtém a lista de sockets prontos para leitura, escrita e exceção
    read_sockets, _, _ = select.select(sockets_list, [], [])

    for sock in read_sockets:
        print(sock)
        # Nova conexão recebida
        if sock == server_socket:
            conn, addr = server_socket.accept()
            sockets_list.append(conn)
            print('Conexão estabelecida por:', addr)
            conn.send((">> Bem vindo, \h - help").encode(utf8))

        # Dados recebidos de uma conexão existente
        else:
            try:
                print("data wait",addr)
                data = sock.recv(1024)
                if data:
                    connn()
                else:
                    # Conexão encerrada
                    sock.close()
                    sockets_list.remove(sock)
            except ConnectionResetError:
                # Conexão encerrada inesperadamente
                sock.close()
                sockets_list.remove(sock)
                continue