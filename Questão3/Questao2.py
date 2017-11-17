'''
Roteiro 1

No exemplo acima, os vértices representam cidades e as arestas indicam se é possível chegar a outra cidade por uma estrada.
Dessa forma, esse grafo pode ser escrito da seguinte forma:
N = {J, C, E, P, M, T, Z}
A = {a1, a2, a3, a4, a5, a6, a7, a8, a9}
g(a1) = JC, g(a2) = CE, g(a3) = CE, g(a4) = CP, g(a5) = CP, g(a6) = CM, g(a7) = CT, g(a8) = MT, g(a9) = TZ

Questão 2

Faça uma programa que receba uma grafo a partir da entrada padrão e o imprima na saída padrão.
O formato de entrada é o seguinte:
a) A primeira linha contém todos os vértices, separados por vírgula e espaço. Ex.:
	J, C, E, P, M, T, Z

b) Os vértices não podem incluir os caracteres “-”, “(“, “)” e “ “

c) A segunda linha contém os nomes das arestas seguido dos vértices que ela conecta. Siga o seguinte formato:
 a1(J-C), a2(C-E), a3(C-E), ...

d) O nome de cada vértice pode ter um tamanho arbitrário de caracteres

e) O programa deve funcionar para qualquer grafo informado pelo usuário

f) Você deve tratar problemas com a formatação da entrada

'''

from grafo import Grafo

def receberVertices():
    entradaVertices = input("Digite os vértices do grafo\nDevem seguir o seguinte formato -> J, C, E, P, M, T, Z, ... :\n")
    listaVertices = tratamentoVertices(entradaVertices)
    return listaVertices

def tratamentoVertices(vertices):
    vertices = vertices.replace(' ', '')
    vertices = vertices.split(',')
    return vertices

def receberArestas():
    entradaArestas = input("Digite as arestas do grafo\nDevem seguir o seguinte formato -> a1(J-C), a2(C-E), a3(C-E), ... :\n")
    listaArestas = tratamentoArestas(entradaArestas)
    dicionarioArestas = criarDicionarioArestas(listaArestas)
    return dicionarioArestas

def tratamentoArestas(arestas):
    ultimoParenteses = (arestas.count('(') - 1)
    arestas = arestas.replace(')', '(', ultimoParenteses)
    arestas = arestas.replace(')', '')
    arestas = arestas.replace(',', '')
    arestas = arestas.replace(' ', '')
    arestas = arestas.split('(')
    return arestas

def criarDicionarioArestas(listaArestas):
    dicionarioArestas = dict()
    for nome_ligacao in range(0, (len(listaArestas) - 1), 2):
        dicionarioArestas[listaArestas[nome_ligacao]] = listaArestas[(nome_ligacao + 1)]
    return dicionarioArestas

def receberGrafo():
    while(True):
        try:
            grafoInformado = Grafo(receberVertices(), receberArestas())
            break
        except:
            print("O grafo informado apresenta algum erro de entrada.\n"
                    "Por favor, atente-se para seguir o seguinte padrão:\n"
                    "Vertices -> J, C, E, P, M, T, Z, ...\n"
                    "Arestas -> a1(J-C), a2(C-E), a3(C-E), ...")
    return grafoInformado
    #print(grafoInformado)
