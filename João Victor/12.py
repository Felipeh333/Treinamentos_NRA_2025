nome = input().strip()

print(nome.upper())
print(nome.lower())

space = int(nome.count(' '))
letras = int(len(nome)-space)

print(letras)

n2 = nome.split()

print(len(n2[0]))
