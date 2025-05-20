cedulas = [50, 20, 10, 1]

valor = int(input('Insira o valor (inteiro) que deseja sacar: R$ '))
print()

print('Cédulas entregues:')
for nota in cedulas:
    x = valor // nota
    valor = valor % nota
    if x > 0:
        print(f'{x} cédula(s) de R${nota}')