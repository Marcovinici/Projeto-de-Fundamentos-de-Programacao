# Importando deque
from collections import deque 

# Função para printar matriz
def printMatriz(matriz, rota):
    for i, linha in enumerate(matriz):
        for j, coluna in enumerate(linha):
            # Se (i,j) pertencer a caminho, no lugar do espaço em branco é printado o +
            if (i, j) in rota:
                print("+", end="")
            else:
                print(coluna, end="")
        print()
        
# Função para construir a rota
def cria_rota(inicio, destino_encontrado, pais):
    rota = []
    while destino_encontrado != inicio:
        rota.append(destino_encontrado)
        destino_encontrado = pais[destino_encontrado]
    return rota

# Função validadora de coordenada(caminho):
# Checa se posição na matriz faz parte da estrada e se já não foi visitada
def validacao(linha, coluna, n, m, matriz, visitado):
    
    return linha >= 0 and linha < n and \
        coluna >= 0 and coluna < m and \
        matriz[linha][coluna] != '#' and \
        not visitado[linha][coluna]
