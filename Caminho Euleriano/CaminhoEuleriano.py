from Questao3 import *

grafo = menuSelecaoGrafo()
imprimirInformacoesDoGrafo(grafo)

def caminhoEuleriano(self):
    grafoEuleriano = False
    if encontrarSeGrafoEstaConexo(self):
        totalVerticesGrauImpar = 0
        for grauDoVertice in self.dicionarioGrauDosVertices.values():
            if grauDoVertice % 2 != 0:
                totalVerticesGrauImpar += 1

        if totalVerticesGrauImpar < 3:
            grafoEuleriano = True

    if grafoEuleriano:
        print("*******************************************************************************************************")
        print("Existe um caminho Euleriano")
        print("*******************************************************************************************************")
    else:
        print("*******************************************************************************************************")
        print("Não existe caminho Euleriano")
        print("*******************************************************************************************************")

caminhoEuleriano(grafo)
