soma_pares = 0

for i in range(6):

    n = int(input("Digite um número: "))

    if n % 2 == 0:
        soma_pares += n

print(f"A soma dos números pares é {soma_pares}")
