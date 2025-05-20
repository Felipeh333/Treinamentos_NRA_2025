def leiaint(texto):
    lista = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    while True:
        n = input(texto)
        m = n.replace(' ', '')

        if m == '':
            print('ERRO! Digite um número válido!')
        else:
            for i in range(len(lista)):
                n = n.replace(lista[i], '')

            if n == '':
                return int(m)
            else:
                print('ERRO! Digite um número válido!')


n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')
