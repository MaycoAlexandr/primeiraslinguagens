import moeda

n = float(input('Digite um valor:'))
print(f'O dobro de {moeda.estilo(n)} vale {moeda.dobro(n, True)}')
print(f'A metade de {moeda.estilo(n)} vale {moeda.metade(n, True)}')
print(f'Com a taxa de 10 % a mais fica {moeda.mais(n, 10, True)}')
print(f'Com a taxa de 10% a menos fica {moeda.menos(n, 10, True)}')