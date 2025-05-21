# Autoria:Gustavo Leal Malafaia
# Data:20/05/2025
# Objetivo do progama: Informar os extremos de uma lista e sua posição

lista_valores = []

for i in range(5):
    valor = float(
        input('Entre com um valor numérico para a lista de 5 valores:'))
    lista_valores.append(valor)

print(
    f'O maior valor digitado foi {max(lista_valores)} e sua posição é {lista_valores.index(max(lista_valores))} nos índices da lista')
print(
    f'O menor valor digitado foi {min(lista_valores)} e sua posição é {lista_valores.index(min(lista_valores))} nos índices da lista')
