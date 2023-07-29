from default import utf8
import models
import os
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
                sock.send(msgsplit[3].encode(utf8))
    except IndexError:
        return conn.send(">> arg invalid".encode(utf8))