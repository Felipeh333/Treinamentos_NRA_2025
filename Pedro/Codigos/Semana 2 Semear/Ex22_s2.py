import numpy as np
import matplotlib.pyplot as plt

x_medio = 0
y_medio = 0
xy = 0
x2 =0

py = np.random.randint(0,1000,15)
px = np.random.randint(0,500,15)

for i in range (15):
    x_medio = x_medio + px[i]
    y_medio = y_medio + py[i]
    xy = xy + (px[i] * py[i])
    x2 = x2 + (px[i]* px[i]) 

x_medio = x_medio / 15
y_medio = y_medio / 15


a = (15*(xy) - (x_medio)*(y_medio))/(15*(x2) - x_medio**2)
b = y_medio - (a*x_medio)


x = np.linspace(0,500,500)
y = a*x + b

plt.title("Grafico MMQ de 15 pontos aléatorios")
plt.xlabel("Força de arrasto de um jato supersonico")
plt.ylabel("Altitude")
plt.grid(True)
plt.scatter(px, py, color= 'red', label='Pontos aleatorios')
plt.plot(x, y, label='Melhor reta', color='blue')
plt.legend()
plt.show()

