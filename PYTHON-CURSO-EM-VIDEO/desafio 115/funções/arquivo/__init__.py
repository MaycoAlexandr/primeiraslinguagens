
def temosarquivo(nome):
    try:
       a = open(nome, 'rt')
       a.close()
    except FileNotFoundError:
#FileNotFoundError: funciona verificando a existencia de um arquivo.
        return False
    else:
        return True


def criaarquivo(nome):
    try:
        a = open(nome, 'wt+')
        # 'wt+' escreve e cria um novo arquivo
        a.close()
    except:
        print('ouve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso.')


def linha():
    return '=-' * 42

def cabeçalho(txt):
    print(linha())
    print(txt.center(84))
    print(linha())


def lerarquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao abrir o arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>10} anos de idade')
    #'rt' lê o artquivo
    #a.readlines: mostra cada linha do arquivo dito
    finally:
        a.close()


def cadastrar(arq, nome='arquivo desconhecido', idade=0):
    try:
        a = open(arq, 'at')
#'at' vem de append no arquivo
    except:
        print('Erro ao abrir ao encontrar o arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Erro ao escrever dados: ')
        else:
            print(f'Novo registro de {nome} adicionado.')
            a.close()
