from Questao3 import *
import cmath

grafo = menuSelecaoGrafo()
imprimirInformacoesDoGrafo(grafo)

def dijkstra(self, verticeInicial, verticeFinal):
    pesoDoMenorCaminho = dict()
    fechado = dict()
    predecessor = dict()

    #Iniciar vertices
    for vertice in self.dicionarioDaMatrizDeAdjacenciasComPesos:
        pesoDoMenorCaminho[vertice] = cmath.inf
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

                '''
                if fechado[j] == False and pesoDoMenorCaminho[j] == pesoDoMenorCaminho[k] + self.dicionarioDaMatrizDeAdjacenciasComPesos[k]:
                    predecessor[j] = list(predecessor[j])
                    predecessor[j].append(k)
                '''

    print("Menor caminho do vertice incial, até o vetice final", verticeInicial, "->", verticeFinal)
    caminho = list()
    if predecessor[verticeFinal] != None:
        x = verticeFinal
        while x != None:
            caminho.insert(0, x)
            x = predecessor[x]

        print(caminho)
    else:
        print("Não existe um caminho entre os vertices!")




    '''
    for r in self.dicionarioDaMatrizDeAdjacenciasComPesos[w]:
        if self.dicionarioDaMatrizDeAdjacenciasComPesos[w][r][0] > 0:
            if fechado[r] == False and pesoDoMenorCaminho[r] > pesoDoMenorCaminho[w] + self.dicionarioDaMatrizDeAdjacenciasComPesos[w][r][1]:
                pesoDoMenorCaminho[r] = pesoDoMenorCaminho[w] + self.dicionarioDaMatrizDeAdjacenciasComPesos[w][r][1]
                predecessor[r] = w
    '''


inicio = input("Digite o vertice raiz da busca: ")
fim = input("Digite o vertice final que deseja obter o menor caminho: ")
dijkstra(grafo, inicio, fim)