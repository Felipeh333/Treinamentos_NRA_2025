l = []

for i in range (10):
    l.append(int(input()))

par = []

for i in range (10):
    if l[i] % 2 == 0:
        par.append(l[i])

impar = []

for i in range (10):
    if l[i] % 2 == 1:
        impar.append(l[i])

print(l, par, impar)