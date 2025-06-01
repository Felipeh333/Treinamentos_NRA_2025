lista = []

for i in range(5):
    lista.append(int(input()))

print(f"Maior número: {max(lista)}({lista.index(max(lista))}) e menore número: {min(lista)} ({lista.index(max(lista))})")