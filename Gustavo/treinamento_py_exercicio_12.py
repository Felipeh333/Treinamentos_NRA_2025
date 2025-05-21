# Autoria:Gustavo Leal Malafaia
# Data:19/05/2025
# Objetivo do programa:Exibir informações a partir do nome do Usuário

nome = input('Insira seu nome: ')

#Impressão do nome em letras maiúsculas e minúsculas usando as funções upper e lower
print(f'Seu nome com todas as letras maiúsculas é: {nome.upper()}')
print(f'Seu nome com todas as letras minúsculas é: {nome.lower()}')

#Para imprimir o número de letras a lógica utilizada é subtrair do tamanho total da string os espaços vazios
print(f'O número de letras no seu nome é: {len(nome)-nome.count(' ')}')

#Para imprimir o primeiro nome a lógica é imprimir todas as letras antes do primeiro espaço
print(f'O seu primeiro nome é: {nome[:(nome.find(' '))]}')
