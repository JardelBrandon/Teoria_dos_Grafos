class VerticeInvalidoException(Exception):
    pass

class ArestaInvalidaException(Exception):
    pass

class Grafo:

    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'

    def __init__(self, N=[], A={}):
        '''
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param N: Uma lista dos vértices (ou nodos) do grafo.
        :param V: Uma dicionário que guarda as arestas do grafo. A chave representa o nome da aresta e o valor é uma string que contém dois vértices separados por um traço.
        '''
        for v in N:
            if not(Grafo.verticeValido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

        self.N = N

        for a in A:
            if not(self.arestaValida(A[a])):
                raise ArestaInvalidaException('A aresta ' + A[a] + ' é inválida')

        self.A = A

        self.matrizAdjacentes = self.criarMatrizDeAdjacencias("adjacentes")
        self.matrizNaoAdjacentes = self.criarMatrizDeAdjacencias("naoAdjacentes")
        self.dicionarioDaMatrizDeAdjacencias = self.criarMatrizDeAdjacencias("dicionarioAdjacencias")
        self.dicionarioGrauDosVertices = dict()




    def arestaValida(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro está dentro do padrão estabelecido.
        Uma aresta é representada por um string com o formato a-b, onde:
        a é um substring de aresta que é o nome de um vértice adjacente à aresta.
        - é um caractere separador. Uma aresta só pode ter um único caractere como esse.
        b é um substring de aresta que é o nome do outro vértice adjacente à aresta.
        Além disso, uma aresta só é válida se conectar dois vértices existentes no grafo.
        :param aresta: A aresta que se quer verificar se está no formato correto.
        :return: Um valor booleano que indica se a aresta está no formato correto.
        '''

        # Não pode haver mais de um caractere separador
        if aresta.count(Grafo.SEPARADOR_ARESTA) != Grafo.QTDE_MAX_SEPARADOR:
            return False

        # Índice do elemento separador
        i_traco = aresta.index(Grafo.SEPARADOR_ARESTA)

        # O caractere separador não pode ser o primeiro ou o último caractere da aresta
        if i_traco == 0 or aresta[-1] == Grafo.SEPARADOR_ARESTA:
            return False

        if not(self.existeVertice(aresta[:i_traco])) or not(self.existeVertice(aresta[i_traco+1:])):
            return False

        return True

    @classmethod
    def verticeValido(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0

    def existeVertice(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return Grafo.verticeValido(vertice) and self.N.count(vertice) > 0

    def existeAresta(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        existe = False
        if Grafo.arestaValida(self, aresta):
            for k in self.A:
                if aresta == self.A[k]:
                    existe = True

        return existe

    def adicionaVertice(self, v):
        if self.verticeValido(v):
            self.N.append(v)
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adicionaAresta(self, nome, a):
        if self.arestaValida(a):
            self.A[nome] = a
        else:
            ArestaInvalidaException('A aresta ' + self.A[a] + ' é inválida')


    def criarListaVertices(self):
        #Adicionando os vertices em forma de String
        grafoVerticesString = ''

        for v in range(len(self.N)):
            grafoVerticesString += self.N[v]
            if v < (len(self.N) - 1):  # Só coloca a vírgula se não for o último vértice
                grafoVerticesString += ", "

        #Criando uma lista que contém os vertices
        grafoVerticesString = grafoVerticesString.replace(" ", "")
        grafoVerticesLista = grafoVerticesString.split(",")
        return grafoVerticesLista

    def criarListaArestas(self):
        #Adicionando as arestas em forma de String
        grafoArestasString = ''

        for i, a in enumerate(self.A):
            grafoArestasString += self.A[a]
            if not(i == len(self.A) - 1): # Só coloca a vírgula se não for a última aresta
                grafoArestasString += ", "

        #Criando uma lista que contém as arestas
        grafoArestasString = grafoArestasString.replace(" ", "")
        grafoArestasString = grafoArestasString.replace("-", "")
        grafoArestasLista = grafoArestasString.split(",")
        return grafoArestasLista

    def criarMatrizDeAdjacencias(self, tipoDeRetornoDaMatrizDeAdjacencia): #Pârametro passado refere-se ao tipo de retorno, se deve ser a matriz de adjacentes ou a matriz de não adjacentes
        listaVertices = self.criarListaVertices()
        listaArestas = self.criarListaArestas()
        matrizVerticesAdjacentes = list()
        matrizVerticesNaoAdjacentes = list()
        dicionarioDaMatrizDeAdjacencias = dict()
        posicaoAdicionarMatriz = 1

        for vertice in range(0, len(listaVertices)):
            matrizVerticesAdjacentes.append(listaVertices[vertice])
            matrizVerticesAdjacentes.append(list())
            matrizVerticesNaoAdjacentes.append(listaVertices[vertice])
            matrizVerticesNaoAdjacentes.append(list())
            #print(listaVertices[vertice], "\n")

            for arestasAdjacentes in range(0, len(listaArestas)):
                for aresta in range(0, len(listaArestas[arestasAdjacentes])):
                    #print(listaArestas[arestasAdjacentes][aresta], aresta)

                    if (listaVertices[vertice] == listaArestas[arestasAdjacentes][aresta] and aresta == 0):
                        matrizVerticesAdjacentes[(posicaoAdicionarMatriz)].append(listaArestas[arestasAdjacentes][(aresta + 1)])
                        #print("entrou 0")

                    if (listaVertices[vertice] == listaArestas[arestasAdjacentes][aresta] and aresta == 1):
                        matrizVerticesAdjacentes[(posicaoAdicionarMatriz)].append(listaArestas[arestasAdjacentes][(aresta - 1)])
                        #print("Entrou 1")

            #Matriz de vertices não adjacentes, realiza a diferença entre o conjunto de todos vertices e o conjunto de vertices adjacentes,
            #o resultado da diferença são os vertices não adjacentes
            #print()
            matrizVerticesNaoAdjacentes[posicaoAdicionarMatriz] = (list(set(listaVertices).difference(matrizVerticesAdjacentes[posicaoAdicionarMatriz])))
            posicaoAdicionarMatriz += 2

        '''
        # Se existir um laço, o vertice do laço só será adicionado uma vez por ocorrência
        for vertice, listaDeVerticesAdjacentes in zip(range(0, len(matrizVerticesAdjacentes), 2),
                                               range(1, len(matrizVerticesAdjacentes), 2)):
            for verticeAdjacentes in matrizVerticesAdjacentes[listaDeVerticesAdjacentes]:
                if (matrizVerticesAdjacentes[vertice] == verticeAdjacentes):
                    matrizVerticesAdjacentes[listaDeVerticesAdjacentes].remove(matrizVerticesAdjacentes[vertice])
        '''
        #Criar dicionario com os vertices e outro dicionario com os vertices e quantas ligações existem entre eles
        for vertice, listaDeVerticesAdjacentes in zip(range(0, len(matrizVerticesAdjacentes), 2),
                                            range(1, len(matrizVerticesAdjacentes), 2)):
            dicionarioDaMatrizDeAdjacencias[matrizVerticesAdjacentes[vertice]] = dict()
            for verticesAdjacentes in range(0, len(matrizVerticesAdjacentes), 2):
                if (matrizVerticesAdjacentes[verticesAdjacentes] in matrizVerticesAdjacentes[listaDeVerticesAdjacentes]):
                    quantidadeDeElementosAdjacentes = matrizVerticesAdjacentes[listaDeVerticesAdjacentes].count(str(matrizVerticesAdjacentes[verticesAdjacentes]))
                    dicionarioDaMatrizDeAdjacencias[matrizVerticesAdjacentes[vertice]][matrizVerticesAdjacentes[verticesAdjacentes]] = quantidadeDeElementosAdjacentes
                else:
                    dicionarioDaMatrizDeAdjacencias[matrizVerticesAdjacentes[vertice]][matrizVerticesAdjacentes[verticesAdjacentes]] = 0

        #Condição do menu de retorno
        if (tipoDeRetornoDaMatrizDeAdjacencia == "adjacentes"):
            return matrizVerticesAdjacentes
        elif (tipoDeRetornoDaMatrizDeAdjacencia == "naoAdjacentes"):
            return matrizVerticesNaoAdjacentes

        elif (tipoDeRetornoDaMatrizDeAdjacencia == "dicionarioAdjacencias"):
            return dicionarioDaMatrizDeAdjacencias


    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo
        '''
        grafo_str = ''
        grafo_str += "Grafo não direcionado:\n"

        for vertice in self.dicionarioDaMatrizDeAdjacencias:
            grafo_str += '  '
            grafo_str += vertice
            '''
            if v < (len(self.N) - 1):  # Só coloca a vírgula se não for o último vértice
                grafo_str += ", "
            '''
        grafo_str += '\n'

        for indeceX, vertice in enumerate(self.dicionarioDaMatrizDeAdjacencias):
            grafo_str += vertice
            #grafo_str += "\n"
            for indeceY, verticesAdjacentes in enumerate(self.dicionarioDaMatrizDeAdjacencias[vertice]):
                if indeceX <= indeceY:
                    grafo_str += " "
                    grafo_str += str(self.dicionarioDaMatrizDeAdjacencias[vertice][verticesAdjacentes])
                    grafo_str += " "
                else:
                    grafo_str += " "
                    grafo_str += "-"
                    grafo_str += " "
            grafo_str += "\n"

        return grafo_str




























