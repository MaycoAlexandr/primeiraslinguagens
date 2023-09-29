def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print(f'\033[33m{"ERRO. por favor tente novamente."}\033[m')
        else:
            return n


def linha():
    return '=-' * 42


def cabeçalho(txt):
    print(linha())
    print(txt.center(84))
    print(linha())


def menu(txt):
    cabeçalho(f'\033[33m{"MENU DE CADASTRO"}\033[m')
    c = 1
    for p in txt:
        print(f'\033[31m{c}\033[m - \033[34m{p}\033[m')
        c += 1
    print(linha())
    opc = leiaint('\033[33mOpção escolhida: \033[m')
    return opc







