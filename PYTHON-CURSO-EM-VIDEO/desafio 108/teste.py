import moeda

n = float(input('Digite um valor:'))
print(f'O dobro de {moeda.estilo(n)} vale {moeda.estilo(moeda.dobro(n))}')
print(f'A metade de {moeda.estilo(n)} vale {moeda.estilo(moeda.metade(n))}')
print(f'Com a taxa de 10 % a mais fica {moeda.estilo(moeda.mais(n, 10))}')
print(f'Com a taxa de 10% a menos fica {moeda.estilo(moeda.menos(n, 10))}')