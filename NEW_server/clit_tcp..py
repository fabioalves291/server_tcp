#! /usr/bin/python3

import socket
import datetime
#from default import destino
destino         = "localhost",2323
clientS         = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
utf8            = "UTF-8"
bollConexo      = False

buffer          = 512
# iniciando conexão
while True:
    try:
        conn           = clientS.connect(destino)
        print("conexão estabecida")
        break
    except ConnectionRefusedError:
        print("conexão recusada\n")
# enviado msg

try:
    data = clientS.recv(buffer)
except ConnectionRefusedError:
    print("conexão recusada\n")
    
while True:
    print(data.decode(utf8))
    mensage = input(">>  ")
    if mensage =="":
        print("envie algo")
        continue
    clientS.send((mensage).encode(utf8))
    try:
        data = clientS.recv(buffer)
    except ConnectionRefusedError:
        print("conexão recusada\n")
    
    
    # ;) toda ação resulta numa reação
