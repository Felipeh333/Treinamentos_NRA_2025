numeros = []

i = 0
for i in range(5):
    num = float(input(f'Insira o {i+1}° número: '))
    numeros.append(num)

print()
print(numeros)
print(f'O maior valor é {max(numeros)}, na posição {numeros.index(max(numeros))}')
print(f'O menor valor é {min(numeros)}, na posição {numeros.index(min(numeros))}')