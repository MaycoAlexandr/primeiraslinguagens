def leiad(msg):
    valido = False
    while not valido:
        entrada = input(msg).replace(',', '.').strip()
        if entrada == '' or not entrada.replace('.', '').replace('-', '').isdigit():
            print(f'\033[31mErro: O valor "{entrada}" não é válido.\033[m')
        else:
            valido = True
            return float(entrada)

