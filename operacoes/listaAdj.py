import numpy as np

#cria a lista de adjacência a partir de uma matriz
#o modelo utilizado é uma lista de adjacência em formato de dicionário
def listaAdjacencia(matriz):
    qtdVertice = np.shape(matriz)[0]
    listAdj = {}
    for i in range (0, qtdVertice):
        adjacentes = []
        for j in range (0, qtdVertice):
            contArestas = matriz[i][j]
            if contArestas > 0:
                for k in range (0, contArestas):
                    adjacentes.append(j)
        listAdj[i] = adjacentes
    print (listAdj)
    return listAdj

def verificaAdjacenciaLista(listaAdj, vi, vj):
    saida = False
    #verifica se o vertice vj esta no vertice vi 
    if vj in listaAdj[vi]:
        saida = True
    print (saida)
    return saida

def calcDensidadeLista(listaAdj):
    qtdVertice = 0
    arestas = 0
    for i in listaAdj:
        qtdVertice = qtdVertice + 1
        for j in listaAdj[i]:
            if i in listaAdj[j]:
                arestas = arestas + 1
    arestas = arestas/2
    densidade  =  2*arestas/(qtdVertice*(qtdVertice - 1))
    print(float(round (densidade, 3)) )
    return float(round (densidade, 3)) 

def insereArestaLista(listaAdj, vi, vj):
    #adicionando os vertices na lista
    if vi in listaAdj:
        listaAdj[vi].append(vj)
    else:
        listaAdj[vi] = [vj]
    if vj in listaAdj:
        listaAdj[vj].append(vi)
    else:
        listaAdj[vj] = [vi]
    
    #colocando os vertices em ordem crescente 
    for x in listaAdj:
        listaAdj[x].sort()
    print (listaAdj)
    return listaAdj

def insereVerticeLista (listaAdj):
    qtdVertice = 0
    adjacente = []
    for i in listaAdj:
        qtdVertice = qtdVertice + 1
    #adiciona um vertice sem arestas na lista
    listaAdj[qtdVertice] = adjacente
    print (listaAdj)
    return listaAdj

def removeArestaLista(listaAdj, vi, vj):
    #verifica se os vertices estã na lista 
    if vi in listaAdj:
        listaAdj[vi].remove(vj)
    if vj in listaAdj:
        listaAdj[vj].remove(vi)
    print (listaAdj)
    return listaAdj
        
def removeVerticeLista(listaAdj, vi):
    listaAdj.pop(vi)

    #removendo as arestas que o vertice possui ligação 
    if vi in listaAdj:
        for i in listaAdj:
            if vi in listaAdj[i]:
                while vi in listaAdj[i]:
                    listaAdj[i].remove(vi)
    print(listaAdj)
    return listaAdj

#0 – simples; 1 – dígrafo; 20 – multigrafo; 21 – multigrafo dirigido; 30 – pseudografo; 31 – pseudografo dirigido
def tipoGrafoLista(listaAdj):
    simples = True
    dirigido = False
    multigrafo = False
    pseudografo = False

    #verificando ligações entre os vertices 
    for vi in listaAdj:
        if len(listaAdj[vi]) != len(set(listaAdj[vi])):
            multigrafo = True
            simples = False
        for vj in listaAdj[vi]:
            if vi not in listaAdj[vi]:
                dirigido = True
                simples = False
            if vi == vj:
                pseudografo = True
                simples = False

    if pseudografo and dirigido:
        tipo = 31
    elif pseudografo:
        tipo = 30
    elif multigrafo and dirigido:
        tipo = 21
    elif multigrafo:
        tipo = 20
    elif dirigido:
        tipo = 1
    else:
        tipo = 0

    for i in listaAdj:
        if len(listaAdj[i]) != len(set(listaAdj[i])):
            tipo = '2' + tipo
        for j in listaAdj[i]:
             if i == j:
                 tipo = '3' + tipo
    
    print (tipo)
                
   
  