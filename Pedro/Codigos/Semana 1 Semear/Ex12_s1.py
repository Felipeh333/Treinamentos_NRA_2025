nome = input("Nome da pessoa: ")
count_blank = 0

print(nome.upper())
print(nome.lower())

for i in range(len(nome)):
    if nome[i]== ' ':
        count_blank += 1

print(f"Número de letras:{len(nome) - count_blank}")

for j in range(len(nome)):
    if nome[j] == ' ':
        break

print(f"Número de letras do primeiro nome: {j}")