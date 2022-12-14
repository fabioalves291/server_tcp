#! /usr/bin/python3 


import os
import sys
import socket
import datetime
import time
import threading

# criar arquivo ifconfig
def createconfigfile():
    ipserver        =   input('digite o ip do server: ')
    port            =   input('digite a porta: ')
    file            =   open('.ifconfig','w')
    file.write('ipserver'       + ':' + ipserver    + '\n' )
    file.write('port'           + ':' + port        + '\n' )
    file.write('buffer-size'    + ':' + str(512)    + '\n' )
    file.write('encoding'       + ':' + 'UTF-8'     + '\n' )
    file.close()
    #adicionar funcao para sobrescrer o arquvio ja existentea


# ler e receber ifconfig
def readifconfig():
    file            = open('.ifconfig','r')
    listconfig      =   list()
    for line in file:
        line        =   line.split(':')
        listconfig.append((line[-1])[:-1])
    return listconfig  


def menu():
    msgmenu = r''' 
1°-   /q                sair 
2°-   /h                help
3°-   /f                listar os arquivos para downloud
4°-   /c                listar os arquivos pasta do client
5°-   /d:namefile       downloud do arquivo
6°-   /u:namefile       uploud do arquivo
7°-   /m                listar ips,date,msgs'''
    return msgmenu

# listar arquivos
def datalist(self):
    totallist       =   str()
    filelist        =   os.listdir(self)
    for file in filelist:
        file        =   str(file)
        wordspace   =   ((48-len(file))*' ')
        totallist   =   totallist    +   (file + wordspace + (str(os.path.getsize(fr'{self}/{file}'))) + ' Bytes'+'\n')
    return totallist

def createlog():
    global date
    datehors        =   datetime.datetime.now()
    date            =   datetime.date.today()
    history         =   str(datehors)+' - '+str(addr)+' - '+ str(data)
    # print(history)
    file            =   open(f'log_clients/{date}','a+')
    file.write(str(history) + '\n')
    file.close()

def createlogstatus(data):
    global date
    datehors        =   datetime.datetime.now()
    date            =   datetime.date.today()
    history         =   str(datehors)+' - '+ str(data)
    # print(history)
    file            =   open(f'log_clients/{date}','a+')
    file.write(str(history) + '\n')
    file.close()

def allfilesdependetes():

    try:
        file            =   open('.ifconfig','r')
    except FileNotFoundError:
        if sys.argv[1]          == r'/stop':
            exit()    
        print('arquivo ".ifconfig" inexistente')
        print('criando arquivo')
        
        createconfigfile()
    try:
        os.mkdir('server_files')
    except FileExistsError:
        pass
    try:
        os.mkdir('log_clients')
    except FileExistsError:
        pass
    try:
        os.mkdir('server_files')
    except FileExistsError:
        pass

def sistemas_de_argv():
    try:
        if sys.argv[1]         ==   r'/start':
            createlogstatus('SERVIDOR CARREGADO NA MEMÓRIA')
            print('primeiro acesso deve ser em primeiro plano para a configuração de ifconfig se estiver configurado ignore esta mensagem')
        elif sys.argv[1]       ==   r'/stop':
            createlogstatus('SERVIDOR REMOVIDO NA MEMÓRIA')
            listconfig          =   readifconfig()    
            port                =   int(listconfig[1])
            WindowsLinux        =   input('digite 1 para windows ou 2 para linux:')
            if WindowsLinux == '1':
                os.system(f'netstat -a -n -o | findstr {port} > portid.txt')
            elif WindowsLinux == '2':
                os.system(f'fuser -n tcp {port} > portid.txt')
            file                =   open('portid.txt','r')
            process             =   file.read()
            process             =   process[-6:]
            process             =   str(process).replace(' ', '')
            if WindowsLinux == '1':
                os.system(f'Taskkill /f /PID {process} ')
            elif WindowsLinux == '2':
                os.system(f'kill -9 {process}')
            else:
                print('opção invalida')
                exit()
            file.close()
        # print(f'processo {process} interrompido que estava utilizando a porta {port}  ')          
            os.remove('portid.txt')
            time.sleep(3.5)
            exit()
        elif sys.argv[1]       ==   r'/help':
            print('nome_aplicação_servidor.py < /start | /stop | /help >')
            print('o primeiro acesso dever sem em primeiro plano para configurar o server')
            time.sleep(3.5)
            exit()
        else:
            print('nome_aplicação_servidor.py < /help >')
            print('o primeiro acesso dever sem em primeiro plano para configuração')
            time.sleep(3.5)
            exit()
    except IndexError:
        print('nome_aplicação_servidor.py < /help >')
        time.sleep(3.5)
        exit()
    except FileNotFoundError:
        print('arquivos depentes inexistentes')
        allfilesdependetes()
        print('inicie novamente o app')
        time.sleep(3.5)
        exit()




sistemas_de_argv()
allfilesdependetes()

listconfig          =   readifconfig()    
ipserver            =   str(listconfig[0]) 
port                =   int(listconfig[1])
buffersize          =   int(listconfig[2])
encodingdefault     =   str(listconfig[3])
server              =   socket.socket(socket.AF_INET, socket.SOCK_STREAM)
localhost           =   (ipserver, port)
try:
    server.bind(localhost)
except OSError:
    print('!erro na porta e ip que vc digitou!')
    print('sugestão de ip:localhost, 0.0.0.0 ou seu ip')
    os.remove('.ifconfig')
    exit()

server.listen(50)
while 1:
    conn, addr      =   server.accept()
    if conn:
        threading.Thread().start()
    data            =   conn.recv(buffersize)
    data            =   data.decode(encodingdefault)
    createlog()
    if      data        == r'/h':
        conn.sendall(menu().encode(encodingdefault))
    elif    data        == r'/f':
        conn.sendall(str(datalist('server_files')).encode(encodingdefault))
    elif    data        == r'/c':
        conn.sendall(str(datalist('client_files')).encode(encodingdefault))
    elif    data        == r'/m':
        file        =   open(f'log_clients/{date}','r')
        conn.send(file.read().encode(encodingdefault))
        file.close()
    elif    data[:3]    == r'/d:':
        file        =   open(fr'server_files/{data[3:]}','rb')
        read        =   file.read()
        conn.sendall(read)
        file.close()
    elif    data[:3]    ==  r'/u:':
        file        =   open(fr'server_files/{data[3:]}','wb')
        data    =   conn.recv(buffersize)  
        while data:
            file.write(data)
            data    =   conn.recv(buffersize)   
        file.close()

    elif    data        == r'/q':
        #print(addr,'finalizou a conexão')
        conn.send(b'saindo...')
    elif    data[:3]    == r'/qx':
        if  data == r'/qxfabio..1408':
            conn.send('server turning off..'.encode(encodingdefault) )
            createlogstatus('SERVIDOR ENCERRADO POR SENHA')
            server.close()
            exit()
        else:
            conn.send('opção inválida'.encode(encodingdefault))
    else:
        try:
            conn.send(r'opção inválida./h   help'.encode(encodingdefault))
        except BrokenPipeError:
            print(addr,'erro 32')
    conn.close()
    
            
