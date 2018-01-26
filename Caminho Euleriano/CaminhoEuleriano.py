from Questao3 import *

grafo = menuSelecaoGrafo()
imprimirInformacoesDoGrafo(grafo)

def caminhoEuleriano(self):
    if self.grafoDirecionado:
        if encontrarSeGrafoEstaConexo(self):
            #Verifica se o grafo direcionado é balanceado
            if (sum(self.dicionarioGrauDeEntradaDosVertices.values()) == sum(self.dicionarioGrauDeSaidaDosVertices.values())):
                print("*******************************************************************************************************")
                print("Existe caminho Euleriano")
                print("*******************************************************************************************************")

            else:
                print("*******************************************************************************************************")
                print("Não existe caminho Euleriano")
                print("*******************************************************************************************************")

        else:
            print("*******************************************************************************************************")
            print("Não existe caminho Euleriano")
            print("*******************************************************************************************************")

    else:
        if encontrarSeGrafoEstaConexo(self):
            totalVerticesGrauImpar = 0
            for grauDoVertice in self.dicionarioGrauDosVertices.values():
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
        else:
            print("*******************************************************************************************************")
            print("Não existe caminho Euleriano")
            print("*******************************************************************************************************")
caminhoEuleriano(grafo)
