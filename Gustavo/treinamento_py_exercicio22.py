# Autoria:Gustavo Leal Malafaia
# Data:20/05/2025
# Objetivo do progama: Teste da biblioteca matplotlib

import matplotlib.pyplot as plt
import numpy as np
import math

x = np.random.randint(1, 100, (100))

x.sort()

y = 1/x

print(x)

plt.plot(x, y)
plt.xlabel('eixo x')
plt.ylabel('eixo y')
plt.legend(['f(x) = 1/x'])
plt.grid(True)
plt.show()
