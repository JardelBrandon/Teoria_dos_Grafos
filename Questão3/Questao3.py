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
#arestas = {"g(a1)": "J-C", "g(a2)": "C-E", "g(a11)": "C-C", "g(a12)": "J-J", "g(a10)": "J-J", "g(a11)": "C-C", "g(a12)": "J-J"}

arestas = {"g(a1)": "J-C", "g(a2)": "C-E", "g(a3)": "C-E",
           "g(a4)": "C-P", "g(a5)": "C-P", "g(a6)": "C-M",
           "g(a7)": "C-T", "g(a8)": "M-T", "g(a9)": "T-Z"}

grafoParaiba = Grafo(vertices, arestas)
print("*******************************************************************************************************")
print("Impressão dos vertices do grafo e na linha abaixo seus vertices adjacentes ligados por uma aresta (-): \n")
print(grafoParaiba)
print("*******************************************************************************************************")

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

def criarMatrizDeAdjacencias(self, tipoDeRetornoDaMatrizDeAdjacencia): #Pârametro passado refere-se ao tipo de retorno, se deve ser a matriz de adjacentes ou a matriz de não adjacentes
    listaVertices = criarListaVertices(self)
    listaArestas = criarListaArestas(self)
    matrizVerticesAdjacentes = list()
    matrizVerticesNaoAdjacentes = list()
    posicaoAdicionarMatriz = 1

    for vertice in range(0, len(listaVertices)):
        matrizVerticesAdjacentes.append(listaVertices[vertice])
        matrizVerticesAdjacentes.append(list())
        matrizVerticesNaoAdjacentes.append(listaVertices[vertice])
        matrizVerticesNaoAdjacentes.append(list())
        #print(listaVertices[vertice], "\n")

        for arestasAdjacentes in range(0, len(listaArestas)):
            for aresta in range(0, len(listaArestas[arestasAdjacentes])):
                #print(listaArestas[arestasAdjacentes][aresta], aresta)

                if (listaVertices[vertice] == listaArestas[arestasAdjacentes][aresta] and aresta == 0):
                    matrizVerticesAdjacentes[(posicaoAdicionarMatriz)].append(listaArestas[arestasAdjacentes][(aresta + 1)])
                    #print("entrou 0")

                elif (listaVertices[vertice] == listaArestas[arestasAdjacentes][aresta] and aresta == 1):
                    matrizVerticesAdjacentes[(posicaoAdicionarMatriz)].append(listaArestas[arestasAdjacentes][(aresta - 1)])
                    #print("Entrou 1")

        #Matriz de vertices não adjacentes, realiza a diferença entre o conjunto de todos vertices e o conjunto de vertices adjacentes,
        #o resultado da diferença são os vertices não adjacentes
        #print()
        matrizVerticesNaoAdjacentes[posicaoAdicionarMatriz] = (list(set(listaVertices).difference(matrizVerticesAdjacentes[posicaoAdicionarMatriz])))
        posicaoAdicionarMatriz += 2

    '''
    # Se existir um laço, o vertice do laço só será adicionado uma vez por ocorrência
    for vertice, listaDeVerticesAdjacentes in zip(range(0, len(matrizVerticesAdjacentes), 2),
                                           range(1, len(matrizVerticesAdjacentes), 2)):
        for verticeAdjacentes in matrizVerticesAdjacentes[listaDeVerticesAdjacentes]:
            if (matrizVerticesAdjacentes[vertice] == verticeAdjacentes):
                matrizVerticesAdjacentes[listaDeVerticesAdjacentes].remove(matrizVerticesAdjacentes[vertice])
    '''

    if (tipoDeRetornoDaMatrizDeAdjacencia == "adjacentes"):
        return matrizVerticesAdjacentes
    elif (tipoDeRetornoDaMatrizDeAdjacencia == "naoAdjacentes"):
        return matrizVerticesNaoAdjacentes

