#! /usr/bin/python3
import threading
import socket
import datetime
import time
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
try:
    while True:
        try:
            conn           = clientS.connect(destino)
            print(">> Connection success")
            break
        except ConnectionRefusedError:
            time.sleep(4)
            print(">> ERR Connection\n")

    thread = threading.Thread(target=recvallmsg)
    thread.start()
    

    while True:
            time.sleep(0.005)
            # colocar um await depois caso tenha mensagem para receber
            mensage = input(">>  ")
            if mensage =="":
                print(">> empty input")
                
                continue
            clientS.send((mensage).encode(utf8))
            
            if mensage[:1] == 'd:':
                file        =   open(fr'client_files/{ms[3:]}','wb')
                data    =   client.recv(buffer)   
                while data:
                    file.write(data)
                    data    =   client.recv(buffer)   
                file.close()
            
#depois trocar por um redirecionadamento de ponteiro!
except ConnectionResetError:
    print(">> Lost connection")
