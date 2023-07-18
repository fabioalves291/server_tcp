#! /usr/bin/python3
import threading
import socket
import datetime
#from default import destino


destino         = "localhost",2323
clientS         = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
utf8            = "UTF-8"
bollConexo      = False
buffer          = 512

def recvallmsg():
    while True:
        try:
            data = clientS.recv(buffer)
            print(data.decode(utf8))
        except ConnectionRefusedError:
            print("conexão recusada\n")

while True:
    try:
        conn           = clientS.connect(destino)
        print("conexão estabecida")
        break
    except ConnectionRefusedError:
        print("conexão recusada\n")

#criar uma tradding para ficar sempre ouvindo.! e mostrando mensagens recebidas pelo servidor
thread = threading.Thread(target=recvallmsg)
thread.start()

while True:
    mensage = input(">>  ")
    if mensage =="":
        print(">> empty input")
        continue
    clientS.send((mensage).encode(utf8))
