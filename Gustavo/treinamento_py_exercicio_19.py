# Autoria:Gustavo Leal Malafaia
# Data:20/05/2025
# Objetivo do progama: Receber valores e dividi-los em duas listas, entre impares e pares

lista_numeros = []

n_numeros = int(input('Digite quantos números deseja inserir: '))

for i in range(n_numeros):
    numero = int(input('Insira um número: '))
    lista_numeros.append(numero)

#Método em que para cada item da lista que atenda a seguinte condição ele fará parte da nova lista
lista_pares = [item for item in lista_numeros if item % 2 == 0]
lista_impares = [item for item in lista_numeros if item % 2 != 0]

print(f'A lista de números inserida é {lista_numeros}')
print(f'Os números pares na lista inserida são {lista_pares}')
print(f'Os números impares na lista inserida são {lista_impares}')
