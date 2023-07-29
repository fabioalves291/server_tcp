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
clientS.settimeout(5)

def recvallmsg():
    def rcvfile():
        try:
            global tradTruercvmsg,mensage  
            if mensage[:2] == 'd:':
                print(mensage,tradTruercvmsg,"bollfile")
                namefile = mensage[2:]
                print(f">> Downloading {mensage[2:]}")
                file        =   open(fr'client_files/{mensage[2:]}','wb')
                data    =   clientS.recv(buffer)   
                print(data)
                while data:
                    try:
                        #apag
                        if f" final {namefile}" in data.decode(utf8):
                            print(f">> {namefile} finally")
                            break
                        if data.decode(utf8) == fr">>{namefile} inistent":
                            break
                    except UnicodeDecodeError:
                        pass
                    #apagar
                    file.write(data)
                    if not mensage[:2] == 'd:':
                        # print("diferente de d:")
                        # 2 versao, 1 no udp
                        break
                    data    =   clientS.recv(buffer)   
                    print(data)
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
            #tradTruercvmsg = False # desativaapois receber a primeira mensagem
            #desativado pois agora tem time out
            #entao vair ficar na escuta por msg e nao por arquivos 
            try:
                #print("iniciando tred recv")
                data = clientS.recv(buffer)
                print(data.decode(utf8))
            except ConnectionRefusedError:
                print("conexão recusada\n")
            except UnicodeDecodeError:
                print("unicode")
                continue
            except TimeoutError:
                #print("timed out")
                continue


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
            time.sleep(0.05)
            # colocar um await depois caso tenha mensagem para receber
            mensage = input(">> ")
            if mensage =="":
                print(">> empty input")
                continue
            elif mensage[:2] =="d:":
                #time.sleep(10) error perder o buffer
                tradTruercvmsg = False
            elif mensage[:2]=="u":
                pass
            else:
                tradTruercvmsg = True
            clientS.send((mensage).encode(utf8))
#depois trocar por um redirecionadamento de ponteiro!
except ConnectionResetError:
    print(">> Lost connection")
