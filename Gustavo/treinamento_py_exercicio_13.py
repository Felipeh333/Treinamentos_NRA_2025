# Autoria:Gustavo Leal Malafaia
# Data:19/05/2025
# Objetivo do programa: Ler uma frase e indicar algumas características dela


frase = input('Insira uma frase: ')

# Conta quantas vezes a letra 'A' aparece na string utilizando o método count
print(f'O número de vezes que a letra A aparece na frase é: {frase.count('A')}')

# Imprime a primeira posição da letra 'A' na frase aplicando o método find
print(f'A posição em que aparece a primeira letra A da frase é: {frase.find('A')}')

# Impressão da última posição da letra 'A' a lógica é procurar a primeira posição de A na string invertida e depois inverter essa posição de acordo com o tamanho da string
print(f'A posição em que aparece a última letra A da frase é: {len(frase) - ((frase[::-1]).find('A'))}')
