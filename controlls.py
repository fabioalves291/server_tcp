import default
import models
import os

def verificar_criarDir(self):
        
        if (os.path.isfile(self)):
            print(">>",self,"existente")
        else:
            print(">> crindo arquivo",self)
            os.mkdir(self)
        
def verificar_dirsDefauts(self):
    list(map(verificar_criarDir,self))
    
    