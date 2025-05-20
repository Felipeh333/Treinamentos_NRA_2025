from random import randint

lista = []
n = int(input('De 1 a: '))

for i in range(5):
    lista.append(randint(1, n))

print(f'Tupla gerada: {tuple(lista)} \nValor máximo: {max(lista)}\nValor mínimo: {min(lista)}')
