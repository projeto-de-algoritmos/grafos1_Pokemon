from pyvis.network import Network
#import pandas as pd
#import networkx as nx

# Criando o grafo
grafo = Network(height='600px', width='100%', bgcolor='#222222', font_color='white')

# Criando os nós
grafo.add_node(0, size=75, shape='circularImage', image ="https://imagens.ne10.uol.com.br/veiculos/_midias/jpg/2022/01/11/arthur_aguiar__1_-20428433.jpg", label='Arthur Aguiar', title='Ator')
grafo.add_node(1, size=50)
grafo.add_node(2, size=50)
grafo.add_node(3, size=50)
grafo.add_node(4, size=50)

# Criando as arestas
grafo.add_edge(0, 1)
grafo.add_edge(0, 2)
grafo.add_edge(0, 3)
grafo.add_edge(0, 4)

# Mostrar botões para ajuste da visualização
grafo.show_buttons(filter_ = ['configure','layout','interaction','physics','edges'])

# Gerar arquivo .html e abrí-lo no navegador
grafo.show('trairagem.html')