# Autoria:Gustavo Leal Malafaia
# Data:18/05/2025
# Objetivo do programa:Cadastras pessoas

# Criação das variáveis do código
mais_18 = 0
homens = 0
mulheres_menos20 = 0
cadastrados = {}


# Laço de repetição do programa que se repete enquanto o usuário quiser cadastrar mais pessoas
while True:
    # Entrada de dados de cadastro
    idade = float(input('Insira a idade da pessoa que deseja cadastrar: '))
    sexo = input(
        'Insira o sexo da pessoa que deseja cadastrar(F = feminino, M = masculino):  ').lower()

    # Cadastro das pessoas em um dicionário
    cadastrados[sexo] = idade

    # Determinação se a pessoa cadastrada se encaixa em uma das categorias analisadas
    if idade > 18:
        mais_18 += 1
    if sexo == 'm':
        homens += 1
    if idade < 20 and sexo == 'f':
        mulheres_menos20 += 1

    # Variável que indica se o programa irá continuar
    continuar = input(
        'Deseja cadastrar mais uma pessoa?(responda com S ou N): ').lower()

    # Para o encerramento do programa ele imprime os dados em observação e encerra o programa
    if continuar == 'n':
        print(f'O número de pessoas com mais de 18 anos é : {mais_18}')
        print(f'O número de homens é: {homens}')
        print(
            f'O número de mulheres com menos de 20 anos é: {mulheres_menos20}')
        break
