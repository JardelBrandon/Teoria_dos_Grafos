'''
Roteiro 1

No exemplo acima, os vértices representam cidades e as arestas indicam se é possível chegar a outra cidade por uma estrada.
Dessa forma, esse grafo pode ser escrito da seguinte forma:
N = {J, C, E, P, M, T, Z}
A = {a1, a2, a3, a4, a5, a6, a7, a8, a9}
g(a1) = JC, g(a2) = CE, g(a3) = CE, g(a4) = CP, g(a5) = CP, g(a6) = CM, g(a7) = CT, g(a8) = MT, g(a9) = TZ

1. Construa o grafo da Paraíba usando o módulo grafo.py disponibilizado aqui e o imprima na saída padrão.
Use import para incluir grafo.py em seu próprio módulo:

from grafo import Grafo

obs.: Você não deve fazer quaisquer modificações em grafo.py

'''
from grafo import Grafo


vertices = ['J', 'C', 'E', 'P', 'M', 'T', 'Z']
arestas = {"g(a1)": "J-C", "g(a2)": "C-E", "g(a3)": "C-E",
           "g(a4)": "C-P", "g(a5)": "C-P", "g(a6)": "C-M",
           "g(a7)": "C-T", "g(a8)": "M-T", "g(a9)": "T-Z"}

grafo_Paraiba = Grafo(vertices, arestas)
print(grafo_Paraiba)
