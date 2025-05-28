

valor = float(input('Qual o valor da casa?'))

salario = float(input('Qual o salário do comprador?'))

anos = int(input('Em quantos anos ele irá pagar?'))

prestação = valor/anos 

if((prestação < 0.3*(salario))):

    print ('O emprestimo foi negado')
else: 
    print ('O empréstimo foi aprovado')

 