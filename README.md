# server tcp de transferência de arquivos.
programa de envio de arquivo e downloud de arquivo usando socket em python

o primeiro acesso deve ser em primeiro plano(para poder configurar os arquivos necessarios)

se o servidor tentar abrir e a porta estiver ainda sendo usada o app vai criar outro ifconfig, isso acaba resultando na possibilidade de criar
varios serves em portas diferentes mas o client so conectará de acordo com ifconfig que foi atualizado.

#### !No cmd do windows use

    python3 servertcp (argv) ou python servertcp (argv)
#### !No terml do linux use

    python3 servertcp (argv) ou python servertcp (argv) ou ./servertcp (argv)


O servidor anterior recebia uma solicitação, atendia-a e fechava a conexão, não permitindo conexões simultâneas, mas sendo rápidas. Ele recebia a solicitação, enviava o arquivo e fechava a conexão para o próximo cliente.
No novo servidor, as conexões são colocadas em uma lista e percorridas através de um laço 'for', enquanto threads são utilizadas para torná-las simultâneas e com processos separados.
