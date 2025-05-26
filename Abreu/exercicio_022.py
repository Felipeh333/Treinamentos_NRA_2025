import numpy as np
import matplotlib.pyplot as plt

x = np.random.randint(0, 100, 50)
y = 2*x

plt.title('Gráfico de função')
plt.xlabel('Eixo X')
plt.ylabel('Eixo Y')
plt.grid(True)
plt.plot(x, y, label='2*x')
plt.legend()
plt.show()
