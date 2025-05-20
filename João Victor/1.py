print('digite por quantos dias o carro foi alugado:' )

d = int(input())

print('digite quantos quilômetros foram percorridos:')

km = int(input())

preço = (d*60)+(0.15*km)

print("Você tem que pagar:",preço)