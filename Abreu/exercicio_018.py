lista = []

for i in range(5):
    n = input(f'Número {i + 1}: ')
    lista.append(n)

max = max(lista)
min = min(lista)

print(f'Maior valor: {max} (posição {lista.index(max) + 1})\nMenor valor: {min} (posição {lista.index(min) + 1})')
