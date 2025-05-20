jogadores = []
partidas = []
gols = []
flag = True

while flag:
    try:
        jogador = str(input('Digite o nome do jogador: '))
        partida = int(input('Digite o número de partidas jogadas: '))
        gol = sum([int(input('Digite o número de gols marcados na partida {}: '.format(i+1))) for i in range(partida)])
    except (TypeError):
        print('O valor digitado não é válido')
        continue
    jogadores.append(jogador)
    partidas.append(partida)
    gols.append(gol)
    flag = input('Deseja adicionar outro jogador? [S/N]').upper() == 'S'

dict_partidas = dict(zip(jogadores, partidas))
dict_gols = dict(zip(jogadores, gols))

for element in jogadores:
    print('O jogador {} jogou {} partidas e fez {} gols'.format(element, dict_partidas[element], dict_gols[element]))