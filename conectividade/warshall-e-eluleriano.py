import numpy as np

def warshall(matriz):
    #mostrar a matriz em que esta trabalhando
    print(matriz)
    print()
    vertice = len(matriz)
    mat = np.array(matriz)

    #criando a matriz de alcançabilidade
    for k in range(vertice):
        for i in range(vertice):
            for j in range(vertice):
                if mat[i][j] == 1 or (mat[i][k] == 1 and mat[k][j] == 1):
                    mat[i][j] = 1
               
    print(mat)
    return mat


def caminhoEuleriano(matriz):
    #organizando a matriz
    matriz = np.array(matriz)

    vertice = len(matriz)
    total = 0
    i = 0
    j = 0
    grau = 0

    #mostrar a matriz em que esta trabalhando
    print(matriz)
    print()


    while (total <= 2) and (i < vertice):
        grau = 0
        #calcula o grau do vertice
        for j in range(vertice):
            grau = matriz[i][j] + grau
        if grau%2 != 0:
            total = total + 1
        i = i + 1

    if total > 2:
        caminho = False
    else:
        caminho = True
    
    print(caminho)
    return caminho