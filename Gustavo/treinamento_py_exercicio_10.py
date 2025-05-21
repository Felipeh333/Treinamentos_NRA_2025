# Autoria:Gustavo Leal Malafaia
# Data:18/05/2025
# Objetivo do programa:Mostrar a Tabuada de numeros positivos

# Laço de funcionamento do programa
while True:
    # Entrada de dados
    numero = float(input('Insira o número que deseja visualizar a tabuada: '))

    # Estrutura condicional de decisão da continuação da execução do programa
    if numero >= 0:
        # Laço que realiza a tabuada
        for i in range(10):
            print(f'{numero} x {i+1} = {numero*(i+1)}')
    elif numero < 0:
        break
