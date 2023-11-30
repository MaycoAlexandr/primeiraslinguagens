from time import sleep
c = ('\033[0;30;41m',# 0vermelho
       '\033[0;30;42m',#1verde
       '\033[0;30;43m',#2amarelo
       '\033[0;30;44m',#3azul
       '\033[0;30;45m',#4roxo
       '\033[0;32;40m',#5preferido
)
def titu(msg, cor=0):
    tam = len(msg)+2
    print(c[cor], end='')
    print('=' * tam)
    print(f' {msg}')
    print('=' * tam)
    print(c[0], end='')
    sleep(1)


def ajuda(comando):

    titu(f'Acessando o camando \'{comando}\'...', 2)
    print(c[5], end='')
    help(comando)
    print(c[5], end='')
    sleep(2)




comando = ''
while True:
    titu('SISTEMA DE AJUDA', 3)
    n = (input('Digite o comando que deseja pesquisar>> '))
    if n.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titu('Até a proxima', 0)
