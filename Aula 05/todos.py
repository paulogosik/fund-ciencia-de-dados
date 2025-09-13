# Importações
import numpy as np
import pandas as pd
from scipy.optimize import minimize
from dash import dcc, html
import statsmodels.api as sm
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns
from scrapy import Selector
import dash
import spacy

# NumPy: criar um array
array = np.array([10, 20, 30, 40, 50])
print(array)

# Pandas: criar um DataFrame
df = pd.DataFrame({'Coluna1': array, 'Coluna2': array**2})


# SciPy: minimizar uma função simples
fun = lambda x: x**2 + 10
result = minimize(fun, 0)

# StatsModels: OLS
X = df['Coluna1']
X = sm.add_constant(X)
y = df['Coluna2']
model = sm.OLS(y, X).fit()

# Plotly: Gráfico interativo
fig = px.scatter(df, x="Coluna1", y="Coluna2", title="Plotly Gráfico")

# Matplotlib: Gráfico simples
plt.plot(df['Coluna1'], df['Coluna2'])
plt.title("Matplotlib Gráfico")
plt.show()

# Seaborn: Gráfico estatístico
sns.lineplot(data=df, x="Coluna1", y="Coluna2")
plt.title("Seaborn Gráfico")
plt.show()

# Scrapy: selecionar conteúdo (apenas ilustração)
html_content = "<p>Olá, ChatGPT!</p>"
selector = Selector(text=html_content)
content = selector.css('p::text').get()

# Dash: criar um app simples
app = dash.Dash(__name__)
app.layout = html.Div([
    dcc.Graph(figure=fig)
])

# SpaCy: Processamento de linguagem natural
nlp = spacy.load("en_core_web_sm")
doc = nlp("OpenAI is an organization that creates cool models like ChatGPT.")
entities = [(ent.text, ent.label_) for ent in doc.ents]

print(entities)


