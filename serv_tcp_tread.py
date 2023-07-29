import socket
import select
import threading
import datetime
import time
from controlls import (verificar_dirsDefauts, list_dir_strg, sendfile, 
                       listconn, sendto, creatuserforip,
                       createlog_client,createlogstatus,
                       queryallhistory,sendmsgallclients)
from default import menu, filesDir_names_defauts
from Oldmodel import sistemas_de_argv


#init arg
sistemas_de_argv()
# Configurações do servidor
host = '127.0.0.1'  
port = 2323        
userlim = 2
# Criação do socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((host, port))
server_socket.listen(userlim)

# Lista de sockets para leitura
sockets_list = [server_socket]
client_threads = {}  

utf8 = "utf-8"

def conn(addr, data, sock):
    dataD = data.decode(utf8)
    structmsg = str(addr)+"enviou:"+str(dataD)
    print(">> "+structmsg)
    createlog_client(addr[0],structmsg)
    
    if dataD == "b:":
        sendmsgallclients(sock,data)
    elif dataD[:2] == "d:":
        #socket.sendfile(file, offset=0, count=None)

        sendfile(dataD[2:], sock)        
    elif dataD == "f":         
        sock.send((list_dir_strg("files_server")[0]).encode(utf8))
    
    elif dataD == "\\h" or dataD == "?":
        sock.send(menu.encode(utf8))
    elif dataD == "l":
        strglistconn = listconn(sockets_list)
        sock.sendall(strglistconn.encode(utf8))
    elif dataD == "lh":
        sock.sendall((queryallhistory(addr[0])).encode(utf8))
    elif dataD[:2] == "m:":
        sendto(sockets_list,sock,dataD)
  
    elif dataD == "q":
        msg = (">> connection terminated by: "+addr)
        print(msg)
        sock.send(msg.encode(utf8))
        sock.close()
        sockets_list.remove(sock)
        exit()
    
    elif dataD == "u":
        pass
    elif dataD == "rss":
        pass
    elif dataD == "w":
        pass
    else:
        sock.send(">> Invalid option".encode(utf8))

def handle_client(connection):
    while True:
        try:
            data = connection.recv(1024)
            if data:
                conn(connection.getpeername(), data, connection)
            else:
                ## criar log final de seção
                print('>> connection terminated by:', connection.getpeername())
                sockets_list.remove(connection)  # Remover o socket da lista
                connection.close()
                break
        except ConnectionResetError:
            # Conexão encerrada inesperadamente
            ## criar log de encerramento bruto
            print('>> connection terminated by:', connection.getpeername())
            sockets_list.remove(connection)  # Remover o socket da lista
            connection.close()
            break

def accept_connections():
    while True:
        try:
            # Obtém a lista de sockets prontos para leitura, escrita e exceção
            read_sockets, _, _ = select.select(sockets_list, [], [])

            for sock in read_sockets:
                if sock == server_socket:
                    connection, addr = server_socket.accept()
                    creatuserforip(str(addr[0]))
                    sockets_list.append(connection)
                    connection.send(">> Bem-vindo, \\h - help".encode(utf8))
                    print('>> Conexão estabelecida por:', addr)

                    # Cria uma nova thread para lidar com o cliente
                    thread = threading.Thread(target=handle_client, args=(connection,))
                    thread.start()
                    client_threads[connection] = thread
        except Exception as e:
            #criar logger
            print('Error:', str(e))

# Inicia a thread para aceitar conexões
print(">> Verifying configuration files")
verificar_dirsDefauts(filesDir_names_defauts)

# verificar arquivos de configurações
print(">> server open")

accept_thread = threading.Thread(target=accept_connections)
accept_thread.start()
createlogstatus("SERVER ACTIVATED")
