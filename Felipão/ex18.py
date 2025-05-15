lista = 0

for _ in range(0,5):
    num = int(input('Digite um número: '))
    lista.append(num)

print('A lista gerada é: {}'.format(lista))
print('O maior número é: {}'.format(max(lista)))
print('O menor número é: {}'.format(min(lista)))