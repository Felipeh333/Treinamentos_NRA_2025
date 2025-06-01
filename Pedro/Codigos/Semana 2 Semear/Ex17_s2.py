import random

numbers = []

for i in range (5):
    numbers.append(random.randint(1,100))
    print(f"{numbers[i]}")

tupla = tuple(numbers)

print(f"Maior número: {max(numbers)} e menore número: {min(numbers)}")