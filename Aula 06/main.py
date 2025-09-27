import numpy as np
import matplotlib.pyplot as plt

dados = [15, 23, 12, 78, 45, 89, 45, 23, 56, 49, 77, 83, 12, 56, 34, 78, 90, 23, 56, 44]
#bins = [0, 20, 40, 60, 80, 100]
k = round(1 + 3.33 * np.log10(len(dados)))

hist, edges = np.histogram(dados, bins=k)

for i in range(k):
    print(f'{edges[i]} - {edges[i+1]}: {hist[i]}')

plt.hist(dados, bins=k, edgecolor='black', alpha=0.2)
plt.xlabel('Intervalos')
plt.ylabel('Frequência')
plt.title('Histograma com Intervalos')
plt.show()