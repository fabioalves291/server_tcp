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
    
def sendfile(data):
    #mudar nome da pasta para arquivo no pasta default
    data    =   data.decode(utf8)
    file        =   open(fr'files_server/{data[2:]}','rb')
    read        =   file.read()
    con.sendall(read)
    file.close()