import datetime
import os
from default import utf8, namedir_clientlog, namedir_log,namedir_serverfiles, buffer
import models
from models import *


def verificar_criarDir(self):
        # tentar resolver isso depois os.path pega diretorio diferente do raiz da aplicação.
        if (os.path.isfile(self)):
            print(">>",self,"existente")
        else:
            print(">> crindo arquivo",self)
            try:
                os.mkdir(self)
            except FileExistsError:
                print(">> file:",self,"extant")
            finally:
                pass
        
def verificar_dirsDefauts(self):
    list(map(verificar_criarDir,self))
    
def list_dir_strg(self):
    msg , cont_dir =      dir_list(self)
    if cont_dir == 0:
        return (">> empty folder",cont_dir)
    return msg,cont_dir

def getfile(self):
    namefile    =   self

def sendfile(namefile,connex):
    #mudar nome da pasta para arquivo no pasta default
    # data    =   data.decode(utf8)
    try:
        print(namefile)
        file        =   open(fr'files_server/{namefile}','rb')
        read        =   file.read()
        connex.sendall(read)
        # print(read)
        file.close()
    except FileNotFoundError:
        connex.sendall((fr">>{namefile} inistent").encode(utf8))

def listconn(conns):
    strlist = str()
    cont = 1
    for conexão in conns[1:]:
        strlist += str(cont) +" "+ str(conexão.getpeername()) + "\n"
        cont    += 1
    return strlist

def sendto(sockets_list,conn,msg):
    try:
        msgsplit = msg.split(":")
        if len(msgsplit) < 3:
            return conn.send(">> arg invalid".encode(utf8))
        for sock in sockets_list[1:]:
            strut = str( "("+"'"+msgsplit[1]+"'"+", "+msgsplit[2]+")")
            if str(sock.getpeername()) == strut:
                sock.send((str(sock.getpeername())+" enviou: "+msgsplit[3]).encode(utf8))
    except IndexError:
        return conn.send(">> arg invalid".encode(utf8))
    

def creatuserforip(ip):
    try:
        os.mkdir(str(namedir_clientlog+"/"+str(ip)))
        
    except FileExistsError:
        print(">> file:",ip,"extant")
    finally:
        pass
    

def createlog_client(ip,msg):
    data = msg
    datehors        =   datetime.datetime.now()
    date            =   datetime.date.today()
    history         =   str(datehors)+' - '+str(ip)+' - '+ str(data)
   
    # print(history)
    file            =   open(f'{namedir_clientlog}/{str(ip)}/{date}','a+')
    file.write(str(history) + '\n')
    file.close()
    
    
def createlogstatus(data):
    datehors        =   datetime.datetime.now()
    date            =   datetime.date.today()
    history         =   str(datehors)+' - '+ str(data)
    # print(history)
    file            =   open(f'{namedir_log}/{date}','a+')
    file.write(str(history) + '\n')
    file.close()
    

def queryallhistory(ip):
    filesindir = os.listdir(f"{namedir_clientlog}/{ip}")
    #bufferread = (55000)
    #criar buffer de leitura para evitar esgotamento de memoria
    print()
    string = str()
    for file in filesindir:
        file = open(f"{namedir_clientlog}/{ip}/{str(file)[:10]}","r")  
        strfile = file.read()
        file.close()
    return  strfile

def sendmsgallclients(sockets_list,data):
    for socket in sockets_list[1:]:
        socket.send(data.encode(utf8))
    

def uploadbyclient(sock,namefile,headmsg):
    MSGLEN = ((headmsg).split("\nlenfile\n".encode(utf8)))
    msgf = MSGLEN[1]
    file = open(f"{namedir_serverfiles}/{namefile}","wb")
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
        print(len(data),"recv")
        contbuffer = contbuffer + data
        print(len(contbuffer))
        file.write(data)
    file.close()