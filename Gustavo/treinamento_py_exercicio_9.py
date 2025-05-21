# Autoria:Gustavo Leal Malafaia
# Data:18/05/2025
# Objetivo do programa:Somar entrada de números pares

soma = 0

for i in range(6):
    numero = int(
        input('Insira o número que deseje incluir na execução do programa: '))
    if numero % 2 == 0:
        soma += numero

print(f'A soma dos números pares é: {soma} ')
