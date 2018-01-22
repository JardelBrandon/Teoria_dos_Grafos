from Questao3 import *

grafo = menuSelecaoGrafo()
imprimirInformacoesDoGrafo(grafo)

def caminhoEuleriano(self):
    totalVerticesGrauImpar = 0
    for listaDeVerticesAdjacentes in range(1, len(self.matrizAdjacentes), 2):
        grauDoVertice = len(self.matrizAdjacentes[listaDeVerticesAdjacentes])
        if grauDoVertice % 2 != 0:
            totalVerticesGrauImpar += 1

    if totalVerticesGrauImpar > 2:
        print("*******************************************************************************************************")
        print("Não existe caminho Euleriano")
        print("*******************************************************************************************************")

    else:
        print("*******************************************************************************************************")
        print("Existe um caminho Euleriano")
        print("*******************************************************************************************************")

caminhoEuleriano(grafo)
