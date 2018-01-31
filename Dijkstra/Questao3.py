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


def imprimirAdjacencias(self, tipoDeImpressaoDaMatrizDeAdjacencias):
    if tipoDeImpressaoDaMatrizDeAdjacencias == "dicionarioNaoAdjacentes":
        print("*******************************************************************************************************")
        print("a) Vertices não adjacentes:\n")
        for vertice in self.dicionarioDaMatrizDeAdjacencias:
            print("O vertice:", vertice, "Não é adjacente aos vertices ->", end=" ")
            for verticesAdjacentes in self.dicionarioDaMatrizDeAdjacencias[vertice]:
                if self.dicionarioDaMatrizDeAdjacencias[vertice][verticesAdjacentes] == 0:
                    print(verticesAdjacentes, end=" ")
            print()
        print("*******************************************************************************************************")

    elif tipoDeImpressaoDaMatrizDeAdjacencias == "dicionarioIncidentes":
        dicionarioIncidentes = dict()

        for vertice in self.dicionarioDaMatrizDeAdjacencias: # Incializar dicionario com a lista dos vertices incidentes
            dicionarioIncidentes[vertice] = list()

        for vertice in self.dicionarioDaMatrizDeAdjacencias:
            for verticesAdjacentes in self.dicionarioDaMatrizDeAdjacencias:
                #if (self.dicionarioDaMatrizDeAdjacencias[vertice][verticesAdjacentes] > 0):
                for QuantidadeDeIncidencias in range(0, self.dicionarioDaMatrizDeAdjacencias[vertice][verticesAdjacentes]):
                    dicionarioIncidentes[verticesAdjacentes].append(vertice)

        print("*******************************************************************************************************")
        print("e) Arestas que são incidentes ao vertice:\n")
        for vertice in self.dicionarioDaMatrizDeAdjacencias:
            print("O vertice:", vertice, "Possuí arestas incidentes dos seguintes vertices ->", dicionarioIncidentes[vertice])
        print("*******************************************************************************************************")


#a. Encontre todos os pares de vértices não adjacentes.
def encontrarAdjacentes(self):
    #imprimirAdjacencias(self, "adjacentes")
    #imprimirAdjacencias(self, "naoAdjacentes")
    imprimirAdjacencias(self, "dicionarioNaoAdjacentes")


#b. Há algum vértice adjacente a ele mesmo? (Retorne True ou False)
def encontrarLacos(self):
    existeLaco = False
    for vertice in self.dicionarioDaMatrizDeAdjacencias:
        if self.dicionarioDaMatrizDeAdjacencias[vertice][vertice] > 0:
            existeLaco = True
    return existeLaco

#c. Há arestas paralelas? (Retorne True ou False)
def encontrarArestasParalelas(self):
    existeArestasParalelas = False

    for vertice in self.dicionarioDaMatrizDeAdjacencias:
        for verticesAdjacencias in self.dicionarioDaMatrizDeAdjacencias[vertice]:
            ''' 
            Obs: Estou com dúvida em relação ao caso de um vertice com mais de um laço incidente a este vertice
            Se nesse caso esses laços são considerados como arestas paralelas! 
            Caso sim esta parte do código deve ser descomentada, se não a verificação desta maneira esta correta.
            if vertice == verticesAdjacencias:
                continue
            '''
            if self.dicionarioDaMatrizDeAdjacencias[vertice][verticesAdjacencias] > 1:
                existeArestasParalelas = True
                break

        if existeArestasParalelas == True:
            break

    return existeArestasParalelas

