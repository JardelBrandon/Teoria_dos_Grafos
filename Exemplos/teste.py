from grafo import Grafo

g = Grafo()

def erro_vertice(lista_vertice):
    lista_erros=[",","-"," "]
    for vertice in range(len(lista_vertice)):
        for erros in lista_erros:
            if erros in lista_vertice[vertice]:
                print("achou")



def adicionar_vertice(lista_vertice):
    for i in range(len(lista_vertice)):
        g.adicionaVertice(lista_vertice[i])

def adicionar_aresta(lista_arestas):
    for par in range(len(lista_arestas)):
        arg1 = lista_arestas[par][0]
        arg2 = lista_arestas[par][1]
        g.adicionaAresta(arg1,arg2)

def recebe_vertice(g) :
    lista_vertice = input("Informe a Lista de vertices:").split(",")
    if erro_vertice(lista_vertice) == False:
        print("erro")
    else:
        return lista_vertice

def recebe_aresta(g) :
    lista_arestas = input("Informe a Lista de Arestas:").split(", ")
    for i in range(len( lista_arestas )):
        lista_arestas[i] = lista_arestas[i].replace(")","")
        lista_arestas[i] = lista_arestas[i].split("(")
    return lista_arestas

lista_vertices = recebe_vertice(g)
lista_arestas = recebe_aresta(g)

try :
    adicionar_aresta(lista_arestas),adicionar_vertice(lista_vertices)

except:
    print("Erro ao adicionar Arestas ou Vertices")



