dias = int(input('Durante quantos dias o carro foi alugado? \n'))
distancia = float(input('Quantos km foram rodados? \n'))

preco = 60 * dias + 0.15 * distancia

print('O preço a pagar é de {} reais'.format(preco))