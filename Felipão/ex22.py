import matplotlib.pyplot as plt
import numpy as np

x = np.random.randint(0, 10000, size=(3))
y = np.random.randint(0, 10000, size=(3))

def desenhar_grafico(x, y):
    plt.title('Gráfico gerado aleatoriamente')
    plt.xlabel('Eixo X')
    plt.ylabel('Eixo Y')
    plt.plot(x,y)
    plt.show()

desenhar_grafico(x,y)