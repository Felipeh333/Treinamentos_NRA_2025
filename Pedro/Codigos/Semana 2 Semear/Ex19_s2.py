import random

lista = []
par = []
impar = []


for i in range (5):
    lista.append(random.randint(1,100))

for n in lista:
    if (n % 2) == 0:
        par.append(n)

    else:
        impar.append(n) 


print(lista)
print(par)
print(impar)