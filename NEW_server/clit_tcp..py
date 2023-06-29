#! /usr/bin/python3

import socket
import time

destino         = "localhost",2323
clientS         = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
utf8            = "UTF-8"
while 1:
    try:
        conex           = clientS.connect(destino)
    except ConnectionRefusedError:
        print("conexão recusada\n")
        
    print(conex)

    mensage = input(">cl ")#fechar conexão
    conex.send(mensage.encode(utf8))
