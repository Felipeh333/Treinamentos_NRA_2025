import random
import numpy as np

a = np.random.randint(0, 10000, size=(3,3))
b = np.random.randint(0, 10000, size=(3,3))

c = a + b
print(c)

d = a*b
print(d)

e = a @ b
print(e)