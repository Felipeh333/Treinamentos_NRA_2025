n = int(input("Quantos números que comparar:"))
numbers = []

for i in range(n):
    numbers.append(int(input()))

def maior(numbers):
    maior_numero = numbers[0]
    for i in numbers:
        if i > maior_numero:
            maior_numero = i
    return maior_numero

print(f"O maior número é {maior(numbers)}")
