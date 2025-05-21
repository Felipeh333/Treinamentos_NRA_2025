# Autoria:Gustavo Leal Malafaia
# Data:19/05/2025
# Objetivo do programa: Descobrir o maior valor inteiro em uma lista


# Definição de variável do programa
valores = []

# Função que descobre o maior valor da lista de números


def maior(numeros):
    return max(numeros)


# Criação da lista de números
tamanho_lista = int(input('Insira quantos valores irá colocar na lista: '))

for i in range(tamanho_lista):
    valores.append(int(input('Insira um valor para a lista:')))

print(maior(valores))
