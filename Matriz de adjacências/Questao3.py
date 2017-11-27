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
        print("a) Vertices adjacentes:\n")
        for vertice, verticesAdjacentes in zip(range(0, len(matrizVerticesAdjacentes), 2),
                                               range(1, len(matrizVerticesAdjacentes), 2)):
            print("O vertice:", matrizVerticesAdjacentes[vertice], "É adjacente aos vertices ->",
                  matrizVerticesAdjacentes[verticesAdjacentes])
        print("*******************************************************************************************************")
        # print(matrizVerticesAdjacentes)
        # print(matrizVerticesNaoAdjacentes)
        # Verificar Vertices:

    elif (tipoDeImpressaoDaMatrizDeAdjacencias == "incidentes"):
        print("*******************************************************************************************************")
        print("e) Arestas que são incidentes ao vertice:\n")
        for vertice, verticesAdjacentes in zip(range(0, len(matrizVerticesAdjacentes), 2),
                                               range(1, len(matrizVerticesAdjacentes), 2)):
            print("O vertice:", matrizVerticesAdjacentes[vertice], "Possuí arestas incidentes dos seguintes vertices ->",
                  matrizVerticesAdjacentes[verticesAdjacentes])
        print("*******************************************************************************************************")

    elif (tipoDeImpressaoDaMatrizDeAdjacencias == "naoAdjacentes"):
        # print(list(set(listaVertices).difference(set(matrizVerticesAdjacentes[1]))))
        print("*******************************************************************************************************")
        print("a) Vertices não adjacentes:\n")
        for vertice, verticesNaoAdjacentes in zip(range(0, len(matrizVerticesNaoAdjacentes), 2),
                                                  range(1, len(matrizVerticesNaoAdjacentes), 2)):
            print("O vertice:", matrizVerticesNaoAdjacentes[vertice], "Não é adjacente aos vertices ->",
                  matrizVerticesNaoAdjacentes[verticesNaoAdjacentes])
        print("*******************************************************************************************************")


#a. Encontre todos os pares de vértices não adjacentes.
def encontrarAdjacentes(self):
    #imprimirAdjacencias(self, "adjacentes")
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


    return existeArestasParalelas

#d. Qual o grau do vértice C (Faça uma função genérica para calcular o grau de qualquer vértice. Em seguida, use-a para verificar o grau do vértice C)
def encontrarGrauDoVertice(self, verticeQueDesejaObterGrauDeRetorno = None): #Se não for passado nenhum vertice como parâmetro, será impresso o grau de todos os vertices do grafo
    matrizVerticesAdjacentes = criarMatrizDeAdjacencias(self, "adjacentes")
    if (verticeQueDesejaObterGrauDeRetorno == None):
        print("*******************************************************************************************************")
        print("d) Grau dos Vertices:\n")
        for vertice, listaDeVerticesAdjacentes in zip(range(0, len(matrizVerticesAdjacentes), 2),
                                                      range(1, len(matrizVerticesAdjacentes), 2)):
            grauDoVertice = len(matrizVerticesAdjacentes[listaDeVerticesAdjacentes])

            print("Grau do Vertice :",matrizVerticesAdjacentes[vertice],"->", grauDoVertice)
        print("*******************************************************************************************************")
    else:
        posicaoDoVertice = matrizVerticesAdjacentes.index(verticeQueDesejaObterGrauDeRetorno)
        grauDoVertice = len(matrizVerticesAdjacentes[posicaoDoVertice + 1])
        print("*******************************************************************************************************")
        print("d) Grau dos Vertices:\n")
        print("Grau do Verrtice :", verticeQueDesejaObterGrauDeRetorno, "->", grauDoVertice)
        print("*******************************************************************************************************")

#e. Quais arestas incidem sobre o vértice M?
def encontrarArestasIncidentes(self, verticeQueDesejaObterAsArestasIncidentes = None): #Se não for passado nenhum vertice como parâmetro, será impresso as arestes incidentes de todos os vertices do grafo
    matrizVerticesAdjacentes = criarMatrizDeAdjacencias(self, "adjacentes")
    if (verticeQueDesejaObterAsArestasIncidentes == None):
        imprimirAdjacencias(self, "incidentes")
    else:
        posicaoDoVertice = matrizVerticesAdjacentes.index(verticeQueDesejaObterAsArestasIncidentes)
        listaDasArestasIncidentes = matrizVerticesAdjacentes[posicaoDoVertice + 1]
        print("*******************************************************************************************************")
        print("e) Arestas que são incidentes ao vertice:\n")
        print("O vertice:", verticeQueDesejaObterAsArestasIncidentes,
              "Possuí arestas incidentes dos seguintes vertices ->", listaDasArestasIncidentes)
        print("*******************************************************************************************************")

