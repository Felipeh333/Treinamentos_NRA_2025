import matplotlib.pyplot as plt
import numpy as np

A = np.arange(50)
B = np.random.randint(0,50,50)
B.sort()

plt.plot(A, B, "-b", label="B")

plt.legend(loc="upper left")

plt.xlabel('A')
plt.ylabel('B')

plt.show()
