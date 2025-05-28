soma_pares = 0
for i in range(6):
    numero = int(input("Digite o {}º número inteiro: ".format(i + 1)))
    if numero % 2 == 0:
        soma_pares += numero

print("A soma dos números pares digitados é: {}".format(soma_pares))

