def leiaInt(mensagem):
    while True:
        entrada = input(mensagem)
        if entrada.isdigit():
            return int(entrada)
        else:
            print('Digite um número inteiro positivo')

n = leiaInt('Digite um n: ')
print('Você digitou o número {}.'.format(n))  