dicionario = dict()
dicionario["J"] = dict()
dicionario["J"]["C"] = 0
dicionario["J"]["M"] = 2
dicionario["J"]["J"] = 3
dicionario["B"] = dict()
dicionario["B"]["ASDFASDF"] = 10222

print(dicionario)
def percorrerDicionario(Aurelio):
    for indice, vertice in enumerate(dicionario):
        print(vertice)
        for indiceAdjacente, adjacente in enumerate(dicionario[vertice]):
            print(vertice, end=" ")
            print(adjacente, end=" ")
            print(dicionario[vertice][adjacente])


percorrerDicionario(dicionario)