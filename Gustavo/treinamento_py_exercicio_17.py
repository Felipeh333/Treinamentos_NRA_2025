#Autoria:Gustavo Leal Malafaia
#Data:20/05/2025
#Objetivo do progama: Inserir valores aleatórios em uma tupla

import random

lista_numeros = []

for i in range(5):
    lista_numeros.append(random.randint(1,10))

maior_valor = max(lista_numeros)
menor_valor = min(lista_numeros)

tupla_numeros = tuple(lista_numeros)
    
print(f'O menor valor da tupla é: {menor_valor}')
print(f'O maior valor da tupla é: {maior_valor}')
print(f'Os elementos da tupla são: {tupla_numeros}')