lista_principal = []
lista_pares = []
lista_impares = []

for i in range(10):
    n = int(input(f'Número {i + 1}: '))
    lista_principal.append(n)

    if n % 2 == 0:
        lista_pares.append(n)
    else:
        lista_impares.append(n)

print(f'Números digitados: {lista_principal}\nPares: {lista_pares}\nÍmpares: {lista_impares}')
