def dobro(d=0):
    resp = d * 2
    return resp


def metade(m=0):
    resp = m / 2
    return resp

def mais(v=0, taxa=0):
    resp = v + (v * (taxa/100))
    return resp


def menos(v=0, taxa=0):
    resp = v - (v * (taxa/100))
    return resp


def estilo(preço = 0, moeda = 'R$'):
    return f'{moeda}{preço:.2f}'.replace('.', ',')