#f. Esse grafo é completo?
def encontrarSeGrafoEstaCompleto(self):
    grafoCompleto = True
    print("*******************************************************************************************************")
    print("f) O Grafo é completo?:\n")
    if (encontrarLacos(self) or encontrarArestasParalelas(self)):
        print("O grafo informado não é simples, pois possuí laço ou aresta paralela, logo não é completo")
        grafoCompleto = False

    else:
        matrizVerticesNaoAdjacentes = criarMatrizDeAdjacencias(self, "naoAdjacentes")
        for verticesNaoAdjacentes in range(1, len(matrizVerticesNaoAdjacentes), 2):
            tamanhoDaListaDosVerticesNaoAdjacentes = len(matrizVerticesNaoAdjacentes[verticesNaoAdjacentes])
            if (tamanhoDaListaDosVerticesNaoAdjacentes != 1):
                grafoCompleto = False

    if (grafoCompleto == True):
        print("O grafo informado é completo!")
        print("*******************************************************************************************************")
    else:
        print("O grafo informado não é completo!")
        print("*******************************************************************************************************")

#i. (DESAFIO) Esse grafo é conexo?
class verticeComAtributoVisita:
    def __init__(self, vertice):
        self.vertice = vertice
        self.visitado = False

def percorrerGrafoDFS(self, vertice, matrizVerticesAdjacentes): #Pesquisa em Profundidade (Depth-First Search - DFS)
    #print("Entrou")
    #print(vertice.vertice)
    '''
    posicaoDoVertice = matrizVerticesAdjacentes.index(vertice)
    print(vertice.find_by_vertice(vertice.vertice))
    '''
    for encontrarPosicao in range(0, len(matrizVerticesAdjacentes), 2):
        if vertice.vertice == matrizVerticesAdjacentes[encontrarPosicao].vertice:
            posicaoDoVertice = encontrarPosicao
            matrizVerticesAdjacentes[posicaoDoVertice].visitado = True
            break

    for arestasAdjacentes in range(0, len(matrizVerticesAdjacentes[posicaoDoVertice + 1])):
        if not(matrizVerticesAdjacentes[posicaoDoVertice + 1][arestasAdjacentes].visitado):
            '''
            print(matrizVerticesAdjacentes[posicaoDoVertice + 1][arestasAdjacentes].vertice)
            print(matrizVerticesAdjacentes[posicaoDoVertice + 1][arestasAdjacentes].visitado)
            '''
            #posicaoDoVertice = matrizVerticesAdjacentes.index(matrizVerticesAdjacentes[posicaoDoVertice + 1][arestasAdjacentes])
            matrizVerticesAdjacentes[posicaoDoVertice + 1][arestasAdjacentes].visitado = True
            percorrerGrafoDFS(self, matrizVerticesAdjacentes[posicaoDoVertice + 1][arestasAdjacentes], matrizVerticesAdjacentes)




def encontrarSeGrafoEstaConexo(self):
    grafoConexo = True
    matrizVerticesAdjacentes = criarMatrizDeAdjacencias(self, "adjacentes")
    #print(matrizVerticesAdjacentes)
    # Criar o objeto verticeComAtributoVisita marcando todos como não visitados
    for vertice, listaDeVerticesAdjacentes in zip(range(0, len(matrizVerticesAdjacentes), 2),
                                                  range(1, len(matrizVerticesAdjacentes), 2)):
        matrizVerticesAdjacentes[vertice] = verticeComAtributoVisita(matrizVerticesAdjacentes[vertice])
        #print(matrizVerticesAdjacentes[vertice].vertice)
        for arestasAdjacentes in range(0, len(matrizVerticesAdjacentes[listaDeVerticesAdjacentes])):
            matrizVerticesAdjacentes[listaDeVerticesAdjacentes][arestasAdjacentes] = verticeComAtributoVisita(matrizVerticesAdjacentes[listaDeVerticesAdjacentes][arestasAdjacentes])
            #print(matrizVerticesAdjacentes[listaDeVerticesAdjacentes][arestasAdjacentes].vertice, end=' ')
        #print()

    #print(matrizVerticesAdjacentes)
    percorrerGrafoDFS(self, matrizVerticesAdjacentes[0], matrizVerticesAdjacentes)


    for vertice in range(0, len(matrizVerticesAdjacentes), 2):
        '''
        print(matrizVerticesAdjacentes[vertice].vertice)
        print(matrizVerticesAdjacentes[vertice].visitado)
        '''
        if not(matrizVerticesAdjacentes[vertice].visitado):
            grafoConexo = False

    return grafoConexo




