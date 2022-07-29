#! /usr/bin/python3


import os
import socket



def readifconfig():
    file            = open('.ifconfig','r')
    listconfig      =   list()
    for line in file:
        line        =   line.split(':')
        listconfig.append((line[-1])[:-1])
    return listconfig

def recvprint():
    data            =   client.recv(buffersize)
    print(data.decode(encodingdefault))
    return data



try:
    os.mkdir('client_files')
except FileExistsError:
    pass


listconfig          =   readifconfig()
host                =   str(listconfig[0])
port                =   int(listconfig[1])
buffersize          =   int(listconfig[2])
encodingdefault     =   str(listconfig[3])
destino             =   host, port
print('conectado ao servidor')
print(r'/h'+20*' ','Help')

while 1: 
    client              =   socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    ms              =   input(':')
    client.connect(destino)
    if ms     == r''        :
        print('/h'+20*' '+'help')
        continue
    client.send(ms.encode(encodingdefault))
    
    if   ms     == r'/h'    :
        recvprint()

    elif ms     == r'/f'    :
        recvprint()

    elif ms     == r'/m'    :
        datastr        =   str()
        while 1:
            data    =   recvprint()
            datastr           += data.decode(encodingdefault)
            if not data:
                break
    
    elif ms[:3]     == r'/d:'   :
        file        =   open(f'client_files/{ms[3:]}','wb')
        data    =   client.recv(buffersize)   
        while data:
            file.write(data)
            data    =   client.recv(buffersize)   
        file.close()

    elif ms[:3]    == r'/u:':
        file        =   open(fr'client_files/{ms[3:]}','rb')
        readfile    =   file.read(buffersize)
        while (readfile):
            client.send(readfile)
            readfile    =   file.read(buffersize)
        print('arquivo encaminhado')
        file.close()
        
    elif ms     == r'/q'    :
        client.close()
        quit()

    elif ms[:3] == r'/qx'   :
        recvprint()
        client.close()
        exit()

    elif ms     ==r''       :
        print('vazio')
        continue

    else:
        recvprint()
    client.close()
