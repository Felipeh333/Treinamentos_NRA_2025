casa = float(input('Valor da casa: '))
salario = float(input('Salário: '))
anos = int(input('Em quantos anos irá pagar: '))

parcela = casa / (anos * 12)

if (parcela > 0.30 * salario): 
	print('Empréstimo negado')
else:
	print('Empréstimo aprovado. Valor mensal: {:.2f}'.format(parcela))
