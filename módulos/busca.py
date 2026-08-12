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
