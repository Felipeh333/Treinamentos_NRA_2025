valor_casa = float(input('Qual é o valor da casa a ser financiada? \n'))
salario = float(input('Qual é o salário do requerente? \n'))
duracao = int(input('Quantos anos durará o financiamento? \n'))

parcela = valor_casa / (duracao * 12)

if parcela >= (salario*0.3):
    print('Infelizmente o financiamento não foi aprovado')
else:
    print('Parabéns! Seu financiamento foi aprovado')