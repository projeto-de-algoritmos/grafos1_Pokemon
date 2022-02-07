from pyvis.network import Network
import pandas as pd
import networkx as nx

# Criando o grafo
grafo = Network(height='600px', width='100%', bgcolor='#222222', font_color='white')

# Criando os nós
grafo.add_node(0)
grafo.add_node(1)
grafo.add_node(2)
grafo.add_node(3)
grafo.add_node(4)

# Criando as arestas
grafo.add_edge(0, 1)

# Mostrar botões para ajuste da visualização
grafo.show_buttons(filter_ = ['configure','layout','interaction','physics','edges'])

# Gerar arquivo .html e abrí-lo no navegador
grafo.show('trairagem.html')