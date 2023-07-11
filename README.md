# programa para redes - server tcp de transferência de arquivos.
programa de envio de arquivo e downloud de arquivo usando socket em python

o primeiro acesso deve ser em primeiro plano(para poder configurar os arquivos necessarios)

se o servidor tentar abrir e a porta estiver ainda sendo usada o app vai criar outro ifconfig, isso acaba resultando na possibilidade de criar
varios serves em portas diferentes mas o client so conectará de acordo com ifconfig que foi atualizado.

#### !No cmd do windows use

    python3 servertcp (argv) ou python servertcp (argv)
#### !No terml do linux use

    python3 servertcp (argv) ou python servertcp (argv) ou ./servertcp (argv)


o server antigo ele requecebia uma requisição e fechava a requisição, nao sendo uma conexões simuntaneas mas rapidas, recebia  a solicitação, enviava o arquivo e fechava a conexão para proximo cliente.
o novo ele coloca as conexões em uma lista em passa pelpo for e ainda colocando tredding para deixar simuntaneas e com processos separados.