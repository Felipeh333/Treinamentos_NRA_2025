while True:
    numero = int(input("Digite um número para ver a tabuada (negativo para sair): "))
    if numero < 0:
        print("Programa encerrado.")
        break
    print("Tabuada de {}:".format(numero))
    for i in range(1, 11):
        print("{} x {} = {}".format(numero, i, numero * i))
