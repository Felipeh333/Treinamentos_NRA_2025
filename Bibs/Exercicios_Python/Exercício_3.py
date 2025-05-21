# Desenvolvido por Beatriz Matias
# Exercício 3

casa = float(input('\nQual o valor da casa? '))
salario = float(input('Qual o seu salário? '))
anos = float(input('Em quantos anos pretende pagar a casa? '))

prestacao = casa / (anos*12)
limite = 0.3 * salario

if (prestacao <= limite):
    print("\nO emprestimo bancário para a compra da casa foi APROVADO.")

else:
    print("\nO emprestimo bancário para a compra da casa foi NEGADO.\n")