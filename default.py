import os

utf8 = "UTF-8"
menu = """
###########################################################
b:      -   enviar mensagem para dos clientes do servidor
d:      -   d: mais o nome do arquivo para donwload 
f       -   listar arquivos para download
m:ip:port:msg - para enviar msg para um client do servidor  
ext     -   fechar conexão
###########################################################"""

EEcurrent_Directory = os.path.dirname(os.path.abspath(__file__))
namedir_serverfiles = "file_server"
namedir_log         = "log"
namedir_clientlog   = "client_log"
filesDir_names_defauts = [namedir_serverfiles,namedir_clientlog, namedir_log]