def imprimirInformacoesDoGrafo(self):
    print("Imprimindo as informações pertinentes ao grafo informado:")
    print("*******************************************************************************************************")
    print("Impressão dos vertices do grafo e na linha abaixo seus vertices adjacentes ligados por uma aresta (-): \n")
    print(self)
    print("*******************************************************************************************************")

    encontrarAdjacentes(self) #Invocando a função que resolve a letra a da 3 questão
    print("*******************************************************************************************************")
    print("b) Existe algum vértice adjacente a ele mesmo?:\n")
    print(encontrarLacos(self),
          "\n*******************************************************************************************************") #Invocando a função que resolve a letra b da 3 questão

    print("*******************************************************************************************************")
    print("c) Há arestas paralelas?:\n")
    print(encontrarArestasParalelas(self),
          "\n*******************************************************************************************************") #Invocando a função que resolve a letra c da 3 questão

    encontrarGrauDoVertice(self) #Invocando a função que resolve a letra d da 3 questão Obs: Laço é contado como duas incidência

    encontrarArestasIncidentes(self) #Invocando a função que resolve a letra e da 3 questão

    encontrarSeGrafoEstaCompleto(self) #Invocando a função que resolve a letra f da 3 questão

    print("*******************************************************************************************************")
    print("1) O grafo é conexo?:\n")
    print(encontrarSeGrafoEstaConexo(self),
          "\n*******************************************************************************************************") #Invocando a função que resolve a letra i da 3 questão

def menuSelecaoGrafo():
    while True:
        print("Se deseja informar um grafo; Digite -> 0\nOu se deseja usar um grafo presente na base de dados; Digite -> 1: ")
        selecaoDoGrafo = input()
        if selecaoDoGrafo == '0':
            grafo = receberGrafo()
            break
        elif selecaoDoGrafo == '1':
            while True:
                print("Se deseja utilizar um grafo básico da Paraíba; Digite -> 0\n"
                      "Ou se deseja utilizar um grafo completo; Digite -> 1\n"
                      "Ou se deseja utilizar um grafo com laço; Digite -> 2\n"
                      "Ou se deseja utilizar um grafo conexo; Digite -> 3\n"
                      "Ou se deseja utilizar um grafo desconexo; Digite -> 4\n"
                      "Ou se deseja utilizar um grafo simples; Digite -> 5\n"
                      "Ou se deseja utilizar um grafo com arestas paralelas; Digite -> 6\n"
                      "Ou se deseja voltar ao menu de seleção anterior; Digite ->7")
                tipoDoGrafo = input()
                if tipoDoGrafo == '0':
                    # Grafo básico da Paraíba
                    vertices = ['J', 'C', 'E', 'P', 'M', 'T', 'Z']
                    arestas = {"g(a1)": "J-C", "g(a2)": "C-E", "g(a3)": "C-E",
                               "g(a4)": "C-P", "g(a5)": "C-P", "g(a6)": "C-M",
                               "g(a7)": "C-T", "g(a8)": "M-T", "g(a9)": "T-Z"}
                    break
                elif tipoDoGrafo == '1':
                    #Grafo simples e Completo
                    vertices = ['J', 'C', 'E']
                    arestas = {"g(a1)": "J-C", "g(a2)": "J-E", "g(a3)": "C-E"}
                    break

                elif tipoDoGrafo == '2':
                    #Grafo com laço
                    vertices = ['J', 'C', 'E', 'P', 'M', 'T', 'Z']
                    arestas = {"g(a1)": "J-C", "g(a2)": "C-E", "g(3)": "C-C", "g(a4)": "J-J",
                                                "g(a5)": "J-J", "g(a6)": "C-C", "g(a7)": "J-J"}
                    break

                elif tipoDoGrafo == '3':
                    #Grafo Conexo
                    vertices = ['J', 'C', 'E', 'P', 'M', 'T', 'Z']
                    arestas = {"g(a1)": "J-C", "g(a2)": "C-E", "g(a3)": "E-P",
                                "g(a4)": "P-M", "g(a5)": "M-T", "g(a6)": "T-Z"}
                    break
                elif tipoDoGrafo == '4':
                    #Grafo Desconexo
                    vertices = ['J', 'C', 'E', 'P', 'M', 'T', 'Z', 'A', 'B']
                    arestas = {"g(a1)": "J-C", "g(a2)": "C-E", "g(a3)": "E-P",
                                "g(a4)": "M-T", "g(a5)": "T-Z","g(a6)": "A-B"}
                    break

                elif tipoDoGrafo == '5':
                    #Grafo simples
                    vertices = ['J', 'C', 'E']
                    arestas = {"g(a1)": "J-C", "g(a2)": "J-E"}
                    break

                elif tipoDoGrafo == '6':
                    #Grafo com arestas paralelas
                    vertices = ['J', 'C', 'E', 'P', 'M', 'T', 'Z']
                    arestas = {"g(a1)": "J-C", "g(a2)": "C-E", "g(a3)": "C-E",
                               "g(a4)": "C-P", "g(a5)": "Z-T", "g(a6)": "T-M",
                               "g(a7)": "M-T", "g(a8)": "M-T", "g(a9)": "T-Z"}
                    break
                elif tipoDoGrafo == '7':
                    break
                else:
                    print("Por farvor, digite um tipo de grafo válido!")
            if tipoDoGrafo == '7':
                continue
            else:
                grafo = Grafo(vertices, arestas)
                break
        else:
            print("Por favor, digite um valor referente a operação que deseja realizar.\n"
                  "Atente-se que os valores possíveis são 0 ou 1!")

    return grafo
'''
grafo = menuSelecaoGrafo()
imprimirInformacoesDoGrafo(grafo)
'''














