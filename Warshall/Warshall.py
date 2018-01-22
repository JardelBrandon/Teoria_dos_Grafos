from Questao3 import *

def warshall(matriz):
    cloneDaMatriz = matriz

    for i in matriz:
        for j in matriz:
            if cloneDaMatriz[j][i] > 0:
                for k in matriz:
                    cloneDaMatriz[j][k] = max(cloneDaMatriz[j][k], cloneDaMatriz[i][k])

    return cloneDaMatriz

def imprimirMatrizDeAlcancabilidadeDeWarshall(matriz):
    print("*******************************************************************************************************")
    print("Impressão da matriz de alcançabilidade obtida a partir do algoritmo de Warshall:\n")
    for vertice in matriz:
        print("  ", vertice, end="")
    print()

    for vertice, in matriz:
        print(vertice, end="")
        for verticesAdjacentes in matriz[vertice]:
                    print(" ", matriz[vertice][verticesAdjacentes], end=" ")

        print("\n")
    print("*******************************************************************************************************")

grafo = menuSelecaoGrafo()
imprimirInformacoesDoGrafo(grafo)

matrizDeAlcancabilidade = warshall(grafo.dicionaioDaMatrizDeAdjacencias)
imprimirMatrizDeAlcancabilidadeDeWarshall(matrizDeAlcancabilidade)
