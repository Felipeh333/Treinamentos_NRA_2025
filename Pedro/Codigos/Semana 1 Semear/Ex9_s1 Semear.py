numbers = []
resultado = []

for i in range (6):
    numbers.append(int(input("numero:")))

print("Somas pares:")

for i in range(6):
        for j in range (i + 1, 6):
            soma = numbers[i] + numbers[j]
            if (soma) % 2 == 0:
                if soma not in resultado:
                    resultado.append(numbers[i] + numbers[j])

for n in resultado:
     print(f"{n}")