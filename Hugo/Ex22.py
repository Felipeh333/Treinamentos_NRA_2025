import matplotlib.pyplot as plt
import numpy as np

x = np.random.uniform(-10, 10, 100)
y = 3/2*np.cos(2*np.pi*x)

plt.title('Gráfico da função')
plt.xlabel('x')
plt.ylabel('y(x)')
plt.grid(True)
plt.plot(x, y, label = '(3/2)*cos(2pix)')
plt.legend()
plt.show()

