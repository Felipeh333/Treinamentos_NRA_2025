# Autoria:Gustavo Leal Malafaia
# Data:20/05/2025
# Objetivo do progama: Analisar um time de futebol e seus gols

total_gols = 0
dados_jogadores = []


# laço de cadastro dos jogadores
while True:
    # Criação de variáveis locais
    dado_jogador = {}
    gols_jogador = 0

    # Entrada de dados
    nome = input('Insira o nome do jogador: ')
    n_jogos = int(input('Insira o número de jogos que o jogador jogou: '))

    for i in range(n_jogos):
        gols_jogo = int(
            input(f'Insira o número de gols que o jogador fez no jogo {i+1}: '))
        gols_jogador += gols_jogo

    total_gols += gols_jogador

    # Criação de item de dicionário para cada dado de cada jogador
    dado_jogador['Nome'] = nome
    dado_jogador['Número de jogos'] = n_jogos
    dado_jogador['Total de gols'] = gols_jogador

    # Inserção do jogador na lista de jogadores
    dados_jogadores.append(dado_jogador)

    continuar = input(
        'Se deseja inserir mais um jogador digite S e se não N: ').lower()
    if continuar == 'n':
        break


print('Os dados dos jogadores são os seguintes:')

for item in dados_jogadores:
    print(
        f'Nome: {item['Nome']} Número de jogos: {item['Número de jogos']} Total de gols: {item['Total de gols']}')

print(f'O total de gols do time é: {total_gols}')
