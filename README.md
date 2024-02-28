# servidor de transferência de arquivos.

Programa de envio e download de arquivos utilizando sockets em Python, criado para práticas de **Programação de Redes de Computadores.**

O primeiro acesso deve ser em primeiro plano, permitindo a configuração dos arquivos necessários.

Se o servidor tentar abrir uma porta que ainda está em uso, o aplicativo irá criar outro socket, resultando na possibilidade de criar vários servidores em portas diferentes. No entanto, o cliente só se conectará de acordo com o socket que foi atualizado no ifconfig.

#### !No cmd do windows use

    python3 servertcp (argv) ou python servertcp (argv)
#### !No terml do linux use

    python3 servertcp (argv) ou python servertcp (argv) ou ./servertcp (argv)


O servidor anterior recebia uma solicitação, atendia-a e fechava a conexão, não permitindo conexões simultâneas, mas sendo rápidas. Ele recebia a solicitação, enviava o arquivo e fechava a conexão para o próximo cliente.
No novo servidor, as conexões são colocadas em uma lista e percorridas através de um laço 'for', enquanto threads são utilizadas para torná-las simultâneas e com processos separados.
