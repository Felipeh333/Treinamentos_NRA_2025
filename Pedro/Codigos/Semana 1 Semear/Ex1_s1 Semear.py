d_alugados = float(input('Quanto tempo o carro foi alugado?'))
km = float(input('Kilometragem percorrida?'))

price = (d_alugados*60) + (0.15 * km)

print('O valor que deve ser pago é {}'.format(price))

