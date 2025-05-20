numeros = []

for i in range (1,7):
    print(f'Número {i}')
    num = int(input('Insira um número inteiro: '))
    print('\n')

    numeros.append(num)

soma = 0
for num in numeros:
    if num % 2 == 0:
        soma = num + soma
print(f'Os números são: {numeros}')
print(f'A soma dos números pares é: {soma}')