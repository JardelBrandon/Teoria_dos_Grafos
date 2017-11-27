from Questao3 import *

grafo = menuSelecaoGrafo()

def imprimirMatrizDeAdjacencias(self):
    matrizAdjacentes = criarMatrizDeAdjacencias(self, "adjacentes")
    for vertice in range(0, len(matrizAdjacentes), 2):
        print("  ",matrizAdjacentes[vertice], end="")
    print()

    for vertice, listaDeVerticesAdjacentes in zip(range(0, len(matrizAdjacentes), 2),
                                                  range(1, len(matrizAdjacentes), 2)):
        print(matrizAdjacentes[vertice], end="")
        for verticesAdjacentes in range(0, len(matrizAdjacentes), 2):
            if verticesAdjacentes >= vertice: #Se optar por imprimir a matriz completamente(Sem os traços) tirar essa condição
                if (matrizAdjacentes[verticesAdjacentes] in matrizAdjacentes[listaDeVerticesAdjacentes]):
                    print(" ", 1, end=" ")
                else:
                    print(" ", 0, end=" ")

            else:
                print("  -", end=" ")
        print("\n")


imprimirInformacoesDoGrafo(grafo)
imprimirMatrizDeAdjacencias(grafo)
