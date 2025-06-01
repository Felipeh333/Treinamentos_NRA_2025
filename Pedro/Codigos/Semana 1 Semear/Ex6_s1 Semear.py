n = int(input("Numerode elementos da Pa: "))
a0 = int(input("Valor inicial da Pa: "))
r = int(input("Razão da Pa: "))

i = a0
cont = 0

while(cont < n):
    print("{}".format(i))
    i = i + r
    cont += 1

m = int(input("Voce gostaria de ver mais quantos termos?"))

while(cont < n + m):
    print("{}".format(i))
    i = i + r
    cont += 1