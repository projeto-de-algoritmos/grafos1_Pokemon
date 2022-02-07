from pyvis.network import Network

# Criando o grafo
grafo = Network(height='600px', width='100%', bgcolor='#222222', font_color='white')

# Criando os nós
grafo.add_node(0, size=75, shape='circularImage', image ="https://imagens.ne10.uol.com.br/veiculos/_midias/jpg/2022/01/11/arthur_aguiar__1_-20428433.jpg", label='Arthur Aguiar', title='Idade: 32 anos<br>Ocupação: ator, cantor e compositor')
grafo.add_node(1, size=50, shape='circularImage', image ="https://s2.glbimg.com/uJPpwLUEX1gCzJiRr7SyO0Ocnrw=/640x424/top/i.glbimg.com/og/ig/infoglobo/f/original/2021/12/27/perolafaria.jpg", label='Pérola Faria', title='Idade: 30 anos<br>Ocupação: atriz <br>Como conheceu Arthur: novela Rebelde Brasil')
grafo.add_node(2, size=50, shape='circularImage', image ="https://www.estrelando.com.br/uploads/2017/08/21/lua-blanco-1503329547.jpg", label='Lua Blanco', title='Idade: 34 anos<br>Ocupação: atriz <br>Como conheceu Arthur: novela Rebelde Brasil')
grafo.add_node(3, size=50, shape='circularImage', image ="https://s2.glbimg.com/v5YO8_UeEFsW98KvvoYB4HFDTmE=/620x466/e.glbimg.com/og/ed/f/original/2020/03/25/alice-wegmann.jpg", label='Alice Wegmann', title='Idade: 26 anos<br>Ocupação: atriz <br>Como conheceu Arthur: ambos sensações teen')
grafo.add_node(4, size=50, shape='circularImage', image ="https://uploads.metropoles.com/wp-content/uploads/2021/09/10135651/DSC8550-600x400.jpg", label='Giovanna Lancelotti', title='Idade: 28 anos<br>Ocupação: atriz <br>Como conheceu Arthur: bastidores da rede Globo')
grafo.add_node(5, size=50, shape='circularImage', image ="https://static1.purepeople.com.br/articles/4/32/21/64/@/3632703-bruna-marquezine-reage-a-comentarios-mac-amp_fixed_height_big-3.jpg", label='Bruna Marquezine', title='Idade: 26 anos<br>Ocupação: atriz <br>Como conheceu Arthur: novela Em Família')

# Criando as arestas
grafo.add_edge(0, 1)
grafo.add_edge(0, 2)
grafo.add_edge(0, 3)
grafo.add_edge(0, 4)
grafo.add_edge(0, 5)

# Mostrar botões para ajuste da visualização
grafo.show_buttons(filter_ = ['configure','layout','interaction','physics','edges'])

# Gerar arquivo .html e abrí-lo no navegador
grafo.show('trairagem.html')