nomes = []
jogador_partidas = {}
jogador_gols = {}
total_gols = 0

while True:
    nome = input('Nome do jogador: ')
    nomes.append(nome)

    partidas = int(input('Partidas: '))
    jogador_partidas[nome] = partidas

    gols = int(input('Gols: '))
    jogador_gols[nome] = gols

    continuar = input('Deseja continuar (S/N)? ')
    if continuar.upper() == 'N':
        break

quadro_geral = []
quadro_geral.append(jogador_partidas)
quadro_geral.append(jogador_gols)

print('')
print('=' * 50)

for i in range(len(nomes)):
    print(f'Jogador: {nomes[i]} | Partidas: {jogador_partidas.get(nomes[i])} | Gols: {jogador_gols.get(nomes[i])}')
    total_gols += jogador_gols.get(nomes[i])

print(f'O time marcou: {total_gols} gols')
print('=' * 50, '\n')
