n = []

for i in range (6):
    n.append(int(input()))

soma = int()

for i in range (6):
    if (n[i]%2 == 0):
        soma = soma+n[i]

print(soma)