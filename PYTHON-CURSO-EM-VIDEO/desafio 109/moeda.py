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