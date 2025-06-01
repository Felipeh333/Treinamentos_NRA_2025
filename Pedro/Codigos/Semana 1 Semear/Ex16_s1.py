def leiaint(texto):
    while True:
        n = input(texto)

        if n.isdigit() == 1:
            return int(n)
        
        else:
            print("Numero invalido")

n = leiaint("Digite um número: ")
print(n)