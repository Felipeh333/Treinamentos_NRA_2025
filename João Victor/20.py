r = ()
time = []

while r != 'n':

    jogador = {}
    
    print('Digite o nome:')
    jogador['nome'] = input().strip()

    print('Digite o n° de partidas:')
    jogador['npartidas'] = int(input())

    print('Digite o n° de gols:')
    jogador['gols'] = int(input())
    
    time.append(jogador)

    print('Deseja continuar a adicionar? (y/n)')

    r = input().strip()


print(time)

tgols = 0

for i in range (len(time)):
    tgols = tgols + time[i]['gols']

print(tgols)