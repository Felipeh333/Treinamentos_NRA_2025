time = []  


for i in range(11):
    print(f'Jogador {i+1}: ')
    jogador = {}

    jogador['nome'] = input('Nome do jogador: ')
    jogador['num_partidas'] = int(input(f'Quantas partidas o(a) {jogador["nome"]} jogou? '))

    jogador['gols por partida'] = []
    jogador['total'] = 0

    for i in range(jogador['num_partidas']):
        gols = int(input(f'Gols na partida {i + 1}: '))
        jogador['gols por partida'].append(gols)
        jogador['total'] += gols

    time.append(jogador.copy())
    print()


while True:
    continuar = input('Quer adicionar outro jogador? (s/n): ')
    if continuar.lower() != 's':
        break

    jogador = {}

    jogador['nome'] = input('Nome do jogador: ')
    jogador['num_partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))

    jogador['gols por partida'] = []
    jogador['total'] = 0

    for i in range(jogador['num_partidas']):
        gols = int(input(f'  Gols na partida {i + 1}: '))
        jogador['gols por partida'].append(gols)
        jogador['total'] += gols

    time.append(jogador.copy())
    print()

print()
print(time)
print()
print('Jogadores do time:')
for i in time:
    print(f'Nome: {i["nome"]}')
    print(f'Número de partidas: {i["num_partidas"]}')
    print(f'Gols por partida: {i["gols por partida"]}')
    print(f'Total de gols: {i["total"]}')
    print()

total_time = 0  
for jogador in time:
    total_time += jogador['total']  

print(f'Total de gols do time: {total_time}')

#QUE CÓDIGO TRABALHOSO