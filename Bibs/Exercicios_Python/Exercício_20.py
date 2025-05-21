# Desenvolvido por Beatriz Matias
# Exercício 20

time = []

while True:
    jogador = {}
    jogador['nome'] = input("\nNome do jogador: ")
    partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

    gols = []
    total = 0
    for i in range(partidas):
        gol = int(input(f"    Quantos gols na partida {i+1}? "))
        gols.append(gol)
        total += gol

    jogador['gols'] = gols
    jogador['total'] = total

    time.append(jogador.copy())

    continuar = input("Deseja adicionar outro jogador? (s/n): ")
    if continuar != 's':
        break

print("\n Informações sobre o time:")
gols_totais = 0
for j in time:
    print(f"\nJogador: {j['nome']}")
    print(f"  Gols por partida: {j['gols']}")
    print(f"  Total de gols: {j['total']}")
    gols_totais += j['total']

print("Total de gols do time:", gols_totais)


