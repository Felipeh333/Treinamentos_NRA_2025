print ('Digite 5 números:')

numeros = []

for i in range(5):
    n = int(input(f'{i+1}º numero:'))
    numeros.append(n)

tupla = tuple(numeros)

maior = tupla [0]
menor = tupla [0]

for num in tupla:
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print ('Números digitados na tupla', tupla)
print ('maior valor:', maior)
print ('menor valor:', menor)
