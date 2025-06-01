lista = []
total_gols = 0

while True:
    nome = input("Nome do jogador: ")
    partidas = int(input("Quantas partidas o jogador jogou: "))
    golspart = int(input("Número de gols: "))

    gol = golspart * partidas

    total_gols = total_gols + gol
    
    jogador = {
        "Nome" : nome,
        "Partidas" : partidas,
        "Gol" : gol
    }
    
    lista.append(jogador)

    control = input("Quer adiconar mais um jogador?(s) ou (n):")

    if control == "n":
        break

print(lista)
print(total_gols)