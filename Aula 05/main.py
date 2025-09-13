import numpy as np
from scipy.stats import *

data = np.array([7, 3, 6, 13, 10, 6, 8, 5, 3, 14])
print(f"Conjunto de dados: {data}")

print("")
# Fazendo a mediana
mediana = np.median(data)
print(f"Mediana: {mediana}")

# Média harmônica
media_harmonica = hmean(data)
print(f"Média harmônica: {media_harmonica:.2f}")

#Média geométrica
media_geometrica= gmean(np.mean(data))
print(f"Média geométrica: {media_geometrica:.2f}")

print("")
