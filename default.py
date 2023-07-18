import os

menu = """ 
###################################################
f       -   listar arquivos para download
d:      -   d: mais o nome do arquivo para donwload 
ext     -   fechar conexão
###################################################"""

current_Directory = os.path.dirname(os.path.abspath(__file__))

filesDir_names_defauts = ["files_server","log"]