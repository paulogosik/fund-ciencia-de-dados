# import matplotlib.pyplot as plt
# import numpy as np

# # Dados
# apartamentos = [29.4, 26.8, 30.0, 37.2, 33.8, 27.7, 36.0, 26.8, 33.0, 42.6,
#                 30.4, 33.6, 28.4, 34.5, 39.3, 35.8, 43.1, 38.3, 25.3, 30.0,
#                 24.9, 38.1, 32.3, 29.1, 35.8, 27.7, 30.4, 20.0, 35.1, 42.9]

# casas_maiores = [93.0, 36.3, 44.6, 55.4, 41.3, 50.7, 54.1, 41.6, 64.4, 49.8,
#                  56.6, 50.1, 55.3, 66.5, 75.6, 68.5, 55.4, 66.9, 34.2, 53.0,
#                  65.8, 57.9, 42.1, 49.5, 53.6, 46.6, 42.2, 57.0, 43.4, 51.0]

# def plot_histogram_and_ogive(data, title, bins_method='sturges', save_prefix=None):
#     # Histograma
#     fig, ax = plt.subplots(1, 2, figsize=(12, 4))
#     counts, bins, patches = ax[0].hist(data, bins=bins_method, edgecolor='black', alpha=0.8)
#     ax[0].set_title(f'{title} - Histograma')
#     ax[0].set_xlabel('Valor')
#     ax[0].set_ylabel('Frequência')
#     ax[0].grid(axis='y', alpha=0.3)

#     # Ogiva (frequência acumulada)
#     hist_counts, hist_bins = np.histogram(data, bins=bins_method)
#     cumulative = np.cumsum(hist_counts)
#     cumulative_percent = cumulative / len(data) * 100

#     ax[1].plot(hist_bins[1:], cumulative, marker='o', linestyle='-')
#     ax[1].set_title(f'{title} - Ogiva (acumulada)')
#     ax[1].set_xlabel('Valor')
#     ax[1].set_ylabel('Frequência acumulada')
#     ax[1].grid(True)

#     # opcional: mostrar percentil na segunda escala
#     ax2 = ax[1].twinx()
#     ax2.plot(hist_bins[1:], cumulative_percent, marker='s', linestyle='--', color='orange', alpha=0.7)
#     ax2.set_ylabel('Percentual acumulado (%)')

#     plt.tight_layout()

#     if save_prefix:
#         fig.savefig(f'{save_prefix}_pair.png', dpi=300, bbox_inches='tight')

#     plt.show()

# # Gerar gráficos para os dois conjuntos
# plot_histogram_and_ogive(apartamentos, 'Apartamentos K', bins_method='sturges', save_prefix='apartamentos')
# plot_histogram_and_ogive(casas_maiores, 'Casas Maiores L', bins_method='sturges', save_prefix='casas_maiores')


# -------------------------------------------------------------------
# import matplotlib.pyplot as plt
# import numpy as np

# apartamentos = [29.4,26.8,30.0,37.2,33.8,27.7,36.0,26.8,33.0,42.6,30.4,33.6,28.4,34.5,39.3,35.8,43.1,38.3,25.3,30.0,24.9,38.1,32.3,29.1,35.8,27.7,30.4,20.0,35.1,42.9]
# casas_maiores = [93.0,36.3,44.6,55.4,41.3,50.7,54.1,41.6,64.4,49.8,56.6,50.1,55.3,66.5,75.6,68.5,55.4,66.9,34.2,53.0,65.8,57.9,42.1,49.5,53.6,46.6,42.2,57.0,43.4,51.0]

# def plot_histogram_ogive(data, title, save=None):
#     bins = np.histogram_bin_edges(data, bins='sturges')
#     counts, edges = np.histogram(data, bins=bins)
#     centers = (edges[:-1] + edges[1:]) / 2
#     cum = np.cumsum(counts)

#     fig, ax = plt.subplots(figsize=(7,4))
#     ax.bar(centers, counts, width=edges[1]-edges[0], edgecolor='black', alpha=0.7)
#     ax.set_xlabel('Valor')
#     ax.set_ylabel('Frequência')
#     ax.grid(axis='y', alpha=0.25)

#     ax2 = ax.twinx()
#     ax2.plot(centers, cum, '-o', color='C1')
#     ax2.set_ylabel('Frequência acumulada')

#     ax.set_title(title)
#     plt.tight_layout()
#     if save:
#         fig.savefig(save, dpi=300, bbox_inches='tight')
#     plt.show()

# plot_histogram_ogive(apartamentos, 'Apartamentos K - Histograma e Ogiva', save='apartamentos.png')
# plot_histogram_ogive(casas_maiores, 'Casas Maiores L - Histograma e Ogiva', save='casas_maiores.png')




# -------------------------------------------------------------------
import matplotlib.pyplot as plt
import numpy as np

apartamentos = [29.4,26.8,30.0,37.2,33.8,27.7,36.0,26.8,33.0,42.6,30.4,33.6,28.4,34.5,39.3,35.8,43.1,38.3,25.3,30.0,24.9,38.1,32.3,29.1,35.8,27.7,30.4,20.0,35.1,42.9]
casas_maiores = [93.0,36.3,44.6,55.4,41.3,50.7,54.1,41.6,64.4,49.8,56.6,50.1,55.3,66.5,75.6,68.5,55.4,66.9,34.2,53.0,65.8,57.9,42.1,49.5,53.6,46.6,42.2,57.0,43.4,51.0]

def plot_histogram(data, title, bins_method='sturges'):
    edges = np.histogram_bin_edges(data, bins=bins_method)
    plt.figure(figsize=(7,4))
    plt.hist(data, bins=edges, edgecolor='black', alpha=0.7)
    plt.title(title)
    plt.xlabel('Valor')
    plt.ylabel('Frequência')
    plt.grid(axis='y', alpha=0.25)
    plt.tight_layout()
    plt.show()
    plt.close()

def plot_ogive(data, title, bins_method='sturges'):
    counts, edges = np.histogram(data, bins=np.histogram_bin_edges(data, bins=bins_method))
    cumulative = np.cumsum(counts)
    upper_limits = edges[1:]
    plt.figure(figsize=(7,4))
    plt.step(upper_limits, cumulative, where='post', linewidth=1.5)
    plt.plot(upper_limits, cumulative, 'o', markersize=4)
    plt.title(title)
    plt.xlabel('Limite superior da classe')
    plt.ylabel('Frequência acumulada')
    ax2 = plt.twinx()
    ax2.plot(upper_limits, cumulative / len(data) * 100, '--', color='C1')
    ax2.set_ylabel('Percentual acumulado %')
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    plt.close()

plot_histogram(apartamentos, 'Apartamentos K - Histograma')
plot_ogive(apartamentos, 'Apartamentos K - Ogiva')

plot_histogram(casas_maiores, 'Casas Maiores L - Histograma')
plot_ogive(casas_maiores, 'Casas Maiores L - Ogiva')
