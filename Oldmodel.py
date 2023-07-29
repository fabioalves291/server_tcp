import sys,os,time
from controlls import createlogstatus

def sistemas_de_argv():
    try:
        if sys.argv[1]         ==   r'/start':
            createlogstatus('SERVIDOR CARREGADO NA MEMÓRIA')
            print('primeiro acesso deve ser em primeiro plano para a configuração de ifconfig se estiver configurado ignore esta mensagem')
        elif sys.argv[1]       ==   r'/stop':
            createlogstatus('SERVIDOR REMOVIDO NA MEMÓRIA')
            # listconfig          =   readifconfig()    
            port                =    2323   
            WindowsLinux        =   input('digite 1 para windows ou 2 para linux:')
            if WindowsLinux == '1':
                os.system(f'netstat -a -n -o | findstr {port} > portid.txt')
            elif WindowsLinux == '2':
                os.system(f'fuser -n tcp {port} > portid.txt')
            file                =   open('portid.txt','r')
            process             =   file.read()
            process             =   process[-6:]
            process             =   str(process).replace(' ', '')
            if WindowsLinux == '1':
                os.system(f'Taskkill /f /PID {process} ')
            elif WindowsLinux == '2':
                os.system(f'kill -9 {process}')
            else:
                print('opção invalida')
                exit()
            file.close()
        # print(f'processo {process} interrompido que estava utilizando a porta {port}  ')          
            os.remove('portid.txt')
            time.sleep(3.5)
            exit()
        elif sys.argv[1]       ==   r'/help':
            print('nome_aplicação_servidor.py < /start | /stop | /help >')
            print('o primeiro acesso dever sem em primeiro plano para configurar o server')
            time.sleep(3.5)
            exit()
        else:
            print('nome_aplicação_servidor.py < /help >')
            print('o primeiro acesso dever sem em primeiro plano para configuração')
            time.sleep(3.5)
            exit()
    except IndexError:
        print('nome_aplicação_servidor.py < /help >')
        time.sleep(3.5)
        exit()
    except FileNotFoundError:
        print('arquivos depentes inexistentes')
        #allfilesdependetes()
        print('inicie novamente o app')
        time.sleep(3.5)
        exit()
