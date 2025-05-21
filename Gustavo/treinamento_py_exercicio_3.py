#Autoria:Gustavo Leal Malafaia
#Data:16/05/2025
#Objetivo do progama:Determinar a aprovação de um empréstimo para a compra de uma casa, a partir de seu valor, salário do comprador e em quanto tempo pretende pagar o empréstimo

valor_casa = float(input('Qual o valor da casa que pretende comprar(em R$)? '))
salario_comprador = float(input('Qual o seu salário mensal(em R$)? '))
anos_pagamento = float(input('Em quantos anos pretende pagar a casa? '))

meses_pagamento = anos_pagamento*12

max_comprometimento_salario = 0.3*salario_comprador

parcela_mensal = valor_casa/meses_pagamento

if max_comprometimento_salario < parcela_mensal:
    print('Empréstimo negado!')
elif max_comprometimento_salario >= parcela_mensal:
    print('Empréstimo aprovado!')
