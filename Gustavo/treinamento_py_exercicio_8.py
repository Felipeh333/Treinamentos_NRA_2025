# Autoria:Gustavo Leal Malafaia
# Data:18/05/2025
# Objetivo do programa:Cadastras pessoas

import statistics

# Criação das variáveis do código
mulheres = {}
homens = {}
mulheres_menos20 = ''


for i in range(4):
    # Entrada de dados de cadastro
    nome = input('Insira o nome da pessoa que deseja cadastrar: ')
    idade = float(input('Insira a idade da pessoa que deseja cadastrar: '))
    sexo = input(
        'Insira o sexo da pessoa que deseja cadastrar(F = feminino, M = masculino):  ').lower()

   # Cadastro das pessoas em seus respectivos dicionários
    if sexo == 'f':
        mulheres[nome] = idade
    if sexo == 'm':
        homens[nome] = idade

# Média ponderada das idades dos homens e das mulheres
media = (statistics.mean(homens.values())*len(homens) +
         statistics.mean(mulheres.values())*len(mulheres))/(len(mulheres)+len(homens))

# Determinação de quais mulheres tem menos de 20 anos
for nome, idade in mulheres.items():
    if idade < 20:
        mulheres_menos20 = mulheres_menos20 + ' ' + nome


print(f'A média da idade do grupo é {media}')
print(f'O nome do homem mais velho é {max(homens)}')
print(f'As mulheres que tem menos de 20 anos são{mulheres_menos20}')
