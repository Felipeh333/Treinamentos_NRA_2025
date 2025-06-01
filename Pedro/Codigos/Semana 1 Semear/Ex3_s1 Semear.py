valor_casa = float(input('Qual o valor da casa?'))
salario = float(input('Valor do salario?'))
tempo = float(input('Tempo que pretende pagar:'))

prestação = valor_casa/tempo

if prestação > salario*0.3:
    print('Emprestimo negado')

else:
    print('Emprestimo aceito')