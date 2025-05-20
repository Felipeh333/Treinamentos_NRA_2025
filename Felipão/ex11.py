saque = int(input('Quanto você deseja sacar? '))

cinquenta = saque // 50
resto = saque % 50

vinte = resto // 20
resto = resto % 20

dez = resto // 10
resto = resto % 10

um = resto

print(f'Você vai receber {cinquenta} nota(s) de 50 reais, {vinte} nota(s) de 20 reais, {dez} nota(s) de 10 reais e {um} moeda(s) de 1 real')