#d. Qual o grau do vértice C (Faça uma função genérica para calcular o grau de qualquer vértice. Em seguida, use-a para verificar o grau do vértice C)
def encontrarGrauDoVertice(self, verticeQueDesejaObterGrauDeRetorno = None): #Se não for passado nenhum vertice como parâmetro, será impresso o grau de todos os vertices do grafo
    grauDeEntradaDosVertices = dict()
    grauDeSaidaDosVertices = dict()

    for vertice in self.dicionarioDaMatrizDeAdjacencias: #Inicializador dos dicionarios dos graus
        grauDeSaidaDosVertices[vertice] = 0
        grauDeEntradaDosVertices[vertice] = 0

    for vertice in self.dicionarioDaMatrizDeAdjacencias:
        for verticesAdjacencias in self.dicionarioDaMatrizDeAdjacencias[vertice]:
            if (self.dicionarioDaMatrizDeAdjacencias[vertice][verticesAdjacencias] > 0):
                grauDeSaidaDosVertices[vertice] += self.dicionarioDaMatrizDeAdjacencias[vertice][verticesAdjacencias]
                grauDeEntradaDosVertices[verticesAdjacencias] += self.dicionarioDaMatrizDeAdjacencias[vertice][verticesAdjacencias]


    if verticeQueDesejaObterGrauDeRetorno == None:
        print("*******************************************************************************************************")
        print("d) Grau dos Vertices:\n")
        for vertice in self.dicionarioDaMatrizDeAdjacencias:
            print("Grau de entrada do Vertice :", vertice, "->", grauDeEntradaDosVertices[vertice])
            print("Grau de saída do Vertice :", vertice, "->", grauDeSaidaDosVertices[vertice])
        print("*******************************************************************************************************")
    else:
        print("*******************************************************************************************************")
        print("d) Grau dos Vertices:\n")
        print("Grau de entrada do Vertice :", verticeQueDesejaObterGrauDeRetorno, "->", grauDeEntradaDosVertices[verticeQueDesejaObterGrauDeRetorno])
        print("Grau de saída do Vertice :", verticeQueDesejaObterGrauDeRetorno, "->", grauDeSaidaDosVertices[verticeQueDesejaObterGrauDeRetorno])
        print("*******************************************************************************************************")

#e. Quais arestas incidem sobre o vértice M?
def encontrarArestasIncidentes(self, verticeQueDesejaObterAsArestasIncidentes = None): #Se não for passado nenhum vertice como parâmetro, será impresso as arestes incidentes de todos os vertices do grafo

    if verticeQueDesejaObterAsArestasIncidentes == None:
        imprimirAdjacencias(self, "dicionarioIncidentes")

    else:
        dicionarioIncidentes = dict()

        for vertice in self.dicionarioDaMatrizDeAdjacencias: # Incializar dicionario com a lista dos vertices incidentes
            dicionarioIncidentes[vertice] = list()

        for vertice in self.dicionarioDaMatrizDeAdjacencias:
            for verticesAdjacentes in self.dicionarioDaMatrizDeAdjacencias:
                #if (self.dicionarioDaMatrizDeAdjacencias[vertice][verticesAdjacentes] > 0):
                for QuantidadeDeIncidencias in range(0, self.dicionarioDaMatrizDeAdjacencias[vertice][verticesAdjacentes]):
                    dicionarioIncidentes[verticesAdjacentes].append(vertice)

        print("*******************************************************************************************************")
        print("e) Arestas que são incidentes ao vertice:\n")
        print("O vertice:", verticeQueDesejaObterAsArestasIncidentes,
              "Possuí arestas incidentes dos seguintes vertices ->", dicionarioIncidentes[verticeQueDesejaObterAsArestasIncidentes])
        print("*******************************************************************************************************")

#f. Esse grafo é completo?
def encontrarSeGrafoEstaCompleto(self):
    grafoCompleto = True
    print("*******************************************************************************************************")
    print("f) O Grafo é completo?:\n")
    if encontrarLacos(self) or encontrarArestasParalelas(self):
        print("O grafo informado não é simples, pois possuí laço ou aresta paralela, logo não é completo")
        grafoCompleto = False

    else:
        for vertice in self.dicionarioDaMatrizDeAdjacencias:
            for verticesAdjacencias in self.dicionarioDaMatrizDeAdjacencias[vertice]:
                if (self.dicionarioDaMatrizDeAdjacencias[vertice][verticesAdjacencias] != 1 and vertice != verticesAdjacencias):
                    grafoCompleto = False

    if grafoCompleto == True:
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

    def __repr__(self):
        verticeString = str()
        verticeString += self.vertice
        verticeString += "-"
        verticeString += str(self.visitado)

        return verticeString

def percorrerGrafoDFS(self, vertice, dicionarioDaMatrizDeVerticesAdjacencias): #Pesquisa em Profundidade (Depth-First Search - DFS)
    # Verificar qual é o vertice correspondente no dicionario ao vertice adjacente
    for proximoVertice in dicionarioDaMatrizDeVerticesAdjacencias:
        if proximoVertice.vertice == vertice.vertice:
            vertice = proximoVertice
            break

    vertice.visitado = True
    for verticesAdjacencias in dicionarioDaMatrizDeVerticesAdjacencias[vertice]:
        if dicionarioDaMatrizDeVerticesAdjacencias[vertice][verticesAdjacencias] > 0:
            if not verticesAdjacencias.visitado:
                verticesAdjacencias.visitado = True
                percorrerGrafoDFS(self, verticesAdjacencias, dicionarioDaMatrizDeVerticesAdjacencias)



