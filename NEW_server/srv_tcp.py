#! /usr/bin/python3

import socket
import time

ipserver    =   "localhost"
port        =   2323
buffersize  =   512

utf8        =   "UTF-8"
srv         =   socket.socket(socket.AF_INET, socket.SOCK_STREAM)
localhost   =   (ipserver, port)

srv.bind(localhost)

srv.listen(5)
while 1 :
    print("aguardando conexão")
    conn,addr   =   srv.accept()
    print(conn,"\nbr",addr)
    print("recebendo data")
    data        =   conn.recv(buffersize)
    if data.decode(utf8)== "cl":
        conn.close()
    
