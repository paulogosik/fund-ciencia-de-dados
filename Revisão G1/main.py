# Importando as bibliotecas necessárias
import numpy as np
from scipy.stats import hmean, gmean, mode, tstd, tvar
from collections import Counter, defaultdict
import math
import matplotlib.pyplot as plt
import stemgraphic

# --- Aula 4: Calculando e implementando ---

# Dados de exemplo para os cálculos
data = np.array([7, 3, 6, 13, 10, 6, 8, 5, 3, 14])

# Cálculo da Média Aritmética
media_aritmetica = np.mean(data)
print(f"Média Aritmética: {media_aritmetica}")

# Cálculo da Média Harmônica
media_harmonica = hmean(data)
print(f"Média Harmônica: {media_harmonica}")

# Cálculo da Média Quadrática
media_quadratica = np.sqrt(np.mean(np.square(data)))
print(f"Média Quadrática: {media_quadratica}")

# Cálculo da Média Geométrica
media_geometrica = gmean(data)
print(f"Média Geométrica: {media_geometrica}")

# Cálculo da Média Ponderada
pesos = np.array([0.2, 0.2, 0.1, 0.1, 0.1, 0.1, 0.05, 0.05, 0.05, 0.05])
media_ponderada = np.average(data, weights=pesos)
print(f"Média Ponderada: {media_ponderada}")

# Cálculo da Mediana
mediana = np.median(data)
print(f"Mediana: {mediana}")

# Cálculo da Moda usando SciPy
moda_scipy = mode(data, keepdims=True)
print(f"Moda (SciPy): {moda_scipy.mode[0]}")

# Cálculo da Moda usando collections.Counter (para casos multimodais)
conta = Counter(data)
max_freq = max(conta.values())
modas_counter = [k for k, v in conta.items() if v == max_freq]
print(f"Moda (Counter): {modas_counter}")

# Cálculo do Ponto Médio
ponto_medio = (np.min(data) + np.max(data)) / 2
print(f"Ponto Médio: {ponto_medio}")

# Cálculo da Amplitude Total
amplitude = np.ptp(data)
print(f"Amplitude Total: {amplitude}")

# Cálculo do Desvio Médio
desvio_medio = np.mean(np.abs(data - media_aritmetica))
print(f"Desvio Médio: {desvio_medio}")

# Cálculo do Desvio Padrão (populacional e amostral)
desvio_padrao_pop = tstd(data, ddof=0)
desvio_padrao_amostral = tstd(data, ddof=1)
print(f"Desvio Padrão Populacional: {desvio_padrao_pop}")
print(f"Desvio Padrão Amostral: {desvio_padrao_amostral}")

# Cálculo da Variância (populacional e amostral)
variancia_pop = tvar(data, ddof=0)
variancia_amostral = tvar(data, ddof=1)
print(f"Variância Populacional: {variancia_pop}")
print(f"Variância Amostral: {variancia_amostral}")

# Cálculo dos Quartis
quartis = np.quantile(data, [0.25, 0.5, 0.75])
print(f"Quartis (Q1, Q2, Q3): {quartis}")


# --- Aula 5: Distribuição de Frequência ---

# Dados de exemplo para a distribuição de frequência
dados_freq = [1, 3, 5, 3, 2, 3, 4, 2, 5, 5, 5, 4, 4, 4, 5, 2, 1, 1, 3]

# Cálculo da Frequência Absoluta
frequencia_absoluta = Counter(dados_freq)
print(f"Frequência Absoluta: {sorted(frequencia_absoluta.items())}")

# Cálculo da Frequência Relativa
total_dados = len(dados_freq)
frequencia_relativa = {chave: valor / total_dados for chave, valor in frequencia_absoluta.items()}
print(f"Frequência Relativa: {sorted(frequencia_relativa.items())}")

# Dados de temperatura para cálculo de classes
dados_temperatura = [
    18.9, 18.7, 18.4, 23.2, 22.3, 22.0, 22.4, 23.0,
    20.9, 18.3, 17.5, 18.0, 19.1, 18.9, 20.0, 25.1,
    21.5, 20.8, 22.4, 23.7, 18.3, 16.1, 17.2, 19.8,
    22.6, 21.2, 21.2, 20.1, 21.4, 22.2, 23.2
]

# Determinando o número de classes usando a fórmula de Sturges
n = len(dados_temperatura)
k = 1 + 3.3 * math.log10(n)
k = round(k)
print(f"Número de classes (Sturges): {k}")

# Determinando o intervalo de classe
h = round(((max(dados_temperatura) - min(dados_temperatura)) / k), 1)
print(f"Intervalo de classe (h): {h}")


# --- Aula 6: Histograma ---

# Dados para o histograma
dados_hist = [15, 23, 12, 78, 45, 89, 45, 23, 56, 49, 77, 83, 12, 56, 34, 78, 90, 23, 56, 44]

# Definindo os intervalos (bins) manualmente
bins_manual = [0, 20, 40, 60, 80, 100]

# Calculando a frequência para os intervalos definidos
hist, edges = np.histogram(dados_hist, bins=bins_manual)

# Imprimindo a frequência por intervalo
for i in range(len(bins_manual)-1):
    print(f'Intervalo {bins_manual[i]}-{bins_manual[i+1]}: {hist[i]}')

# Criando e mostrando o histograma com intervalos manuais
plt.figure() # Cria uma nova figura para o gráfico
plt.hist(dados_hist, bins=bins_manual, edgecolor='black', alpha=0.7)
plt.xlabel('Intervalos')
plt.ylabel('Frequência')
plt.title('Histograma com Intervalos Manuais')
plt.show()

# Usando a fórmula de Sturges para definir o número de bins
k_sturges = round(1 + 3.33 * np.log10(len(dados_hist)))
hist_sturges, edges_sturges = np.histogram(dados_hist, bins=k_sturges)

# Imprimindo a frequência por intervalo (Sturges)
for i in range(k_sturges):
    print(f'Intervalo {edges_sturges[i]:.2f}-{edges_sturges[i+1]:.2f}: {hist_sturges[i]}')

# Criando e mostrando o histograma com bins definidos por Sturges
plt.figure() # Cria uma nova figura para o gráfico
plt.hist(dados_hist, bins=k_sturges, edgecolor='black', alpha=0.7)
plt.xlabel('Intervalos')
plt.ylabel('Frequência')
plt.title('Histograma com Fórmula de Sturges')
plt.show()


# --- Aula 7: Outras formas de representação de dados ---

# Dados para o Diagrama Ramo-e-Folhas
dados_ramo = [23, 25, 26, 31, 32, 33, 33, 34, 35, 36, 37, 40, 41]

# Construção do Diagrama Ramo-e-Folhas usando a biblioteca stemgraphic
fig, ax = stemgraphic.stem_graphic(dados_ramo, scale=10)
plt.title("Diagrama Ramo-e-Folhas (stemgraphic)")
plt.show()

# Construção manual do Diagrama Ramo-e-Folhas
d = defaultdict(list)
for i in dados_ramo:
    caule, folha = divmod(i, 10)
    d[caule].append(folha)

print("\nDiagrama Ramo-e-Folhas (manual):")
for caule in sorted(d):
    print(caule, "|", *sorted(d[caule]))