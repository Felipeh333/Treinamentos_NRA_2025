import numpy as np


A = np.random.randint(0, 10, (3, 3))  
B = np.random.randint(0, 10, (3, 3))  


print("Matriz A:")
print(A)
print("\nMatriz B:")
print(B)


C = A + B


print("\nMatriz C (A + B):")
print(C)


D = A * B


print("\nMatriz D (A * B elemento a elemento):")
print(D)


E = np.dot(A, B)  


print("\nMatriz E (A x B - produto matricial):")
print(E)
