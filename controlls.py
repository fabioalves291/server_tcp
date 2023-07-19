import default
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
    
def list_dir_strg():
    return dir_list(self)