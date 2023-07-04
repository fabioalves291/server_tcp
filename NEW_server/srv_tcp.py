import socket
import select
import time
from default import menu

ipserver = "localhost"
port = 2323
buffersize = 512

utf8 = "UTF-8"

# Configurações do servidor
host = '127.0.0.1'  
port = 2323
userslim = 5

# Criação do socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((host, port))
server_socket.listen(userslim)  

# Lista de sockets para leitura
sockets_list = [server_socket]

print('Aguardando conexões...')

def connn(conn, addr, data):
    print(addr, "enviou:", data.decode('utf-8'))
    dataD = data.decode('utf-8')

    if dataD == "ext":
        print("close connection")
        conn.close()
        sockets_list.remove(conn)
    elif dataD == "e":
        print("fechando server...")
        time.sleep(2)
        exit()
    elif dataD == "\\h":
        conn.send(menu.encode('utf-8'))
    elif dataD == "f":
        conn.send("send file".encode('utf-8'))
    elif dataD[:2] == "d:":
        print(">> filename:", dataD[2:])
        # Faça algo com a variável Di aqui
        pass
    else:
        conn.send("opção inválida".encode('utf-8'))

while True:
    # Obtém a lista de sockets prontos para leitura, escrita e exceção
    read_sockets, _, _ = select.select(sockets_list, [], [])
    for sock in read_sockets:
        try:
            if sock == server_socket:
                conn, addr = server_socket.accept()
                sockets_list.append(conn)
                print('Conexão estabelecida por:', addr)
                conn.send(">> Bem-vindo, \\h - help".encode(utf8))

            # Dados recebidos de uma conexão existente
            else:
                try:
                    print("data wait", addr)
                    data = sock.recv(1024)
                    if data:
                        connn(sock, addr, data)
                    else:
                        # Conexão encerrada
                        sock.close()
                        sockets_list.remove(sock)
                except ConnectionResetError:
                    # Conexão encerrada inesperadamente
                    sock.close()
                    sockets_list.remove(sock)
                    continue
        except Exception as e:
            print("err", str(e))
            pass
