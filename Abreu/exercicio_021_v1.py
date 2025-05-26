import numpy as np
import random

a1 = []
a2 = []
a3 = []
b1 = []
b2 = []
b3 = []

for i in range(3):
    n1 = random.randint(0, 9)
    a1.append(n1)
    n2 = random.randint(0, 9)
    a2.append(n2)
    n3 = random.randint(0, 9)
    a3.append(n3)
    m1 = random.randint(0, 9)
    b1.append(m1)
    m2 = random.randint(0, 9)
    b2.append(m2)
    m3 = random.randint(0, 9)
    b3.append(m3)

a = np.array([a1, a2, a3])
b = np.array([b1, b2, b3])
c = a + b
d = a * b
e = a @ b

print(f'Matriz A: \n{a}'
      f'\nMatriz B: \n{b}'
      f'\nMatriz C: \n{c}'
      f'\nMatriz D: \n{d}'
      f'\nMatriz E: \n{e}'
      )
