time = []

while True: 
    jogador = {}




    nome = input ('Nome do jogador:')
    jogador["nome"] = nome

    partidas = int(input(f'Quantas partidas {nome} jogou?'))
    gols = []
    total = 0 
    
    
    
    for i in range(partidas):
        g = int(input(f'Gols numa partida {i+1}:'))
        gols.append(g)
        total += g 
    jogador ["gols"] = gols
    jogador ["total"] = total

    time.append(jogador)

    def continuar():
    
        while True:
            resposta = input('Deseja adicionar outro jogador (S/N):').strip().upper()
            if resposta == 'S':
                return True 
            elif resposta == 'N':
                return False
            else:
                print("Resposta inválida. Digite S para sim ou N para não.")
    
    if not continuar():  
        break

print("\n--- Jogadores cadastrados ---")
for jogador in time:
    print(jogador)

print("\n--- Detalhes por jogador ---")
for jogador in time:
    print(f"{jogador["nome"]} fez um total de {jogador["total"]} gols.")


