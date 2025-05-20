def maior_valor(lista):

    maior = 0
    for i in range(len(lista)):
        if lista[i] >= maior:
            maior = lista[i]
    return maior

lista = [0, 0, 0, 0, 0]

for i in range(5):
    lista[i] = int(input(f'Número {i + 1}: '))

print(maior_valor(lista))
