#! /usr/bin/python3
import threading
import socket
import datetime
import time
import os
#from default import destino

destino         = "localhost",2323
clientS         = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
utf8            = "UTF-8"
bollConexo      = False
buffer          = 512
clientS.settimeout(10)

def recvallmsg():
    def rcvfile():
        try:
            global tradTruercvmsg 
            global mensage
            if mensage[:2] == 'd:':
                namefile = mensage[2:]
                print(f">> Downloading {mensage[2:]}")
                file        =   open(fr'client_files/{mensage[2:]}','wb')
                data    =   clientS.recv(buffer)   
                print(data)
                while data:
                    try:
                        if f" final {namefile}" in data.decode(utf8):
                            print(f">> {namefile} finally")
                            break
                        if data.decode(utf8) == fr">>{namefile} inistent":
                            break
                    except UnicodeDecodeError:
                        pass
                    #input(str(data)+"recebendo")
                    file.write(data)
                    if not mensage[:2] == 'd:':
                        # print("diferente de d:")
                        # 2 versao, 1 no udp
                        break
                    # print("segundo data")
                    data    =   clientS.recv(buffer)   
                    print(data)
                #     print("finalizado segundo") 
                # print(f">> Downloaded {mensage[2:]}")
                # print(f">> Saving {mensage[2:]}")
                
                # print("finalizando arquivo")
                mensage = str()
        except NameError:
            pass
        except TimeoutError:
            file.close()
            mensage = str()
            print("timed out")
            return 0 

    while True:
        rcvfile()
        global tradTruercvmsg
        if tradTruercvmsg:
            tradTruercvmsg = False # desativaapois receber a primeira mensagem
            try:
                print("iniciando tred")
                data = clientS.recv(buffer)
                print(data.decode(utf8))
            except ConnectionRefusedError:
                print("conexão recusada\n")
            except UnicodeDecodeError:
                print("unicode")
                rcvfile()

try:
    os.mkdir('client_files')
except FileExistsError:
    pass


try:
    while True:
        try:
            conn           = clientS.connect(destino)
            print(">> Connection success")
            break
        except ConnectionRefusedError:
            time.sleep(4)
            print(">> ERR Connection\n")

    tradTruercvmsg = True
    thread = threading.Thread(target=recvallmsg)
    thread.start()

    while True:
            time.sleep(0.005)
            # colocar um await depois caso tenha mensagem para receber
            mensage = input(">>  ")
            if mensage =="":
                print(">> empty input")
                continue
            elif mensage[:2] =="d:":
                tradTruercvmsg = False
                # clientS.send(("zerar recv").encode(utf8))
            else:
                tradTruercvmsg = True
            clientS.send((mensage).encode(utf8))
#depois trocar por um redirecionadamento de ponteiro!
except ConnectionResetError:
    print(">> Lost connection")
