def maior(lista):
    maior_numero = lista[0]
    for numero in lista:
        if numero > maior_numero:
            maior_numero = numero
    return maior_numero

lista = []
n = int(input('Quantos números inteiros deseja inserir: '))
for i in range(0, n):
    numero = int(input(f'Insira o número da posição {i}: '))
    print()
    lista.append(numero)

maior_numero = maior(lista)
print(f'O maior número é o {maior_numero}.')   