dias = float(input('Informe a quantidade de dias que o carro foi alugado: '))
km = float(input('Informe a quantidade de km percorridos: '))
preco = dias*60 + km*0.15
print(f'O valor total eh: {preco}')