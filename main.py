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
grafo.add_node(6, size=50, shape='circularImage', image ="https://i.pinimg.com/originals/bd/73/c6/bd73c6949fe65251317aa11209a5d9b0.jpg", label='Camila Mayrink', title='Idade: 28 anos<br>Ocupação: atriz<br>Como conheceu Arthur: informação desconhecida')
grafo.add_node(7, size=50, shape='circularImage', image ="https://s2.glbimg.com/2o_h82dQzdhA6WbJ3OEWPHVGdhU=/e.glbimg.com/og/ed/f/original/2020/01/23/mayiearaujo_82803437_1014005122314801_2307136361965189139_n.jpg", label='May Araújo', title='Idade: 28 anos<br>Ocupação: dançarina<br>- Como conheceu Arthur: quadro Dança dos Famosos do programa Domingão do Faustão')
grafo.add_node(8, size=50, shape='circularImage', image ="https://imgsapp2.correiobraziliense.com.br/app/noticia_127983242361/2020/07/10/871081/20200710105341922586o.jpg", label='Mayra Cardi', title='Idade: 30 anos<br>Ocupação: coach fitness<br>Como conheceu Arthur: bastidores do programa Domingão do Faustão')
grafo.add_node(9, size=50, shape='circularImage', image ="https://rd1.com.br/wp-content/uploads/2020/07/20200720-aricia-silva.jpg", label='Aricia Silva', title='Idade: 28 anos<br>Ocupação: ex-panicat<br>Como conheceu Arthur: Instagram')
grafo.add_node(10, size=50, shape='circularImage', image ="https://fernandascheer.com.br/wp-content/uploads/2018/10/AdobeStock_198332985_Preview-copy-1080x675.png", label='Carboidrato', title='Idade: 7 milhões de anos<br>Ocupação: macronutriente<br>Como conheceu Arthur: Big Brother Brasil 22')

# Criando arestas partindo do centro
grafo.add_edge(0, 1, title='Ex')
grafo.add_edge(0, 2, title='Ex')
grafo.add_edge(0, 3, title='Ex')
grafo.add_edge(0, 4, title='Ex')
grafo.add_edge(0, 5, title='Ex')
grafo.add_edge(0, 6, title='Ex')
grafo.add_edge(0, 7, title='Ex')
grafo.add_edge(0, 8, title='Esposa')
grafo.add_edge(0, 9, title='Ex')
grafo.add_edge(0, 10, title='Em um relacionamento sério')

# Criando arestas laterais
grafo.add_edge(1, 2, title='Namoro com Pérola e Lua ao mesmo tempo')
grafo.add_edge(2, 3, title='Lua traída por Alice (Alice nega!)')
grafo.add_edge(3, 4, title='Alice traída por Giovanna')
grafo.add_edge(4, 5, title='Giovanna traída por Bruna (Bruna nega!)')
grafo.add_edge(5, 6, title='Bruna traída por Camila')
grafo.add_edge(6, 7, title='Camila traída por May')
grafo.add_edge(7, 8, title='Término com Camila, casamento com Mayra')
grafo.add_edge(8, 9, title='Esposa Mayra traída por Aricia')
grafo.add_edge(8, 10, title='INIMIGOS MORTAIS')

# Definindo física da visualização dos nós
grafo.hrepulsion(node_distance=170, central_gravity=0.0, spring_length=115, spring_strength=0.075, damping=0.09)

# Mostrar botões para ajuste da visualização
grafo.show_buttons(filter_ = ['configure','layout','interaction','physics','edges'])

# Gerar arquivo .html e abrí-lo no navegador
grafo.show('trairagem.html')
