import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

top_institutions_df = pd.read_csv('C:\\Users\\admin\\Desktop\\top50_country.csv')

countries = top_institutions_df['country '].unique()  
colors = plt.cm.tab20(np.linspace(0, 1, len(countries)))
country_color_map = dict(zip(countries, colors))

G = nx.Graph()

for _, row in top_institutions_df.iterrows():
    country = row['country ']
    author = row['Author']
    G.add_node(author, color=country_color_map[country])

plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G) 
nx.draw_networkx_edges(G, pos)

for node in G.nodes(data=True):
    nx.draw_networkx_nodes(G, pos, nodelist=[node[0]], node_color=[node[1]['color']])
nx.draw_networkx_labels(G, pos)

plt.title("Network Graph of Authors Colored by Nationality of Institutions")
plt.axis('off')
plt.show()
