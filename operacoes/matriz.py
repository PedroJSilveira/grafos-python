import numpy as np

#0 – simples; 1 – dígrafo; 20 – multigrafo; 21 – multigrafo dirigido; 30 – pseudografo; 31 – pseudografo dirigido
def tipografo(matriz):
    arestaMultipla = False
    laco = False
    vertice = len(matriz)
    for i in range(vertice):
        for j in range (vertice):
            #verifica se existe arestas multiplas
            if matriz[i][j] > 1:
                arestaMultipla = True
            #verifica se existe laços
            if matriz[i][j] > 1 and i == j:
                laco = True
    #verifica se a matriz transposta é igual a matriz
    if (np.transpose(matriz) == matriz).all():
        dirigido = False
    else:
        dirigido = True
    
    if dirigido and arestaMultipla and laco:
        tipo = 31
    elif dirigido and arestaMultipla:
        tipo = 21
    elif dirigido:
        tipo = 1
    elif laco:
        tipo = 30
    elif arestaMultipla:
        tipo = 20
    else:
        tipo = 0      

    print(tipo)      
    return tipo

def verificaAdjacencia(matriz, vi, vj):
    mat = np.array(matriz)
    saida = False
    #verifica se possui aresta, caso possua é adjacente
    if mat[vi][vj] > 0:
        saida = True

    print(saida)
    return saida

def calcDensidade(matriz):
    mat = np.array(matriz)
    vertice = 0
    arestas = 0
    for linha in mat:
        vertice = vertice + 1
    for i in range(vertice):
        for j in range(vertice):
            arestas = arestas + mat[i][j]
    densidade  =  2*arestas/(vertice*(vertice - 1))
    print(float(round (densidade, 3)) )
    return float(round (densidade, 3))    

def insereAresta(matriz, vi, vj):
    mat = np.array(matriz)
    mat[vi][vj] = mat[vi][vj] + 1
    print(mat)
    return mat



def removeAresta(matriz, vi, vj):
    #verifica se os dois lados da matriz tem arestas
    if matriz[vi][vj] > 0 and matriz[vj][vi] > 0:
        matriz[vi][vj] = matriz[vi][vj] - 1
        matriz[vj][vi] = matriz[vj][vi] - 1
    #verifica qual lado da matriz tem arestas
    elif matriz[vi][vj] > 0:
        matriz[vi][vj] -= 1
    elif matriz[vj][vi] > 0:
        matriz[vi][vj] -= 1
    #caso nenhum possua, as arestas continuam igual a 0
    else:
        matriz[vi][vj] = matriz[vj][vi] = 0
    print(matriz)
    return matriz

#essa função usa como ideia que se o valor do vertice for -1 ele não existe
#mas tvm esses funções na biblioteca numpy para retirar totalmente o vertice
def removeVertice(matriz, vi):
    mat = np.array(matriz)
    contlinha = 0
    for i in mat:
        contlinha = contlinha + 1

    for i in range(0, contlinha):
        mat[vi][i] = -1
        mat[i][vi] = -1

    print(mat)
    return mat
