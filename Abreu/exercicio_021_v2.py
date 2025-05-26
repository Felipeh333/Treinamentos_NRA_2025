import numpy as np

a = np.random.randint(0, 9, (3, 3))
b = np.random.randint(0, 9, (3, 3))

c = a + b
d = a * b
e = a @ b

print(f'Matriz A: \n{a}'
      f'\nMatriz B: \n{b}'
      f'\nMatriz C: \n{c}'
      f'\nMatriz D: \n{d}'
      f'\nMatriz E: \n{e}'
      )
