# Autoria:Gustavo Leal Malafaia
# Data:18/05/2025
# Objetivo do programa:Simular o Funcionamento de um caixa eletrônico

# Variáveis que representam o número de notas a serem sacadas
um = 0
dez = 0
vinte = 0
cinquenta = 0

# Entrada do valor a ser sacado
valor = int(input('Insira o valor que deseja sacar: '))

# Cálculo do npumero de notas necessárias
if valor >= 50:
    cinquenta = valor//50
    valor -= cinquenta*50
if valor >= 20:
    vinte = valor//20
    valor -= vinte*20
if valor >= 10:
    dez = valor//10
    valor -= dez*10
if valor >= 1:
    um = valor//1
    valor -= um

print(
    f'Você irá sacar\n{cinquenta} nota(s) de R$50\n{vinte} nota(s) de R$20\n{dez} nota(s) de R$10\n{um} nota(s) de R$1')
