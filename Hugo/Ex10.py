numeros = []

print('\n')
print('Digite abaixo os números inteiros que você deseja conhecer a tabuada! Ao inserir um número negativo, o recebimento se encerra.')
print()

num = int(input('Insira o número: '))
numeros.append(num)
while True:
    num = int(input('Insira o seguinte número: '))
    if num < 0:
        print('Números recebidos.')
        print()
        break
    else:
        numeros.append(num)

for num in numeros:
    print(f'Tabuada do {num}:')
    print()
    for i in range(1,11):
        print(f'{num} * {i} = {num * i}')
    print()    

