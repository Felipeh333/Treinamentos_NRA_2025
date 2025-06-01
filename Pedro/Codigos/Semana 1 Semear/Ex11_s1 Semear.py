valor = int(input("Valor para ser sacado:"))

c =int(valor / 100)
d = int((valor - c*100) / 10)
u = int(valor - c*100 - d*10)

notas_1 = u
notas_50 = c * 2

if d == 5:
    notas_50 += 1

elif d > 5:
    temp = d - 5
    notas_20 = int(temp / 2)
    if temp % 2 == 1:
        notas_10 = 1
    
elif d < 5:
    notas_20 = int(d / 2)
    if d % 2 == 1:
        notas_10 = 1


print(f"Notas de 50:{notas_50}")
print(f"Notas de 20:{notas_20}")
print(f"Notas de 10:{notas_10}")
print(f"Notas de 1:{notas_1}")