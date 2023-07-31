import os

utf8 = "UTF-8"
menu = """
###########################################################
b:      -   enviar mensagem para dos clientes do servidor
d:      -   d: mais o nome do arquivo para donwload 
f       -   listar arquivos para download
\h      -   help
lh      -   seu historico de solicitação 
m:      -   para enviar msg para um client do servidor  
u:      -   enviar arquivo para o servidor
ext     -   fechar conexão
###########################################################"""

buffer              = 512
EEcurrent_Directory = os.path.dirname(os.path.abspath(__file__))
namedir_serverfiles = "files_server"
namedir_log         = "log"
namedir_clientlog   = "client_log"
filesDir_names_defauts = [namedir_serverfiles,namedir_clientlog, namedir_log]