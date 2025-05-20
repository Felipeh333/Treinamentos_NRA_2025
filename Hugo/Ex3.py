casa  = float(input('Insira o valor da casa: '))
salario = float(input('Insira seu salário: '))
anos = float(input('Insira o tempo (em anos) que deseja pagar: '))
prest = casa/(anos*12)

if prest <= salario*0.3:
    print('\nEmpréstimo aceito!')
else:
    print('\nEmpréstimo negado')