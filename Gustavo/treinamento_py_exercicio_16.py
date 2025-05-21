# Autoria:Gustavo Leal Malafaia
# Data:19/05/2025
# Objetivo do programa: Função de input de apenas um valor numérico

def leialnt(texto):

    while True:

        entrada = input(texto)

        try:
            entrada = float(entrada)
            break
        except ValueError:
            print('Digite um valor numérico')

    return entrada


n = leialnt('Digite um n: ')

print(n)
