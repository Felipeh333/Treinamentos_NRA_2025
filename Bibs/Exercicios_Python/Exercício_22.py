# Desenvolvido por Beatriz Matias
# Exercício 22

import matplotlib.pyplot as plt
import numpy as np

# Segui a lógica parecida com os gráficos que o professor ensinou a fazer no MATLAB, para os relatórios

x = np.arange(1, 11) 
y1 = np.random.randint(15, 50, size=10)  
y2 = np.random.randint(5, 25, size=10)   

plt.title("Comparação de Vendas Aleatórias")
plt.xlabel("Dias")
plt.ylabel("Quantidade de Vendas")

plt.plot(x, y1, label='Vendas A', color='blue', marker='x')   
plt.plot(x, y2, label='Vendas B', color='red', marker='o')
plt.legend()

plt.grid(True)
plt.show()


