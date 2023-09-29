import moeda

n = float(input('Digite um valor:'))
print(f'O dobro de {n} vale {moeda.dobro(n)}')
print(f'A metade de {n} vale {moeda.metade(n)}')
print(f'Com a taxa de 10 % a mais fica {moeda.mais(n, 10)}')
print(f'Com a taxa de 10% a menos fica {moeda.menos(n, 10)}')