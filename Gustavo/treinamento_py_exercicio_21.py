# Autoria:Gustavo Leal Malafaia
# Data:20/05/2025
# Objetivo do progama:Teste da biblioteca Numpy

import numpy as np

A = np.random.randint(0, 9, (3, 3))
B = np.random.randint(0, 9, (3, 3))

print(A)
print(B)

C = A + B

print(C)

D = A*B

print(D)

E = A@B

print(E)
