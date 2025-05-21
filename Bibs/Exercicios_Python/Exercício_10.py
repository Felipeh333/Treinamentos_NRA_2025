# Desenvolvido por Beatriz Matias
# Exercício 10

while True:
    numero = int(input("\nDigite um número para ver a tabuada (negativo para parar): "))
    if numero < 0:
        print("Programa encerrado.")
        break

    print(f"\nTabuada de {numero}:")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")
