from Questao3 import *
import math

grafo = menuSelecaoGrafo()
imprimirInformacoesDoGrafo(grafo)

def dijkstra(self, verticeInicial, verticeFinal):
    pesoDoMenorCaminho = dict()
    fechado = dict()
    predecessor = dict()

    #Iniciar vertices
    for vertice in self.dicionarioDaMatrizDeAdjacenciasComPesos:
        pesoDoMenorCaminho[vertice] = math.inf
        fechado[vertice] = False
        predecessor[vertice] = None

    pesoDoMenorCaminho[verticeInicial] = 0

    while False in fechado.values():
        k = min({k:v for k, v in fechado.items() if v == False}, key=pesoDoMenorCaminho.get)
        fechado[k] = True

        for j in self.dicionarioDaMatrizDeAdjacenciasComPesos[k]:
            if self.dicionarioDaMatrizDeAdjacenciasComPesos[k][j][0] > 0:
                if fechado[j] == False and pesoDoMenorCaminho[j] > pesoDoMenorCaminho[k] + self.dicionarioDaMatrizDeAdjacenciasComPesos[k][j][1]:
                    pesoDoMenorCaminho[j] = pesoDoMenorCaminho[k] + self.dicionarioDaMatrizDeAdjacenciasComPesos[k][j][1]
                    predecessor[j] = k

    print("Menor caminho do vertice incial, até o vetice final", verticeInicial, "->", verticeFinal)
    caminho = list()
    if predecessor[verticeFinal] != None:
        x = verticeFinal
        while x != None:
            caminho.insert(0, x)
            x = predecessor[x]

        print(caminho)
        print("Peso total do menor caminho: ", pesoDoMenorCaminho[verticeFinal])
    else:
        print("Não existe um caminho entre os vertices!")



inicio = input("Digite o vertice raiz da busca: ")
fim = input("Digite o vertice final que deseja obter o menor caminho: ")
dijkstra(grafo, inicio, fim)
