sum = 0

for i in range(0,4):
    num = int(input('Digite o número: '))
    if num % 2 == 0:
        sum += num

print('A soma dos números pares é: {}'.format(sum))