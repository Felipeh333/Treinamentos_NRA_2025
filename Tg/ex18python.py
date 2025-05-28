numeros = []

for i in range(5):
    n = int(input(f'{i+1}º numero:'))
    numeros.append(n)

maior = numeros[0]
menor = numeros[0]
posicao_maior = 0
posicao_menor = 0


for i in range (1,5):
    if numeros[i] > maior:
        maior = numeros [i]
        posicao_maior = i
    if numeros[i] < menor:
        menor = numeros [i]
        posicao_menor = i

print ('Números digitados:', numeros)
print (f'maior valor:{maior} na posição {posicao_maior}')
print (f'menor valor: {menor} na posição {posicao_menor}')