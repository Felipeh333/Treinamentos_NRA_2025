import numpy as np

A = np.random.randint(0,9,9)
A = A.reshape(3, 3)

B = np.random.randint(0,9,9)
B = B.reshape(3, 3)

C = A + B

D = A * B

E = A @ B



print (A, '\n', '\n', B, '\n', '\n', C, '\n', '\n', D, '\n', '\n', E)

