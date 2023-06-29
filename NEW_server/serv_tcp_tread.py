import socket
import select
import threading

# Configurações do servidor
HOST = '127.0.0.1'  # Endereço IP do servidor
PORT = 2323        # Porta para conexão

# Criação do socket TCP
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(5)  # O servidor irá aceitar até 5 conexões simultâneas

# Lista de sockets para leitura
sockets_list = [server_socket]
client_threads = {}  # Dicionário para mapear os clientes às suas threads


def conn():
    print(addr,"enviu: ", (data).decode(utf8))
    dataD   =data.decode(utf8)
    
    if dataD       ==  "ext":
        print("finalizando conexão")
        sock.close()
        sockets_list.remove(sock) 
    elif dataD      ==  "e":
        print("fechando server...")
        time.sleep(2)
        exit()
    elif dataD      ==  "\h":
        conn.send((menu).encode(utf8))    
    elif dataD      ==  "f":
        pass
    elif dataD[:2]         ==  "d:":
        print(">> filename: "+dataD[2:])
        print(Di)
        
    else:
        conn.send("opção invalida".encode(utf8))
print('Aguardando conexões...')

def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if data:
                # Processa os dados recebidos (exemplo: transforma em maiúsculas)
                processed_data = data.decode().upper()
                # Envia a resposta de volta para o cliente
                client_socket.sendall(processed_data.encode())
            else:
                # Conexão encerrada
                print('Conexão encerrada por:', client_socket.getpeername())
                client_socket.close()
                break
        except ConnectionResetError:
            # Conexão encerrada inesperadamente
            print('Conexão encerrada por:', client_socket.getpeername())
            client_socket.close()
            break

def accept_connections():
    while True:
        # Obtém a lista de sockets prontos para leitura, escrita e exceção
        read_sockets, _, _ = select.select(sockets_list, [], [])

        for sock in read_sockets:
            # Nova conexão recebida
            if sock == server_socket:
                client_socket, addr = server_socket.accept()
                sockets_list.append(client_socket)
                conn.send((">> Bem vindo, \h - help").encode(utf8))
                print('Conexão estabelecida por:', addr)


                # Cria uma nova thread para lidar com o cliente
                thread = threading.Thread(target=handle_client, args=(client_socket,))
                thread.start()
                client_threads[client_socket] = thread

# Inicia a thread para aceitar conexões
accept_thread = threading.Thread(target=accept_connections)
accept_thread.start()