def encontrarSeGrafoEstaConexo(self):
    dicionarioAdjacenciasComAtributoVisita = dict()
    # Criar o objeto verticeComAtributoVisita marcando todos como não visitados
    for vertice in self.dicionarioDaMatrizDeAdjacencias:
        dicionarioAdjacenciasComAtributoVisita[verticeComAtributoVisita(vertice)] = dict()


    for vertice, verticeComAtributo in zip(self.dicionarioDaMatrizDeAdjacencias, dicionarioAdjacenciasComAtributoVisita):
        for verticesAdjacencias in self.dicionarioDaMatrizDeAdjacencias[verticeComAtributo.vertice]:
            dicionarioAdjacenciasComAtributoVisita[verticeComAtributo][verticeComAtributoVisita(verticesAdjacencias)] = self.dicionarioDaMatrizDeAdjacencias[verticeComAtributo.vertice][verticesAdjacencias]


    #Percorrer todos os vertices do grafo para verificar se a partir de algum vertice o grafo é conexo
    for verticeComAtributo in dicionarioAdjacenciasComAtributoVisita:
        grafoConexo = True
        percorrerGrafoDFS(self, verticeComAtributo, dicionarioAdjacenciasComAtributoVisita)

        #Verificar se a partir desse vertice o grafo é conexo
        for vertice in dicionarioAdjacenciasComAtributoVisita:
            if not vertice.visitado:
                grafoConexo = False
                break

        if grafoConexo:
            break

        else: #Se o grafo não for conexo a partir desse vertice, então o grafo é zerado e um novo teste com o próximo vertice será realizado
            for verticeComAtributo in dicionarioAdjacenciasComAtributoVisita:
                verticeComAtributo.visitado = False
                for verticesAdjacencias in dicionarioAdjacenciasComAtributoVisita[verticeComAtributo]:
                    verticesAdjacencias.visitado = False


    return grafoConexo



def imprimirInformacoesDoGrafo(self):
    print(self.dicionarioDaMatrizDeAdjacencias)
    print("*******************************************************************************************************")
    print("Imprimindo as informações pertinentes ao grafo informado(Utilizando matriz de Adjacências):")
    print("*******************************************************************************************************")
    print("*******************************************************************************************************")
    print("Impressão do grafo em forma de matriz de adjacências.\n"
          "Obs: A matriz representa se existe caminho entre o vertice da linha sobre o vertice da coluna,\n"
          "Demostrando dessa maneira um par ordenado -> (quantidade de arestas que os ligam, peso da aresta): \n")
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
                    #Grafo simples e Completo direcionado
                    vertices = ['J', 'C', 'E']
                    arestas = {"g(a1)": "J-C", "g(a2)": "J-E", "g(a3)": "C-E",
                                "g(a4)": "C-J", "g(a5)": "E-J", "g(a6)": "E-C"}
                    break

                elif tipoDoGrafo == '2':
                    #Grafo com laço
                    vertices = ['J', 'C', 'E', 'P', 'M', 'T', 'Z']
                    arestas = {"g(a1)": "J-C", "g(a2)": "C-E", "g(3)": "C-C", "g(a4)": "J-J",
                                                "g(a5)": "J-J", "g(a6)": "C-C", "g(a7)": "J-J"}
                    break

                elif tipoDoGrafo == '3':
                    #Grafo fracamente Conexo
                    vertices = ['J', 'C', 'E', 'P', 'M', 'T', 'Z']
                    arestas = {"g(a1)": "J-C", "g(a2)": "C-E", "g(a3)": "E-P",
                                "g(a4)": "P-M", "g(a5)": "M-T", "g(a6)": "T-Z"}
                    break
                elif tipoDoGrafo == '4':
                    #Grafo Desconexo
                    vertices = ['J', 'C', 'E', 'P', 'M', 'T', 'Z', 'A', 'B']
                    arestas = {"g(a1)": "J-C", "g(a2)": "C-E", "g(a3)": "E-P",
                                "g(a4)": "M-T", "g(a5)": "T-Z", "g(a6)": "A-B"}
                    break

                elif tipoDoGrafo == '5':
                    #Grafo simples
                    vertices = ['J', 'C', 'E']
                    arestas = {"g(a1)": "J-C", "g(a2)": "C-E"}
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

















