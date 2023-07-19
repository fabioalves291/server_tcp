import socket
import select
import threading
import time
from controlls import verificar_dirsDefauts,list_dir_strg
from default import menu,filesDir_names_defauts


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
    print(addr, "enviou:", data.decode(utf8))
    dataD = data.decode(utf8)
    if dataD == "b":
        pass
    elif dataD[:2] == "d:":
        print(">> filename:", dataD[2:])
    elif dataD == "f":
        print(list_dir_strg())
        sock.send(list_dir_strg().encode(utf8))
    elif dataD == "\\h" or dataD == "?":
        sock.send(menu.encode(utf8))
    elif dataD == "l":
        pass
    elif dataD == "q":
        msg = (">> finalizando conexão "+addr)
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
        sock.send(">> opção inválida".encode(utf8))

def handle_client(connection):
    while True:
        try:
            data = connection.recv(1024)
            if data:
                conn(connection.getpeername(), data, connection)
            else:
                ## criar log final de seção
                print('>> Conexão encerrada por:', connection.getpeername())
                sockets_list.remove(connection)  # Remover o socket da lista
                connection.close()
                break
        except ConnectionResetError:
            # Conexão encerrada inesperadamente
            ## criar log de encerramento bruto
            print('>> Conexão encerrada por:', connection.getpeername())
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
                    #criar log de acesso
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
print(">> verificando arquivos de configuração...")
verificar_dirsDefauts(filesDir_names_defauts)

# verificar arquivos de configurações
print(">> server open")
accept_thread = threading.Thread(target=accept_connections)
accept_thread.start()
