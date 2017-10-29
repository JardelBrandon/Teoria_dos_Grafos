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

class informarGrafo:

    def __init__(self):
        pass

    def receberVertices(self):
        self.entradaVertices = input("Digite os vértices do grafo\nDevem seguir o seguinte formato -> J, C, E, P, M, T, Z, ... :\n")
        self.listaVertices = self.tratamentoVertices(self.entradaVertices)
        return self.listaVertices

    def tratamentoVertices(self, vertices):
        self.vertices = vertices.replace(' ', '')
        self.vertices = vertices.split(',')
        print(self.vertices)
        return self.vertices

    def receberArestas(self):
        self.entradaArestas = input("Digite as arestas do grafo\nDevem seguir o seguinte formato -> a1(J-C), a2(C-E), a3(C-E), ... :\n")
        self.listaArestas = self.tratamentoArestas(self.entradaArestas)
        self.dicionarioArestas = self.criarDicionarioArestas(self.listaArestas)
        return self.dicionarioArestas

    def tratamentoArestas(self, arestas):
        self.ultimoParenteses = (arestas.count('(') - 1)
        self.arestas = arestas.replace(')', '(', self.ultimoParenteses)
        self.arestas = arestas.replace(')', '')
        self.arestas = arestas.replace(',', '')
        #print(self.arestas)
        self.arestas = arestas.replace(' ', '')
        self.arestas = arestas.split('(')
        return self.arestas

    def criarDicionarioArestas(self, listaArestas):
        self.dicionarioArestas = dict()
        for nome_ligacao in range(0, (len(listaArestas) - 1), 2):
            self.dicionarioArestas[listaArestas[nome_ligacao]] = listaArestas[(nome_ligacao + 1)]
        return self.dicionarioArestas

    def receberGrafo(self):
        self.grafoInformado = Grafo(self.receberVertices(), self.receberArestas())
        '''
        while(True):
            try:
                self.grafoInformado = Grafo(self.receberVertices(), self.receberArestas())
                return self.grafoInformado
                break
            except:
                print("O grafo informado apresenta algum erro de entrada.\n"
                        "Por favor, atente-se para seguir o seguinte padrão:\n"
                        "Vertices -> J, C, E, P, M, T, Z, ...\n"
                        "Arestas -> a1(J-C), a2(C-E), a3(C-E), ...")
        '''

    def imprimirGrafo(self, grafo):
        print(grafo)
