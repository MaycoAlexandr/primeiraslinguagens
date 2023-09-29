def dobro(d=0, formato=False):
    resp = d * 2
    return resp if formato is False else estilo(resp)


def metade(m=0, formato=False):
    resp = m / 2
    return resp if formato is False else estilo(resp)


def mais(v=0, taxa=0, formato=False):
    resp = v + (v * (taxa/100))
    return resp if formato is False else estilo(resp)


def menos(v=0, taxa=0, formato=False):
    resp = v - (v * (taxa/100))
    return resp if formato is False else estilo(resp)


def estilo(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')


def resumo(n =0 , mai=10, meno =5):
    print('~='*50)
    print('RESUMO DAS TAXAS'.center(50))
    print(f'O valor analizaso foi \t{estilo(n)}')
    print(f'O dobro vale \t\t\t{dobro(n, True)}')
    print(f'A metade vale \t\t\t{metade(n, True)}')
    print(f'{mai}% a mais tamos \t\t{mais(n, mai, True)}')
    print(f'{meno}% a menos temos \t\t{menos(n, meno, True)}')
    print('~='*50)