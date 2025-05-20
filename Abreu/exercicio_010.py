while True:
    n1 = int(input("Digite um número: "))

    if n1 >= 0:
        for i in range (10):
            print(f"{n1} x {i+1} = {n1 * (i + 1)}")
    else:
        break