def imprimirAdjacencias(self, tipoDeImpressaoDaMatrizDeAdjacencias):
    matrizVerticesNaoAdjacentes = criarMatrizDeAdjacencias(self, "naoAdjacentes")
    matrizVerticesAdjacentes = criarMatrizDeAdjacencias(self, "adjacentes")

    if (tipoDeImpressaoDaMatrizDeAdjacencias == "adjacentes"):
        print("*******************************************************************************************************")
        print("Vertices adjacentes:\n")
        for vertice, verticesAdjacentes in zip(range(0, len(matrizVerticesAdjacentes), 2),
                                               range(1, len(matrizVerticesAdjacentes), 2)):
            print("O vertice:", matrizVerticesAdjacentes[vertice], "É adjacente aos vertices ->",
                  matrizVerticesAdjacentes[verticesAdjacentes])
        print("*******************************************************************************************************")
        # print(matrizVerticesAdjacentes)
        # print(matrizVerticesNaoAdjacentes)
        # Verificar Vertices:

    elif (tipoDeImpressaoDaMatrizDeAdjacencias == "naoAdjacentes"):
        # print(list(set(listaVertices).difference(set(matrizVerticesAdjacentes[1]))))
        print("*******************************************************************************************************")
        print("Vertices não adjacentes:\n")
        for vertice, verticesNaoAdjacentes in zip(range(0, len(matrizVerticesNaoAdjacentes), 2),
                                                  range(1, len(matrizVerticesNaoAdjacentes), 2)):
            print("O vertice:", matrizVerticesNaoAdjacentes[vertice], "Não é adjacente aos vertices ->",
                  matrizVerticesNaoAdjacentes[verticesNaoAdjacentes])
        print("*******************************************************************************************************")


#a. Encontre todos os pares de vértices não adjacentes.
def encontrarAdjacentes(self):
    imprimirAdjacencias(self, "adjacentes")
    imprimirAdjacencias(self, "naoAdjacentes")


#b. b. Há algum vértice adjacente a ele mesmo? (Retorne True ou False)
def encontrarLacos(self):
    existeLaco = False
    matrizVerticesAdjacentes = criarMatrizDeAdjacencias(self, "adjacentes")
    for vertice, listaDeVerticesAdjacentes in zip(range(0, len(matrizVerticesAdjacentes), 2),
                                                    range(1, len(matrizVerticesAdjacentes), 2)):
        for verticeAdjacentes in matrizVerticesAdjacentes[listaDeVerticesAdjacentes]:
            if (matrizVerticesAdjacentes[vertice] == verticeAdjacentes):
                existeLaco = True

    print("Existe algum vértice adjacente a ele mesmo?:")
    return existeLaco

#c. Há arestas paralelas? (Retorne True ou False)
def encontrarArestasParalelas(self):
    contadorParalelismo = 0
    existeArestasParalelas = False
    matrizVerticesAdjacentes = criarMatrizDeAdjacencias(self, "adjacentes")
    for vertice, listaDeVerticesAdjacentes in zip(range(0, len(matrizVerticesAdjacentes), 2),
                                                    range(1, len(matrizVerticesAdjacentes), 2)):
        for procurarVerticeParalelo in matrizVerticesAdjacentes[listaDeVerticesAdjacentes]:
            for verticeParaleloprocurado in matrizVerticesAdjacentes[listaDeVerticesAdjacentes]:
                if (procurarVerticeParalelo == verticeParaleloprocurado and (matrizVerticesAdjacentes[vertice] != procurarVerticeParalelo)):
                    contadorParalelismo += 1
                    if (contadorParalelismo > 1):
                        existeArestasParalelas = True
            contadorParalelismo = 0

    print("Há arestas paralelas?:")
    return existeArestasParalelas

#d. Qual o grau do vértice C (Faça uma função genérica para calcular o grau de qualquer vértice. Em seguida, use-a para verificar o grau do vértice C)
def encontrarGrauDoVertice(self, verticeQueDesejaObterGrauDeRetorno = None): #Se não for passado nenhum vertice como parâmetro, será impresso o grau de todos os vertices do grafo
    matrizVerticesAdjacentes = criarMatrizDeAdjacencias(self, "adjacentes")
    if (verticeQueDesejaObterGrauDeRetorno == None):
        for vertice, listaDeVerticesAdjacentes in zip(range(0, len(matrizVerticesAdjacentes), 2),
                                                      range(1, len(matrizVerticesAdjacentes), 2)):
            grauDoVertice = len(matrizVerticesAdjacentes[listaDeVerticesAdjacentes])
            print("Grau do Vertice :",matrizVerticesAdjacentes[vertice],"->", grauDoVertice)

    else:
        posicaoDoVertice = matrizVerticesAdjacentes.index(verticeQueDesejaObterGrauDeRetorno)
        grauDoVertice = len(matrizVerticesAdjacentes[posicaoDoVertice + 1])
        print(grauDoVertice)



encontrarAdjacentes(grafoParaiba) #Invocando a função que resolve a letra a da 3 questão
print(encontrarLacos(grafoParaiba)) #Invocando a função que resolve a letra b da 3 questão
print(encontrarArestasParalelas(grafoParaiba)) #Invocando a função que resolve a letra c da 3 questão
encontrarGrauDoVertice(grafoParaiba, "C") #Invocando a função que resolve a letra d da 3 questão Obs: Laço é contado como duas incidência
















