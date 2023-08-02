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
def uploadbyclient(sock,namefile,headmsg):
    try:
        MSGLEN = ((headmsg).split("\nlenfile\n".encode(utf8)))
        print(MSGLEN)
        msgf = MSGLEN[1]
        file = open(f"client_files/{namefile}","wb")
        file.write(msgf)
        
        if MSGLEN[0] == msgf:
            data = False
        contbuffer = msgf
        print(len(contbuffer),len(msgf),int(MSGLEN[0]),type(MSGLEN[0]),type(contbuffer))
        while len(contbuffer) < int(MSGLEN[0]):
            # print(int(MSGLEN[0]) - len(contbuffer),"buffer")
            data = sock.recv(min((int(MSGLEN[0]) - len(contbuffer)),buffer))
            # print(data)
            if data == b"":
                print("finnaly erro")
                break
            #print(len(data),"recv")
            contbuffer = contbuffer + data
            print(len(contbuffer))
            file.write(data)
        file.close()
        print("finalziado download")
    except IndexError:
        file.close()
        return 0 
    except TimeoutError:
        print("timeout")
        file.close()
        pass
def recvallmsg():
    
    while True:
        time.sleep(0.3) 
        # time necessario para nao grudar o recv da funcao uploadbyclient!
        global tradTruercvmsg
        if tradTruercvmsg:
            #tradTruercvmsg = False # desativaapois receber a primeira mensagem
            #desativado pois agora tem time out
            #entao vair ficar na escuta por msg e nao por arquivos 
            try:
                
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
            else:
                #err decohecido
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
            elif mensage[:2]=="d:":
                clientS.send((mensage).encode(utf8))
                tradTruercvmsg = False
                namefile = mensage[2:]
                MSGLEN = clientS.recv(512)
                uploadbyclient(clientS, namefile, MSGLEN)
                continue
            elif mensage[:2]=="u:":
                clientS.send((mensage).encode(utf8))

                namefile = mensage[2:]
                lenfile = str(os.path.getsize(f'client_files/{namefile}'))
                clientS.send((f'{lenfile}\nlenfile\n').encode(utf8))
                
                file = open(f"client_files/{namefile}","rb")
                fileread = file.read()
                # print(fileread)
                print(len(fileread))
                clientS.send(fileread)
                file.close()
                print(namefile,"Envoy")
                continue
            
            else:
                tradTruercvmsg = True
            clientS.send((mensage).encode(utf8))
#depois trocar por um redirecionadamento de ponteiro!
except ConnectionResetError:
    print(">> Lost connection")
