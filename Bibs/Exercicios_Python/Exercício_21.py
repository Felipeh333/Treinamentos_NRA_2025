# Desenvolvido por Beatriz Matias
# Exercício 21

import numpy as np

A = np.random.randint(0, 10, (3, 3))
B = np.random.randint(0, 10, (3, 3))

print("Matriz A:\n", A)
print("\nMatriz B:\n", B)

C = A + B

print("\nMatriz C (A + B):\n", C)

D = A * B

print("\nMatriz D (A * B elemento a elemento):\n", D)

E = np.dot(A, B)

print("\nMatriz E (A multiplicado por B):\n", E)


# Esse não deu muito certo, voltar e consertar
