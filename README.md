
# Teia de traições

**Número da Lista**: 1 <br>
**Conteúdo da Disciplina**: Grafos 1 <br>

## Alunos
|Matrícula | Aluno |
| -- | -- |
| 14/0031634  |  Stefânia Bezerra da Silva |
| 15/0150741  |  Victor Alves Gomide |

## Sobre 
Em 2022, começou uma nova edição do reality show Big Brother Brasil, a qual um dos participantes foi muito polêmico no passado por conta de sua vida amorosa: Arthur Aguiar.

O debate entrou em questão após o jornalista Léo Dias divulgar as traições de Arthur, na época casado com Mayra Cardi.

Neste trabalho foi implementado:
- Um grafo interativo das relações e traições de Arthur Aguiar;
- Uma painel onde o usuário pode fazer ajustes na visualização do grafo;
- Uma mini biografia para cada pessoa envolvida (nó);
- Uma breve descrição para cada ligação entre as pessoas (aresta).

## Screenshots
### Grafo
![](/images/grafo.png)
### Painel
![](/images/painel.png)
### Mini Biografia
![](/images/biografia.png)
### Descrição da Ligação
![](/images/aresta.png)


## Instalação 
**Linguagem**: Python<br>
**Framework**: Não foi utilizado<br>

**Passos para a instalação**:
1) Primeiramente o usuário deverá clonar o repositório:

``
git clone https://github.com/projeto-de-algoritmos/grafos1_TeiaDeTraicoes.git
``

2) Depois do repositório clonado, você deverá instalar o Python, caso não tenha na sua máquina:

``
sudo apt-get install python3
``

3) Instalar a biblioteca que será usada:

``
pip install pyvis
``


## Uso 
Depois de instalar as dependências acima, o usuário precisará apenas compilar o código:

``
python3 main.py
``

Logo após um arquivo chamado 'trairagem.html' será aberto no navegador, mostrando o grafo e suas conexões.
