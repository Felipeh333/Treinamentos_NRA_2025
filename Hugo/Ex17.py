import random #Tiver que pesquisar qual função trabalhava com números aleatórios para facilitar o exercício.

numeros = ()
for i in range(5):
    num = random.randint(0,100)
    numeros += (num,)

print(numeros)
print(f'O menor valor da tupla é {min(numeros)}')
print(f'O maior valor da tupla é {max(numeros)}')