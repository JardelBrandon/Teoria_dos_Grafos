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
                if (matrizAdjacentes[verticesAdjacentes] in matrizAdjacentes[listaDeVerticesAdjacentes]):
                    quantidadeDeElementosAdjacentes = matrizAdjacentes[listaDeVerticesAdjacentes].count(str(matrizAdjacentes[verticesAdjacentes]))
                    print(" ", quantidadeDeElementosAdjacentes, end=" ")
                else:
                    print(" ", 0, end=" ")
        print("\n")


imprimirInformacoesDoGrafo(grafo)
imprimirMatrizDeAdjacencias(grafo)
