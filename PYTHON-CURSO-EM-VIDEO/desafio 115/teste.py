import funções
from funções import arquivo
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivo.temosarquivo(arq):
    arquivo.criaarquivo(arq)

while True:
    opcao = funções.menu(['Criar novo cadastro', 'Ver cadastrados', 'Sair do menu'])
    if opcao == 1:
#opção de criar novo cadastro
        arquivo.cabeçalho('NOVO CADASTRO')
        nome = input('Nome: ')
        idade = funções.leiaint('Idade: ')
        arquivo.cadastrar(arq, nome, idade)
    elif opcao == 2:
    #opção de ver pessoas cadastradas
        arquivo.lerarquivo(arq)
    elif opcao == 3:
        print('Obrigado, continue praticando amigão!')
        break
    else:
        print('ERRO. Opção inválida.')
    sleep(2)


