'''
Roteiro 1
No exemplo acima, os vértices representam cidades e as arestas indicam se é possível
chegar a outra cidade por uma estrada.
Dessa forma, esse grafo pode ser escrito da seguinte forma:
N = {J, C, E, P, M, T, Z}
A = {a1, a2, a3, a4, a5, a6, a7, a8, a9}
g(a1) = JC, g(a2) = CE, g(a3) = CE, g(a4) = CP, g(a5) = CP, g(a6) = CM, g(a7) = CT, g(a8) =
MT, g(a9) = TZ

3. Crie funções em Python para satisfazer os seguintes questionamentos:
a. Encontre todos os pares de vértices não adjacentes.
b. Há algum vértice adjacente a ele mesmo? (Retorne True ou False)
c. Há arestas paralelas? (Retorne True ou False)
d. Qual o grau do vértice C (Faça uma função genérica para calcular o grau de
qualquer vértice. Em seguida, use-a para verificar o grau do vértice C)
e. Quais arestas incidem sobre o vértice M?
f. Esse grafo é completo?
g. (DESAFIO) Encontre um ciclo, se houver (Retorne a sequência de vértices e
arestas do ciclo ou False se não houver ciclo)
h. (DESAFIO) Encontre um caminho de comprimento 4, se houver (Faça uma
função genérica que encontre um caminho de tamanho arbitrário)
i. (DESAFIO) Esse grafo é conexo?
'''

from grafo import Grafo
from Questao2 import *


'''
def escolherGrafo():
    while(True):
        grafo = receberGrafo()
        print(grafo)
'''

'''
grafo = receberGrafo()
#print(grafo)
'''
vertices = ['J', 'C', 'E', 'P', 'M', 'T', 'Z']
arestas = {"g(a1)": "J-C", "g(a2)": "C-E", "g(a3)": "C-E",
           "g(a4)": "C-P", "g(a5)": "C-P", "g(a6)": "C-M",
           "g(a7)": "C-T", "g(a8)": "M-T", "g(a9)": "T-Z"}

grafo_Paraiba = Grafo(vertices, arestas)
#print(grafo_Paraiba)

def criarListaVertices(self):
    #Adicionando os vertices em forma de String
    grafoVerticesString = ''

    for v in range(len(self.N)):
        grafoVerticesString += self.N[v]
        if v < (len(self.N) - 1):  # Só coloca a vírgula se não for o último vértice
            grafoVerticesString += ", "

    #Criando uma lista que contém os vertices
    grafoVerticesString = grafoVerticesString.replace(" ", "")
    grafoVerticesLista = grafoVerticesString.split(",")
    return grafoVerticesLista

def criarListaArestas(self):
    #Adicionando as arestas em forma de String
    grafoArestasString = ''

    for i, a in enumerate(self.A):
        grafoArestasString += self.A[a]
        if not(i == len(self.A) - 1): # Só coloca a vírgula se não for a última aresta
            grafoArestasString += ", "

    #Criando uma lista que contém as arestas
    grafoArestasString = grafoArestasString.replace(" ", "")
    grafoArestasString = grafoArestasString.replace("-", "")
    grafoArestasLista = grafoArestasString.split(",")
    return grafoArestasLista


#a. Encontre todos os pares de vértices não adjacentes.
def encontrarAdjacentes(self):
    listaVertices = criarListaVertices(grafo_Paraiba)
    listaArestas = criarListaArestas(grafo_Paraiba)
    print(listaVertices)
    print(listaArestas)
    listaVerticesNaoAdjacentes = list()
    listaVerticesAdjacentes = list()

    for vertices in range(0, len(listaVertices)):
        print(listaArestas[vertices])
        for arestas in range(0, len(listaArestas)):
            print(listaArestas[arestas])

    #Verificar Vertices:


encontrarAdjacentes(grafo_Paraiba)















