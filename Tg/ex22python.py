import matplotlib.pyplot as plt 
import numpy as np 


x = np.linspace(-10, 10, 100)
a = np.random.randint(-5, 5)   
b = np.random.randint(-10, 10)  
y = a * x + b 

plt.title ('Gráfico de Dispersão com Dados Aleatórios', fontsize=14)
plt.xlabel ('Eixo X - Valores aleatórios', fontsize=12)
plt.ylabel ('Eixo Y - Valores aleatórios', fontsize=12)
plt.grid(True)
plt.plot(x,y, 'o', label ='Python SEMEAR 025')
plt.legend ()

plt.show()