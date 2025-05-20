import numpy as np

a = np.random.randint(0, 9, (3, 3))
b = np.random.randint(0, 9, (3, 3))

print(f'A matriz A é: \n{a}\n')
print(f'A matriz B é: \n{b}\n')

c = a + b
print(f'A matriz C é: \n{c}\n')

d = a * b
print(f'A matriz D é: \n{d}\n')

e = a @ b
print(f'A matriz E é: \n{e}')