flag = True

list = []

while flag:
    try:
        num = int(input('Digite um número inteiro: '))
        list.append(num)
    except (TypeError):
        print('Isso não é um número inteiro')
        continue
    flag = input('Deseja adicionar outro número? [S/N]') == 'S'

pares = [_ for _ in list if _ % 2 == 0]
impares = [_ for _ in list if _ % 2 != 0]

print('A lista digitada é: {}'.format(list))
print('A lista de números pares é: {}'.format(pares))
print('A lista de números ímpares é: {}'.format(impares))